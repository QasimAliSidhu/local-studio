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
    def test_intermediate_state(self):
        with redirect_stdout(StringIO()) as output:
            result = trace_total([3, -1, 5])
        self.assertEqual(result, 7)
        self.assertEqual(output.getvalue(), "total=3\ntotal=2\ntotal=7\n")

    def test_empty(self):
        with redirect_stdout(StringIO()) as output:
            self.assertEqual(trace_total([]), 0)
        self.assertEqual(output.getvalue(), "")

    def test_zero(self):
        with redirect_stdout(StringIO()) as output:
            self.assertEqual(trace_total([0]), 0)
        self.assertEqual(output.getvalue(), "total=0\n")


if __name__ == "__main__":
    unittest.main()
