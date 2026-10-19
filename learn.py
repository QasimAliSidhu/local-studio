"""Offline companion runner. No account credentials or remote grading."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
CATALOG = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
PROGRESS = ROOT / 'progress.json'


def environment():
    env = os.environ.copy()
    paths = [str(ROOT / '.tools' / 'bin'), str(ROOT / '.tools' / 'go' / 'bin')]
    env['PATH'] = os.pathsep.join(paths + [env.get('PATH', '')])
    env['GOTOOLCHAIN'] = 'local'
    return env


def progress():
    return json.loads(PROGRESS.read_text()) if PROGRESS.exists() else {}


def exercise(ident):
    for item in CATALOG:
        if item['id'] == ident:
            return item
    raise SystemExit(f'Unknown exercise: {ident}. Run python learn.py list')


def currently_passes(item, data):
    result=data.get(item['id'],{})
    source=ROOT/item['folder']/item.get('source_filename','exercise.py' if item['language']=='python' else 'exercise.go')
    return bool(result.get('passed') and result.get('code_hash')==hashlib.sha256(source.read_text(encoding='utf-8').encode('utf-8')).hexdigest())


def check(item, folder=None, record=True):
    if folder is None and record:
        # Use the same grading, version hashes and earned credit as the web app.
        from ui_server import run_checks
        print(f'\nChecking {item["id"]}: {item["title"]}',flush=True)
        result=run_checks(item['id'])
        print(result['output'],end='')
        print('PASS' if result['passed'] else 'NOT YET: use the failing case as your next clue.',flush=True)
        return result['passed']
    folder = Path(folder or ROOT / item['folder'])
    if item['language'] == 'python':
        command = [sys.executable, '-m', 'unittest', 'discover', '-s', '.', '-p', 'test_exercise.py', '-v']
    else:
        go = shutil.which('go', path=environment()['PATH'])
        if not go:
            print('Go is unavailable. Run Start-Learning.cmd from the workspace folder.')
            return False
        command = [go, 'test', '-count=1', '-timeout=30s', '-v', '.']
    print(f'\nChecking {item["id"]}: {item["title"]}', flush=True)
    try:
        result = subprocess.run(command, cwd=folder, env=environment(), timeout=120)
        passed = result.returncode == 0
    except subprocess.TimeoutExpired:
        print('Check timed out. Look for an infinite loop or blocked worker.')
        passed = False
    if record:
        data = progress()
        data[item['id']] = {'passed': passed, 'checked_at': datetime.datetime.now().isoformat(timespec='seconds')}
        PROGRESS.write_text(json.dumps(data, indent=2), encoding='utf-8')
    print('PASS' if passed else 'NOT YET: implement the starter and try again.', flush=True)
    return passed


def main():
    parser = argparse.ArgumentParser(description='Python & Go local learning companion')
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('list', help='Show exercises and local check results')
    commands.add_parser('next', help='Show the suggested starting exercise')
    for name in ['show', 'hint', 'check']:
        command = commands.add_parser(name)
        command.add_argument('id', help='Exercise ID, e.g. py04 or go01')
    commands.add_parser('check-all', help='Check all starters; unfinished exercises will fail')
    commands.add_parser('courses', help='Show local courses')
    course = commands.add_parser('course', help='Show a local course brief')
    course.add_argument('number', type=int)
    args = parser.parse_args()
    if args.command == 'list':
        data = progress()
        for item in CATALOG:
            status = 'PASS' if currently_passes(item,data) else 'TODO'
            print(f'{item["id"]:5} {status:4} {item["title"]}')
    elif args.command == 'next':
        data=progress()
        item=next((item for item in CATALOG if item['language']=='python' and not currently_passes(item,data)),None)
        if item:
            print(f'Next unfinished Python mission: {item["id"]}')
            print((ROOT/item['folder']/'README.md').read_text(encoding='utf-8'))
        else:
            print('Every Python mission currently passes. Choose a Go lesson or ask your tutor for more practice.')
    elif args.command in ['show', 'hint', 'check']:
        item = exercise(args.id)
        if args.command == 'show':
            print((ROOT / item['folder'] / 'README.md').read_text(encoding='utf-8'))
        elif args.command == 'hint':
            print(item['hint'])
        else:
            return 0 if check(item) else 1
    elif args.command == 'check-all':
        outcomes = [check(item) for item in CATALOG]
        print(f'\n{sum(outcomes)}/{len(outcomes)} exercises passing.')
        return 0 if all(outcomes) else 1
    elif args.command == 'courses':
        courses = json.loads((ROOT / 'courses.json').read_text(encoding='utf-8'))
        for item in courses:
            print(f'{item["number"]:2}. {item["title"]} ({len(item["exercises"])} interactive challenges)')
    elif args.command == 'course':
        courses=json.loads((ROOT/'courses.json').read_text(encoding='utf-8'))
        selected=next((course for course in courses if course['number']==args.number),None)
        if selected is None:
            parser.error('That course is archived or unavailable. Use python learn.py courses for the active courses.')
        folder = ROOT/selected['folder']
        print((folder / 'README.md').read_text(encoding='utf-8'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
