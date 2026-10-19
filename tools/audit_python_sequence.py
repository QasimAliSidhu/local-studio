"""Check syntax prerequisites in learner-visible code, not in grading machinery."""
import ast
import json
import re
from pathlib import Path

from python_curriculum import LESSONS as BASE
from python_path_v2 import PATH, revised_path


def features(source):
    try:tree=ast.parse(source)
    except SyntaxError:return set()  # An explicitly discussed fragment is not a runnable program.
    used=set()
    for node in ast.walk(tree):
        kind=type(node)
        names={ast.Assign:'variables',ast.AugAssign:'variables',ast.BinOp:'arithmetic',
            ast.FunctionDef:'functions',ast.Return:'returns',ast.If:'branches',ast.IfExp:'branches',
            ast.Compare:'comparisons',ast.BoolOp:'logic',ast.List:'lists',ast.Tuple:'tuples',
            ast.Dict:'dictionaries',ast.Set:'sets',ast.For:'loops',ast.While:'while_loops',
            ast.Break:'loop_control',ast.Continue:'loop_control',ast.ListComp:'comprehensions',
            ast.DictComp:'comprehensions',ast.SetComp:'comprehensions',ast.GeneratorExp:'generators',
            ast.Lambda:'lambdas',ast.Import:'modules',ast.ImportFrom:'modules',ast.Raise:'raising',
            ast.Try:'exception_handling',ast.With:'context_managers',ast.ClassDef:'classes',
            ast.AnnAssign:'annotations',ast.Nonlocal:'closures',ast.Global:'global_state',
            ast.Yield:'generators',ast.Assert:'assertions',ast.AsyncFunctionDef:'async',ast.Await:'async',
            ast.JoinedStr:'fstrings'}
        if kind in names:used.add(names[kind])
        if isinstance(node,ast.Constant):
            if node.value is None:used.add('none')
            elif isinstance(node.value,bool):used.add('booleans')
            elif isinstance(node.value,str):used.add('strings')
        if isinstance(node,ast.Subscript):used.add('slicing' if isinstance(node.slice,ast.Slice) else 'indexing')
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.Not):used.add('logic')
        if isinstance(node,ast.BinOp):
            if isinstance(node.op,(ast.FloorDiv,ast.Mod)):used.add('integer_division')
            if isinstance(node.op,ast.Pow):used.add('powers')
            if isinstance(node.op,(ast.BitAnd,ast.BitOr,ast.BitXor,ast.LShift,ast.RShift)):
                # The union spelling in a type annotation is introduced with annotations.
                used.add('bitwise')
        if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):
            if node.args.args or node.args.kwonlyargs:used.add('parameters')
            if node.args.vararg or node.args.kwarg:used.add('argument_unpacking')
            if node.returns or any(arg.annotation for arg in node.args.args):used.add('annotations')
            if any(isinstance(child,(ast.FunctionDef,ast.AsyncFunctionDef)) for statement in node.body for child in ast.walk(statement)):
                used.add('closures')
            for decorator in node.decorator_list:
                name=decorator.func.id if isinstance(decorator,ast.Call) and isinstance(decorator.func,ast.Name) else decorator.id if isinstance(decorator,ast.Name) else ''
                used.add({'property':'properties','dataclass':'dataclasses'}.get(name,'decorators'))
        if isinstance(node,ast.Call):
            if isinstance(node.func,ast.Name) and node.func.id=='print':used.add('print')
            if any(isinstance(arg,ast.Starred) for arg in node.args) or any(key.arg is None for key in node.keywords):used.add('argument_unpacking')
        if isinstance(node,ast.Dict) and any(key is None for key in node.keys):used.add('mapping_unpacking')
    return used


def audit(root):
    lessons=revised_path(BASE)
    available=set();results=[];errors=[]
    for title,level,ids in PATH:
        for ident in ids:
            item=lessons.get(ident)
            if item:
                introduced=set(item['teaches']);declared=set(item['requires'])
                code='\n\n'.join(item[name] for name in ['starter','solution','example'])
                used=set().union(*(features(item[name]) for name in ['starter','solution','example']))
                # Annotations use bitwise-looking union syntax, not numeric permission masks.
                if 'annotations' in introduced or 'annotations' in available:used.discard('bitwise')
                if 'set_operations' in introduced:
                    used.discard('bitwise');used.add('set_operations')
                # Method self parameters arrive with the first class definition.
                if 'classes' in introduced:used.discard('parameters')
                missing=(used|declared)-(available|introduced)
                if missing:errors.append({'id':ident,'title':item['title'],'missing':sorted(missing)})
                available|=introduced
            else:
                reference=root/'reference-solutions'/f'{ident}.py.txt'
                used=features(reference.read_text(encoding='utf-8'))
                missing=used-available
                if missing:errors.append({'id':ident,'missing':sorted(missing)})
            results.append({'id':ident,'stage':level,'syntax_used':sorted(used),'prerequisites_available':not missing})
    if errors:
        print(json.dumps(errors,indent=2))
        raise ValueError('Learner-visible code uses syntax before its introduction')
    first_definition=next(row['id'] for row in results if row['id'] in lessons and 'functions' in lessons[row['id']]['teaches'])
    assert first_definition=='py184'
    return {'passed':True,'lessons_reviewed':len(results),'first_custom_function':'py184','checks':results,
        'limits':'This checks syntax order and declared dependencies. Teaching clarity also requires reading the explanations and trying the course as a beginner.'}


if __name__=='__main__':
    root=Path(__file__).resolve().parents[1]
    result=audit(root)
    (root/'PYTHON-SEQUENCE-AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print('PASS: prerequisite sequence for',result['lessons_reviewed'],'lessons')
