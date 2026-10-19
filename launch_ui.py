"""Start the local learning application quietly and open its browser UI."""
from pathlib import Path
import json
import os
import subprocess
import sys
import time
import urllib.request
import webbrowser

ROOT = Path(__file__).resolve().parent
URL = 'http://127.0.0.1:8765'


def ready():
    try:
        with urllib.request.urlopen(URL + '/api/bootstrap', timeout=1) as response:
            result = json.load(response)
            return result.get('app') == 'backend-workshop' and result.get('workspace') == str(ROOT)
    except (OSError, ValueError):
        return False


def main():
    if not ready():
        interpreter = Path(sys.executable)
        quiet = interpreter.with_name('pythonw.exe')
        if os.name == 'nt' and quiet.exists():
            interpreter = quiet
        log_dir = ROOT / '.tools'
        log_dir.mkdir(exist_ok=True)
        with (log_dir / 'ui-server.log').open('ab') as log:
            options = {'creationflags': subprocess.CREATE_NO_WINDOW} if os.name == 'nt' else {'start_new_session': True}
            process = subprocess.Popen([str(interpreter), str(ROOT / 'ui_server.py')], cwd=ROOT, stdout=log, stderr=log, **options)
        for _ in range(60):
            if ready():
                break
            if process.poll() is not None:
                raise SystemExit('Could not start the UI. Check .tools/ui-server.log; port 8765 may already be in use.')
            time.sleep(0.15)
        else:
            raise SystemExit('UI startup timed out. Check .tools/ui-server.log.')
    if '--no-browser' not in sys.argv:
        webbrowser.open(URL)
    print('Local Studio is ready at ' + URL)


if __name__ == '__main__':
    main()
