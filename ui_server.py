"""Local, offline learning UI with file editing and Python/Go exercise checks."""
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
import argparse
import datetime
import hashlib
import json
import mimetypes
import os
import secrets
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
import webbrowser
from studio_tutor import Tutor, child_environment

ROOT = Path(__file__).resolve().parent
TOKEN = secrets.token_urlsafe(32)
STATE_LOCK = threading.Lock()
LOCKS = {}
TUTOR = None


def tutor_service():
    global TUTOR
    with STATE_LOCK:
        if TUTOR is None:
            TUTOR = Tutor(ROOT)
    return TUTOR


def tutor_context(scope, data):
    if scope.startswith('course-'):
        course = course_data(int(scope[7:]))
        context = {'title':course['title'],'lesson':course['instructions'][:24000],'notes':course['notes'][:4000]}
    else:
        item = exercise_data(scope)
        result = read_json(ROOT/'progress.json',{}).get(scope,{})
        context = {'title':item['title'],'language':item['language'],'lesson':item['lesson'][:16000],
                   'assignment':item['instructions'][:8000],'tests':item['tests'][:12000],
                   'last_test_output':result.get('output','')[:12000],
                   'execution_mode':item.get('execution_mode','function'),'stage':item.get('level',''),
                   'concepts_introduced':item.get('teaches',[]),
                   'previous_concepts':sorted({concept for earlier in catalog() if earlier.get('course_position',100000)<item.get('course_position',0) for concept in earlier.get('teaches',[])})}
    code = data.get('code','')
    quote = data.get('selection','')
    if not isinstance(code,str) or not isinstance(quote,str):
        raise ValueError('Expected text context')
    context.update({'current_code':code[:32000],'editor':data.get('editor','challenge'),
                    'selected_passage':quote[:4000],'current_console':str(data.get('console',''))[:12000]})
    return context


def playground_data(ident):
    item, _, _ = get_item(ident)
    folder = ROOT/'playgrounds'/ident
    folder.mkdir(parents=True,exist_ok=True)
    source = folder/('practice.py' if item['language']=='python' else 'main.go')
    if not source.exists():
        starter = '# Try a tutor exercise here. This file is separate from your challenge.\n\nprint("Ready to practice")\n' if item['language']=='python' else 'package main\n\nimport "fmt"\n\nfunc main() {\n\tfmt.Println("Ready to practice")\n}\n'
        source.write_text(starter,encoding='utf-8')
    code=source.read_text(encoding='utf-8')
    return {'code':code,'version':digest(code),'filename':source.name,'language':item['language']},source


def run_playground(ident):
    data, source=playground_data(ident)
    return run_program(data, source, playground=True)


def run_program(data, source, playground=False):
    """Execute a script for debugging without changing grades or completion."""
    env=child_environment()
    env['PATH']=str(ROOT/'.tools/go/bin')+os.pathsep+env.get('PATH','')
    env['GOTOOLCHAIN']='local'
    if data['language']=='python': command=[sys.executable,str(source)]
    else:
        go=shutil.which('go',path=env['PATH'])
        if not go: raise ValueError('Go is not available on this laptop')
        command=[go,'run',str(source)]
    started=time.monotonic()
    with tempfile.TemporaryFile() as output:
        options={'creationflags':subprocess.CREATE_NO_WINDOW} if os.name=='nt' else {'start_new_session':True}
        process=subprocess.Popen(command,cwd=source.parent,env=env,stdin=subprocess.DEVNULL,stdout=output,stderr=subprocess.STDOUT,**options)
        timed_out=False
        try:process.wait(timeout=30)
        except subprocess.TimeoutExpired:
            timed_out=True
            if os.name=='nt':subprocess.run(['taskkill','/PID',str(process.pid),'/T','/F'],capture_output=True,creationflags=subprocess.CREATE_NO_WINDOW)
            else:os.killpg(process.pid,signal.SIGKILL)
            process.wait(timeout=10)
        output.seek(0)
        text=output.read(128000).decode('utf-8','replace')
        if output.read(1):text+='\n[Output truncated at 128 KB]'
    if timed_out:text+='\nStopped after 30 seconds.'
    return {'passed':process.returncode==0 and not timed_out,'output':text,'duration':round(time.monotonic()-started,2),'checked_at':datetime.datetime.now().isoformat(timespec='seconds'),'code_hash':digest(data['code']),'playground':playground,'timed_out':timed_out,'graded':False,'xp_earned':0,'run_kind':'program'}


