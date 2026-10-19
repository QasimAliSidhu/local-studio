"""Build a prerequisite-first Python course while preserving earlier learner files."""
from pathlib import Path
from textwrap import dedent, indent
from tempfile import TemporaryDirectory
import datetime
import hashlib
import json
import re
import shutil
import subprocess
import sys
from html import escape

from python_curriculum import LESSONS as BASE
from python_path_v2 import PATH, revised_path
from audit_python_sequence import audit
from lesson_concepts import CONCEPTS
from python_readability import reading_sections, task_bullets

ROOT=Path(__file__).resolve().parents[1]
LEGACY_STARTERS={item['id']:item['starter'] for item in BASE}
LESSON_MAP=revised_path(BASE)
ORDER=[ident for _,_,ids in PATH for ident in ids]
LESSONS=[LESSON_MAP[ident] for ident in ORDER if ident in LESSON_MAP]
CHAPTERS=[(title,level) for title,level,_ in PATH]
IMPORTS='''import unittest
import asyncio
import json
import os
import runpy
from io import StringIO
from contextlib import redirect_stdout
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import get_type_hints
from unittest.mock import Mock, patch
'''


def test_source(lesson):
    text=IMPORTS
    if lesson['execution_mode']=='script':
        text+='''

class MissionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        output=StringIO()
        try:
            with redirect_stdout(output):
                cls.state=runpy.run_path(str(Path(__file__).with_name("main.py")),run_name="__main__")
        finally:
            cls.output=output.getvalue()
            result_file=os.environ.get("STUDIO_SCRIPT_OUTPUT")
            if result_file:
                Path(result_file).write_text(json.dumps({"stdout":cls.output}),encoding="utf-8")
            else:
                print(cls.output,end="",flush=True)
'''
    else:
        text+='from challenge import *\n\n\nclass MissionTests(unittest.TestCase):\n'
    for name,body in lesson['checks']:
        if lesson['execution_mode']=='function':
            body=body.replace('exercise.','challenge.').replace('import exercise','import challenge')
        text+=f'    def test_{name}(self):\n'+indent(dedent(body).strip(),'        ')+'\n\n'
    return text+'\nif __name__ == "__main__":\n    unittest.main()\n'


def lesson_source(lesson):
    teaching,more=reading_sections(lesson)
    output=''
    if lesson.get('example_output') is not None:
        output='<div class="example-output"><span>Console output</span><pre>'+escape(lesson['example_output'])+'</pre></div>\n\n'
    return (f"# {lesson['title']}\n\n{lesson['goal']}\n\n"
        f"{teaching}\n\n"
        f"## Walk through an example\n\n```python\n{lesson['example']}\n```\n\n"
        f"{output}"
        f"{more}"
        f"## Before you run\n\n{lesson['reflection']}\n\n"
        'Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. '
        'Hints and a reference solution are available after you try. Your work stays saved on the laptop.\n')


def task_source(lesson):
    mode='This is a **script**: Run executes its instructions. Write the requested instructions directly in the file.' if lesson['execution_mode']=='script' else 'This is a **function challenge**: Run calls the tests for debugging without completion credit. Follow the function\'s return-value contract.'
    if lesson['id'] in ['py101','py102','py103','py104']:
        mode='Write directly in **main.py**, then press **Run** to see the output. No function definition is needed.'
    return f"# {lesson['title']}\n\n## Your mission\n\n{task_bullets(lesson['task'])}\n\n{mode}\n\n**Run** to experiment and debug. **Submit answer** checks your work and saves completion when all checks pass.\n"


def fixture_files(folder,lesson):
    for name,content in lesson.get('fixtures',{}).items():
        path=folder/name
        if not path.exists():path.write_text(content,encoding='utf-8')


