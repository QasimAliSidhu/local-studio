"""Verify reference solutions in a temporary workspace, keeping learner files untouched."""
from pathlib import Path
from tempfile import TemporaryDirectory
import ast, json, os, shutil, sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import ui_server

def main():
    catalog=json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'))
    assert len(catalog)==len({item['id'] for item in catalog})==123
    assert sum(item['language']=='python' for item in catalog)==115
    courses=json.loads((ROOT/'courses.json').read_text(encoding='utf-8'))
    first=next(course for course in courses if course['number']==1)['exercises'][:17]
    by_id={item['id']:item for item in catalog}
    for ident in first:
        item=by_id[ident]
        assert item['execution_mode']=='script'
        code=(ROOT/item['folder']/item['source_filename']).read_text(encoding='utf-8')
        assert not any(isinstance(node,(ast.FunctionDef,ast.ClassDef)) for node in ast.walk(ast.parse(code))),ident
    go=shutil.which('go')
    outcomes=[]
    with TemporaryDirectory(prefix='local-studio-release-') as directory:
        workspace=Path(directory)
        shutil.copytree(ROOT/'exercises',workspace/'exercises',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        shutil.copyfile(ROOT/'catalog.json',workspace/'catalog.json')
        ui_server.ROOT=workspace
        for item in catalog:
            if item['language']=='go' and not go:
                continue
            suffix='py' if item['language']=='python' else 'go'
            source=workspace/item['folder']/item.get('source_filename','exercise.'+suffix)
            source.write_text((ROOT/'reference-solutions'/(item['id']+'.'+suffix+'.txt')).read_text(encoding='utf-8'),encoding='utf-8')
            result=ui_server.run_checks(item['id'],record=False)
            if not result['passed']:
                print(item['id']+' FAILED\n'+result['output'],flush=True)
                return 1
            outcomes.append(item['id'])
            if len(outcomes)%20==0:print(f'{len(outcomes)} reference solutions passed',flush=True)
        item=by_id['py101'];source=workspace/item['folder']/item['source_filename']
        source.write_text('print("Hello!")\n',encoding='utf-8')
        wrong=ui_server.run_checks('py101',record=False)
        assert not wrong['passed'] and wrong['program_output']=='Hello!\n'
        source.write_text('print("Helpdesk online!")\n',encoding='utf-8')
        correct=ui_server.run_checks('py101',record=False)
        assert correct['passed'] and correct['program_output']=='Helpdesk online!\n'
        assert not (workspace/'progress.json').exists()
    print(json.dumps({'references_passed':len(outcomes),'python_passed':115,'go_passed':8 if go else 0,'go_skipped':0 if go else 8,'first_17_plain_scripts':True,'wrong_output_rejected':True,'correct_output_passed':True,'learner_files_modified':False}),flush=True)
    if not go:print('Go is not on PATH; Go reference checks were skipped.',flush=True)
    return 0

if __name__=='__main__':
    raise SystemExit(main())
