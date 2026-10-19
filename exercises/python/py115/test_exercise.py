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
    def test_fresh_calls(self):
        self.assertEqual(add_job("a"), ["a"])
        self.assertEqual(add_job("b"), ["b"])

    def test_caller_list(self):
        jobs = ["a"]
        result = add_job("b", jobs)
        self.assertEqual(result, ["a", "b"])
        self.assertEqual(jobs, ["a"])
        self.assertIsNot(result, jobs)

    def test_empty_input(self):
        jobs = []
        self.assertEqual(add_job("a", jobs), ["a"])
        self.assertEqual(jobs, [])


if __name__ == "__main__":
    unittest.main()
