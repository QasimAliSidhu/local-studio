"""Regenerate only Python reading/task Markdown, preserving learner work."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import re
import shutil

from build_python_course import ROOT, ORDER, LESSON_MAP, lesson_source, task_source
from python_readability import READINGS, ILLUSTRATED


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def protected_files():
    paths = [p for p in (ROOT/'exercises').rglob('*') if p.is_file()
             and p.name not in {'lesson.md', 'README.md'} and '__pycache__' not in p.parts]
    paths += [p for p in ROOT.glob('*.json')]
    paths += [p for p in (ROOT/'courses').rglob('notes.md')]
    return {str(p.relative_to(ROOT)): digest(p) for p in paths}


def main(write=False):
    legacy = json.loads((ROOT/'tools/python_legacy_reading.json').read_text(encoding='utf-8'))
    lessons = {**legacy, **LESSON_MAP}
    assert set(READINGS) | ILLUSTRATED == set(ORDER) == set(lessons)
    before = protected_files()
    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    backup = ROOT/'.history'/('python-reading-all-'+stamp)
    results = []
    for ident in ORDER:
        item = lessons[ident]
        folder = ROOT/'exercises/python'/ident
        texts = {'lesson.md': lesson_source(item), 'README.md': task_source(item)}
        old_lesson = (folder/'lesson.md').read_text(encoding='utf-8')
        examples = lambda s: re.findall(r'```python\s*\n(.*?)\n```', s, re.S)
        assert examples(old_lesson) == examples(texts['lesson.md']), ident+' example changed'
        assert len(re.findall(r'^- ', texts['lesson.md'], re.M)) >= 3, ident
        assert re.search(r'^- ', texts['README.md'], re.M), ident
        for name, text in texts.items():
            path = folder/name
            if write:
                saved = backup/path.relative_to(ROOT)
                saved.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, saved)
                path.write_text(text, encoding='utf-8')
            else:
                assert path.read_text(encoding='utf-8') == text, str(path)+' needs regeneration'
        results.append({'id': ident, 'chapter': item.get('chapter'), 'teaching_bullets': len(re.findall(r'^- ', texts['lesson.md'], re.M)),
                        'task_bullets': len(re.findall(r'^- ', texts['README.md'], re.M)),
                        'example_unchanged': True, 'expanded_explanation': ident in READINGS,
                        'files': {str((folder/name).relative_to(ROOT)).replace('\\','/'): digest(folder/name) for name in texts}})
    assert protected_files() == before, 'A learner, grading, catalog or progress file changed'
    result = {'passed': True, 'checked_at': datetime.datetime.now().isoformat(timespec='seconds'),
              'python_lessons': len(results), 'chapters': 21, 'every_lesson_has_teaching_and_task_bullets': True,
              'worked_examples_unchanged': True, 'protected_files_unchanged': len(before),
              'backup': str(backup) if write else None, 'lessons': results}
    (ROOT/'.tools/PYTHON-READABILITY-COVERAGE.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in result.items() if key != 'lessons'}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    main(parser.parse_args().write)
