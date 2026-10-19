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
    def test_spaces(self):
        self.assertEqual(dash_words("  Night   Shift  "),"Night-Shift")

    def test_other_whitespace(self):
        self.assertEqual(dash_words("a\nb\tc"),"a-b-c")

    def test_empty(self):
        self.assertEqual(dash_words(" "),"")
        self.assertEqual(dash_words(""),"")


if __name__ == "__main__":
    unittest.main()
