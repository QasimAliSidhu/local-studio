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
        self.assertEqual(job_labels(["A", "", "B"]), ["1: A", "3: B"])

    def test_empty(self):
        self.assertEqual(job_labels([]), [])
        self.assertEqual(job_labels(["", ""]), [])

    def test_space_and_input(self):
        names = [" ", "Pip"]
        self.assertEqual(job_labels(names), ["1:  ", "2: Pip"])
        self.assertEqual(names, [" ", "Pip"])


if __name__ == "__main__":
    unittest.main()