def read_json(path, default=None):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def learning_record():
    saved = read_json(ROOT / 'learning.json')
    if saved is not None:
        return saved
    # Retain credit for successful checks made before the learning dashboard existed.
    data = {'completed': {}, 'days': {}, 'goal': 2}
    for ident, result in read_json(ROOT / 'progress.json', {}).items():
        if result.get('passed') and result.get('checked_at'):
            day = result['checked_at'][:10]
            data['completed'][ident] = day
            data['days'].setdefault(day, []).append(ident)
    return data


def learning_summary(data=None):
    data = data if data is not None else learning_record()
    today = datetime.date.today()
    days = data['days']
    cursor = today if days.get(today.isoformat()) else today - datetime.timedelta(days=1)
    streak = 0
    while days.get(cursor.isoformat()):
        streak += 1
        cursor -= datetime.timedelta(days=1)
    week = []
    for offset in range(6, -1, -1):
        day = today - datetime.timedelta(days=offset)
        week.append({'date': day.isoformat(), 'label': day.strftime('%a'), 'count': len(days.get(day.isoformat(), [])), 'today': day == today})
    total_xp = len(data['completed']) * 100
    return {**data, 'xp': total_xp, 'level': total_xp // 500 + 1,
            'level_xp': total_xp % 500, 'streak': streak, 'week': week,
            'today_count': len(days.get(today.isoformat(), [])), 'today': today.isoformat()}


def write_learning(data):
    temp = ROOT / 'learning.json.saving'
    temp.write_text(json.dumps(data, indent=2), encoding='utf-8')
    temp.replace(ROOT / 'learning.json')


def catalog():
    return read_json(ROOT / 'catalog.json', [])


def get_item(ident):
    item = next((item for item in catalog() if item['id'] == ident), None)
    if item is None:
        raise ValueError('Unknown exercise')
    folder = (ROOT / item['folder']).resolve()
    if not folder.is_relative_to(ROOT / 'exercises'):
        raise ValueError('Invalid exercise folder')
    extension = 'py' if item['language'] == 'python' else 'go'
    filename=item.get('source_filename',f'exercise.{extension}')
    if not isinstance(filename,str) or Path(filename).name!=filename or Path(filename).suffix!='.'+extension:
        raise ValueError('Invalid source filename')
    return item, folder, folder / filename


def exercise_data(ident):
    item, folder, source = get_item(ident)
    code = source.read_text(encoding='utf-8')
    tests = folder / ('test_exercise.py' if item['language'] == 'python' else 'exercise_test.go')
    return {**item, 'code': code, 'version': digest(code), 'filename': source.name,
            'instructions': (folder / 'README.md').read_text(encoding='utf-8'),
            'lesson': (folder / 'lesson.md').read_text(encoding='utf-8') if (folder / 'lesson.md').exists() else (folder / 'README.md').read_text(encoding='utf-8'),
            'tests': tests.read_text(encoding='utf-8')}


def course_data(number):
    course = next((course for course in read_json(ROOT / 'courses.json', []) if course['number'] == number), None)
    if course is None:
        raise ValueError('Unknown course')
    folder = next((ROOT / 'courses').glob(f'{number:02}-*'))
    notes = (folder / 'notes.md').read_text(encoding='utf-8')
    return {**course, 'number': number,
            'instructions': (folder / 'README.md').read_text(encoding='utf-8'),
            'notes': notes, 'version': digest(notes)}


def lock_for(ident):
    with STATE_LOCK:
        return LOCKS.setdefault(ident, threading.Lock())


def save_file(path, code, version, ident):
    if not isinstance(code, str) or len(code.encode('utf-8')) > 256000:
        raise ValueError('Keep files under 256 KB')
    previous = path.read_text(encoding='utf-8')
    if digest(previous) != version:
        raise FileExistsError('This file changed outside the UI. Reload it before saving; your draft is still in the editor.')
    if code != previous:
        history = ROOT / '.history' / ident
        history.mkdir(parents=True, exist_ok=True)
        stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
        (history / f'{stamp}-{path.name}').write_text(previous, encoding='utf-8')
        temp_path = path.with_name(path.name + '.saving')
        temp_path.write_text(code, encoding='utf-8')
        temp_path.replace(path)
    return digest(code)


