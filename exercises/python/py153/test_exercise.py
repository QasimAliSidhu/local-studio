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
    def test_normal(self):
        self.assertEqual(word_report("Ping ping PONG"), [("ping",2),("pong",1)])

    def test_whitespace(self):
        self.assertEqual(word_report("  A\nB\tA "), [("a",2),("b",1)])
        self.assertEqual(word_report("  "), [])

    def test_punctuation(self):
        self.assertEqual(word_report("Hi hi!"), [("hi",1),("hi!",1)])


if __name__ == "__main__":
    unittest.main()
