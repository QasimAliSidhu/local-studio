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
    def test_positions(self):
        self.assertEqual(numbered_jobs(["a","b"]),[(1,"a"),(2,"b")])

    def test_empty_names(self):
        self.assertEqual(numbered_jobs(["", "x"]),[(1,""),(2,"x")])
        self.assertEqual(numbered_jobs([]),[])


if __name__ == "__main__":
    unittest.main()