def run_checks(ident, record=True):
    item, folder, source = get_item(ident)
    code_hash = digest(source.read_text(encoding='utf-8'))
    env = child_environment()
    env['PATH'] = os.pathsep.join([str(ROOT / '.tools/bin'), str(ROOT / '.tools/go/bin'), env.get('PATH', '')])
    env['GOTOOLCHAIN'] = 'local'
    env.pop('STUDIO_SCRIPT_OUTPUT',None)
    if item['language'] == 'python':
        command = [sys.executable, '-m', 'unittest', 'discover', '-s', '.', '-p', 'test_exercise.py', '-v']
    else:
        go = shutil.which('go', path=env['PATH'])
        if not go:
            raise ValueError('Go was not found in the local toolchain')
        command = [go, 'test', '-count=1', '-timeout=25s', '-v', '.']
    started = time.monotonic()
    timed_out = False
    program_output=None
    with tempfile.TemporaryDirectory(prefix='studio-script-run-') as run_directory, tempfile.TemporaryFile() as output:
        script_result=Path(run_directory)/'program-output.json'
        if item.get('execution_mode')=='script':env['STUDIO_SCRIPT_OUTPUT']=str(script_result)
        options = {'creationflags': subprocess.CREATE_NO_WINDOW} if os.name == 'nt' else {'start_new_session': True}
        process = subprocess.Popen(command, cwd=folder, env=env, stdout=output, stderr=subprocess.STDOUT, **options)
        try:
            process.wait(timeout=90)
        except subprocess.TimeoutExpired:
            timed_out = True
            if os.name == 'nt':
                subprocess.run(['taskkill', '/PID', str(process.pid), '/T', '/F'], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                os.killpg(process.pid, signal.SIGKILL)
            process.wait(timeout=10)
        output.seek(0)
        text = output.read(128000).decode('utf-8', errors='replace')
        if output.read(1):
            text += '\n[Output truncated at 128 KB]'
        if script_result.exists():
            try:
                value=json.loads(script_result.read_text(encoding='utf-8')).get('stdout')
                if isinstance(value,str):program_output=value[:128000]
            except (ValueError,OSError):pass
    if timed_out:
        text += '\nThe check stopped after 90 seconds. Look for a loop or blocked worker.'
    result = {'passed': process.returncode == 0 and not timed_out,
              'checked_at': datetime.datetime.now().isoformat(timespec='seconds'),
              'duration': round(time.monotonic() - started, 2), 'code_hash': code_hash,
              'output': text, 'timed_out': timed_out,'content_revision':item.get('content_revision',1)}
    if program_output is not None:
        result['program_output']=program_output
        result['output']=program_output+'\nChecks:\n'+text
    result.update(graded=record,run_kind='tests',xp_earned=0)
    if not record:
        return result
    with STATE_LOCK:
        learning = learning_record()
        xp_earned = 0
        if result['passed']:
            today = datetime.date.today().isoformat()
            if ident not in learning['completed']:
                learning['completed'][ident] = today
                xp_earned = 100
            activity = learning['days'].setdefault(today, [])
            if ident not in activity:
                activity.append(ident)
            write_learning(learning)
        result['xp_earned'] = xp_earned
        data = read_json(ROOT / 'progress.json', {})
        data[ident] = result
        path = ROOT / 'progress.json'
        temp = path.with_suffix('.json.saving')
        temp.write_text(json.dumps(data, indent=2), encoding='utf-8')
        temp.replace(path)
    return result


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def allowed_host(self):
        host = self.headers.get('Host')
        local = f'127.0.0.1:{self.server.server_port}'
        config = read_json(ROOT / 'hosting.json', {})
        origin = config.get('origin', '')
        remote = urlparse(origin).netloc
        proxied = bool(self.headers.get('Tailscale-User-Login') or self.headers.get('X-Forwarded-For') or host == remote)
        if self.client_address[0] not in ('127.0.0.1', '::1'):
            return False
        if not proxied:
            return host == local
        # Tailscale Serve removes spoofed identity headers before injecting its own.
        # The backend remains loopback-only; only this configured identity may execute code.
        login = self.headers.get('Tailscale-User-Login', '').casefold()
        return bool(origin.startswith('https://') and remote and host in (local, remote)
                    and login in [value.casefold() for value in config.get('allowed_logins', [])])

    def allowed_origin(self):
        origin = self.headers.get('Origin')
        local = f'http://127.0.0.1:{self.server.server_port}'
        if self.headers.get('Tailscale-User-Login'):
            return origin == read_json(ROOT / 'hosting.json', {}).get('origin')
        return origin in (None, local)

    def respond(self, data, status=200, content_type='application/json; charset=utf-8'):
        body = json.dumps(data).encode() if content_type.startswith('application/json') else data
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'same-origin')
        self.send_header('Content-Security-Policy', f"default-src 'self'; script-src 'self'; style-src 'self' 'nonce-{TOKEN}'; style-src-attr 'unsafe-inline'; font-src 'self'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if not self.allowed_host():
            return self.respond({'error': 'Invalid host'}, 403)
        path = urlparse(self.path).path
        try:
            assets = {'/': ('studio.html', 'text/html'), '/studio.css': ('studio.css', 'text/css')}
            if path in assets:
                filename, mime = assets[path]
                text = (ROOT / 'ui' / filename).read_text(encoding='utf-8').replace('__WORKSPACE_TOKEN__', TOKEN)
                return self.respond(text.encode(), content_type=mime + '; charset=utf-8')
            if path.startswith('/assets/'):
                asset = (ROOT / 'ui' / path.lstrip('/')).resolve()
                if not asset.is_relative_to((ROOT / 'ui' / 'assets').resolve()) or not asset.is_file():
                    return self.respond({'error': 'Not found'}, 404)
                mime = {'.js': 'text/javascript', '.css': 'text/css', '.woff2': 'font/woff2', '.txt': 'text/plain'}.get(asset.suffix, mimetypes.guess_type(asset.name)[0] or 'application/octet-stream')
                return self.respond(asset.read_bytes(), content_type=mime)
            if path == '/api/bootstrap':
                data = read_json(ROOT / 'progress.json', {})
                # A passed check is current only while its checked source remains unchanged.
                for ident, result in data.items():
                    try:
                        _, _, source = get_item(ident)
                        result['stale'] = result.get('code_hash') != digest(source.read_text(encoding='utf-8'))
                    except ValueError:
                        result['stale'] = True
                return self.respond({'app': 'backend-workshop', 'workspace': str(ROOT), 'catalog': catalog(), 'courses': read_json(ROOT / 'courses.json', []), 'progress': data, 'learning': learning_summary(), 'resume':read_json(ROOT/'workspace-state.json',{})})
            parts = path.strip('/').split('/')
            if path == '/api/tutor/status':
                return self.respond(tutor_service().status())
            if len(parts)==3 and parts[:2]==['api','tutor']:
                tutor_context(parts[2],{})
                return self.respond(tutor_service().history(parts[2]))
            if len(parts)==4 and parts[:3]==['api','tutor','jobs']:
                return self.respond(tutor_service().job(parts[3]))
            if len(parts)==3 and parts[:2]==['api','playgrounds']:
                return self.respond(playground_data(parts[2])[0])
            if len(parts) == 3 and parts[:2] == ['api', 'exercises']:
                return self.respond(exercise_data(parts[2]))
            if len(parts) == 4 and parts[:2] == ['api', 'exercises'] and parts[3] == 'solution':
                item, _, _ = get_item(parts[2])
                extension = 'py' if item['language'] == 'python' else 'go'
                return self.respond({'code': (ROOT / 'reference-solutions' / f'{item["id"]}.{extension}.txt').read_text(encoding='utf-8')})
            if len(parts) == 3 and parts[:2] == ['api', 'courses']:
                return self.respond(course_data(int(parts[2])))
            return self.respond({'error': 'Not found'}, 404)
        except (ValueError, StopIteration, FileNotFoundError):
            return self.respond({'error': 'Item not found'}, 404)

    def do_POST(self):
        if not self.allowed_host() or self.headers.get('X-Workspace-Token') != TOKEN or not self.allowed_origin():
            return self.respond({'error': 'Request rejected'}, 403)
        lock = None
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if length < 0 or length > 300000 or self.headers.get('Content-Type', '').split(';')[0] != 'application/json':
                return self.respond({'error': 'Expected JSON under 300 KB'}, 400)
            data = json.loads(self.rfile.read(length))
            if not isinstance(data, dict):
                raise ValueError('Expected an object')
            if urlparse(self.path).path == '/api/session':
                route=data.get('route','')
                if not isinstance(route,str):raise ValueError('Expected a lesson route')
                if route.startswith('exercise/'):get_item(route[9:])
                elif route.startswith('course/'):course_data(int(route[7:]))
                else:raise ValueError('Unknown lesson route')
                with STATE_LOCK:
                    temp=ROOT/'workspace-state.json.saving'
                    session=read_json(ROOT/'workspace-state.json',{})
                    last_exercises=session.get('last_exercises',{})
                    if not isinstance(last_exercises,dict):last_exercises={}
                    if route.startswith('exercise/'):
                        ident=route[9:]
                        for course in read_json(ROOT/'courses.json',[]):
                            if ident in course.get('exercises',[]):
                                last_exercises[str(course['number'])]=ident
                    session.update(route=route,updated=datetime.datetime.now().isoformat(timespec='seconds'),last_exercises=last_exercises)
                    temp.write_text(json.dumps(session),encoding='utf-8')
                    temp.replace(ROOT/'workspace-state.json')
                return self.respond({'saved':True})
            request_parts=urlparse(self.path).path.strip('/').split('/')
            if len(request_parts)==3 and request_parts[:2]==['api','tutor']:
                context=tutor_context(request_parts[2],data)
                return self.respond(tutor_service().submit(request_parts[2],data.get('question'),context,data.get('mode','question')),202)
            if len(request_parts)==4 and request_parts[:2]==['api','playgrounds'] and request_parts[3] in ('save','run'):
                ident,action=request_parts[2:]
                _,source=playground_data(ident)
                lock=lock_for('playground-'+ident)
                if not lock.acquire(blocking=False):
                    lock=None
                    return self.respond({'error':'This playground is running. Try again when it finishes.'},409)
                version=save_file(source,data.get('code'),data.get('version'),'playground-'+ident)
                if action=='save':return self.respond({'version':version})
                return self.respond({'version':version,'result':run_playground(ident)})
            if urlparse(self.path).path == '/api/learning/goal':
                goal = data.get('goal')
                if type(goal) is not int or goal not in (1, 2, 3):
                    raise ValueError('Choose a daily goal of 1, 2, or 3 challenges')
                with STATE_LOCK:
                    learning = learning_record()
                    learning['goal'] = goal
                    write_learning(learning)
                return self.respond({'learning': learning_summary(learning)})
            parts = urlparse(self.path).path.strip('/').split('/')
            if len(parts) != 4 or parts[0] != 'api':
                return self.respond({'error': 'Not found'}, 404)
            ident, action = parts[2:]
            if parts[1] == 'exercises' and action in ('save', 'run', 'submit'):
                item, _, source = get_item(ident)
                lock = lock_for(ident)
                if not lock.acquire(blocking=False):
                    lock = None
                    return self.respond({'error': 'This exercise is already running. Try again when it finishes.'}, 409)
                version = save_file(source, data.get('code'), data.get('version'), ident)
                if action == 'save':
                    return self.respond({'version': version})
                if action=='run' and item.get('execution_mode')=='script':
                    result=run_program({'language':item['language'],'code':source.read_text(encoding='utf-8')},source)
                else:
                    result = run_checks(ident, record=action=='submit')
                return self.respond({'version': version, 'result': result, 'learning': learning_summary()})
            if parts[1] == 'courses' and action == 'notes':
                number = int(ident)
                course_data(number)
                folder = next((ROOT / 'courses').glob(f'{number:02}-*'))
                lock = lock_for('notes-' + ident)
                if not lock.acquire(blocking=False):
                    lock = None
                    return self.respond({'error': 'Notes are being saved. Try again.'}, 409)
                version = save_file(folder / 'notes.md', data.get('notes'), data.get('version'), 'course-' + ident)
                return self.respond({'version': version})
            return self.respond({'error': 'Not found'}, 404)
        except FileExistsError as error:
            return self.respond({'error': str(error)}, 409)
        except (ValueError, KeyError, StopIteration) as error:
            return self.respond({'error': str(error)}, 400)
        except Exception:
            return self.respond({'error': 'The operation failed. Check file access and try again.'}, 500)
        finally:
            if lock is not None:
                lock.release()


def main():
    parser = argparse.ArgumentParser(description='Local interactive Python & Go learning workspace')
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--open', action='store_true')
    args = parser.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    server.daemon_threads = True
    url = f'http://127.0.0.1:{server.server_port}'
    print('Local Studio: ' + url, flush=True)
    if args.open:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