def validate():
    sequence=audit(ROOT)
    results=[]
    with TemporaryDirectory(prefix='python-course-v2-check-') as directory:
        base=Path(directory)
        for position,lesson in enumerate(LESSONS,1):
            folder=base/lesson['id'];folder.mkdir()
            source=folder/lesson['source_filename']
            tests=test_source(lesson)
            compile(tests,str(folder/'test_exercise.py'),'exec')
            compile(lesson['starter'],str(source),'exec')
            (folder/'test_exercise.py').write_text(tests,encoding='utf-8')
            fixture_files(folder,lesson)
            for variant in ['solution','starter']:
                source.write_text(lesson[variant],encoding='utf-8')
                shutil.rmtree(folder/'__pycache__',ignore_errors=True)
                run=subprocess.run([sys.executable,'-B','-m','unittest','discover','-v'],cwd=folder,capture_output=True,text=True,timeout=20)
                if (variant=='solution') != (run.returncode==0):
                    raise RuntimeError(f"{lesson['id']} {variant} behaved incorrectly:\n{run.stdout}\n{run.stderr}")
            results.append({'id':lesson['id'],'tests':len(lesson['checks']),'reference_passed':True,'starter_requires_work':True,'mode':lesson['execution_mode']})
            if position%20==0:print(f'Validated {position}/{len(LESSONS)} authored lessons...',flush=True)
        catalog=json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'))
        for ident in ORDER:
            if ident in LESSON_MAP:continue
            item=next(item for item in catalog if item['id']==ident)
            folder=base/ident
            shutil.copytree(ROOT/item['folder'],folder,ignore=shutil.ignore_patterns('__pycache__'))
            (folder/'exercise.py').write_text((ROOT/'reference-solutions'/f'{ident}.py.txt').read_text(encoding='utf-8'),encoding='utf-8')
            run=subprocess.run([sys.executable,'-B','-m','unittest','discover','-v'],cwd=folder,capture_output=True,text=True,timeout=20)
            if run.returncode:raise RuntimeError(ident+'\n'+run.stderr)
            count=int(re.search(r'Ran (\d+) tests?',run.stderr).group(1))
            results.append({'id':ident,'tests':count,'reference_passed':True,'existing':True})
    record={'checked_at':datetime.datetime.now().isoformat(timespec='seconds'),'curriculum_version':2,
        'python_lessons':len(ORDER),'authored_lessons':len(LESSONS),'chapters':len(PATH),
        'script_lessons':sum(item['execution_mode']=='script' for item in LESSONS),
        'test_methods':sum(item['tests'] for item in results),'all_references_passed':True,
        'all_starters_require_work':True,'prerequisites_audited':True,'results':results}
    (ROOT/'PYTHON-COURSE-VALIDATION.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
    (ROOT/'PYTHON-SEQUENCE-AUDIT.json').write_text(json.dumps(sequence,indent=2),encoding='utf-8')
    print(f"PASS: {len(ORDER)} references, {record['test_methods']} test methods, and a prerequisite-first syntax audit.",flush=True)
    return record


def install():
    stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    backup=ROOT/'.history'/f'python-teaching-v2-{stamp}';backup.mkdir(parents=True)
    readme=Path('courses/01-python-foundations/README.md')
    for relative in [Path('catalog.json'),Path('courses.json'),readme]:
        target=backup/relative;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/relative,target)
    protected=[path for path in (ROOT/'exercises').rglob('*.py') if path.name!='test_exercise.py']
    protected+=list((ROOT/'exercises').rglob('exercise.go'))+list((ROOT/'courses').glob('*/notes.md'))
    protected += [ROOT/name for name in ['progress.json','learning.json','workspace-state.json'] if (ROOT/name).exists()]
    before={str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest() for path in protected}
    catalog=json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'));by_id={item['id']:item for item in catalog}
    for lesson in LESSONS:
        folder=ROOT/'exercises/python'/lesson['id'];folder.mkdir(parents=True,exist_ok=True)
        source=folder/lesson['source_filename']
        if not source.exists():
            code=lesson['starter']
            old=folder/'exercise.py'
            # Earlier function attempts are copied when the contract is unchanged; never erased.
            if old.exists() and lesson['execution_mode']=='function' and old.read_text(encoding='utf-8').strip()!=LEGACY_STARTERS.get(lesson['id'],'').strip():
                code=old.read_text(encoding='utf-8')
            source.write_text(code,encoding='utf-8')
        fixture_files(folder,lesson)
        for name,content in [('lesson.md',lesson_source(lesson)),('README.md',task_source(lesson)),('test_exercise.py',test_source(lesson))]:
            target=folder/name
            if target.exists():
                saved=backup/target.relative_to(ROOT);saved.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(target,saved)
            target.write_text(content,encoding='utf-8')
        reference=ROOT/'reference-solutions'/f"{lesson['id']}.py.txt"
        if reference.exists():
            saved=backup/reference.relative_to(ROOT);saved.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(reference,saved)
        reference.write_text(lesson['solution'],encoding='utf-8')
        item=by_id.get(lesson['id'],{})
        item.update({key:lesson[key] for key in ['id','title','chapter','chapter_title','level','execution_mode','source_filename','content_revision','teaches','requires']})
        item.update(language='python',folder=str(folder.relative_to(ROOT)).replace('\\','/'),hint=lesson['hint'],objective=lesson['goal'],kind='mission',lesson_layout='teach-first')
        by_id[item['id']]=item
    chapters=[]
    for number,(title,level,ids) in enumerate(PATH,1):
        chapters.append({'number':number,'title':title,'level':level,'description':level+' · '+title,'lessons':ids})
        for position,ident in enumerate(ids,1):by_id[ident].update(chapter=number,chapter_title=title,chapter_position=position,level=level,lesson_layout='teach-first')
    for position,ident in enumerate(ORDER,1):by_id[ident]['course_position']=position
    catalog=[by_id[ident] for ident in ORDER]+[item for item in catalog if item['id'] not in ORDER]
    for item in catalog:item['concept']=CONCEPTS[item['id']]
    courses=json.loads((ROOT/'courses.json').read_text(encoding='utf-8'))
    python_course=next(course for course in courses if course['number']==1)
    python_course.update(title='Python: foundations to backend',exercises=ORDER,chapters=chapters,curriculum_version=2,
        description='Start with one line of Python. Learn each prerequisite before functions, collections, objects, advanced patterns and backend practice.',
        core_chapters=13,core_lessons=sum(len(ids) for _,_,ids in PATH[:13]))
    syllabus='\n'.join(f"- **{number}. {title}** ({level}): {len(ids)} missions" for number,(title,level,ids) in enumerate(PATH,1))
    (ROOT/readme).write_text('# Python: foundations to backend\n\n'
        f'**{len(ORDER)} interactive lessons across {len(PATH)} chapters.**\n\n'
        '## Start from zero\n\nThe opening lessons run plain scripts. Learn what the editor, console, strings and print mean, then change a working example. '
        'Variables, numbers and text come next. Custom functions are introduced in separate definition, parameter and return-value lessons before function challenges.\n\n'
        '## How to learn\n\nRead the explanation, walk through the example, predict the result, then try the mission. Run executes scripts or runs function tests without completion credit. Submit answer grades the requested behavior and saves completion on success. '
        'Ask the tutor whenever a word or line is unfamiliar. Hints come before optional reference solutions. Experiments in Extra practice keep your challenge separate.\n\n'
        '## Progression\n\nFoundation chapters teach basic syntax. Core Python adds collections, loops, errors, hints and mutation. Intermediate chapters cover modules, objects and functional tools. '
        'Advanced Python patterns include closures, argument forwarding, decorators and context managers. Backend practice applies files, JSON, CSV, SQLite, caching and asynchronous work. '
        'This is a learning path through those topics, not a claim that finishing it makes someone an expert in every Python framework.\n\n'
        '## Your existing work\n\nEarlier code files are retained. Revised missions use new working filenames so an old function wrapper does not remain in a first-day script. '
        'Edited function attempts are carried forward when their contract is unchanged. Old browser drafts remain stored separately by content revision. Completion credit, notes and conversations are retained.\n\n'
        '## Chapters\n\n'+syllabus+'\n',encoding='utf-8')
    (ROOT/'catalog.json').write_text(json.dumps(catalog,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    (ROOT/'courses.json').write_text(json.dumps(courses,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    after={str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest() for path in protected}
    assert before==after,'An earlier learner file changed during the installation'
    (ROOT/'.tools/teaching-v2-preservation.json').write_text(json.dumps({'unchanged':True,'files':before,'backup':str(backup)},indent=2),encoding='utf-8')
    print(f'Installed teaching v2: {len(ORDER)} lessons; all {len(before)} earlier learner files retained.',flush=True)


if __name__=='__main__':
    validate()
    if '--check-only' not in sys.argv:install()
