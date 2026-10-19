import unittest
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
from challenge import *


class MissionTests(unittest.TestCase):
    def test_content(self):
        with TemporaryDirectory() as directory:
            path=Path(directory)/"notes.txt"
            path.write_text("  alpha  \n\n beta\t\n",encoding="utf-8")
            original=path.read_bytes()
            self.assertEqual(nonblank_lines(path),["alpha","beta"])
            self.assertEqual(path.read_bytes(),original)

    def test_utf8_empty(self):
        with TemporaryDirectory() as directory:
            path=Path(directory)/"notes.txt"
            path.write_text("caf\u00e9\n",encoding="utf-8")
            self.assertEqual(nonblank_lines(str(path)),["caf\u00e9"])
            path.write_text("  \n",encoding="utf-8")
            self.assertEqual(nonblank_lines(path),[])

    def test_missing(self):
        with TemporaryDirectory() as directory:
            with self.assertRaises(FileNotFoundError):
                nonblank_lines(Path(directory)/"missing.txt")


if __name__ == "__main__":
    unittest.main()
