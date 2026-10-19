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
    def test_result(self):
        self.assertEqual(tagged_copy({"tags": ["a"], "id": 7}, "b"), {"tags": ["a", "b"], "id": 7})

    def test_independence(self):
        original = {"tags": [], "id": 1}
        result = tagged_copy(original, "x")
        self.assertEqual(original, {"tags": [], "id": 1})
        self.assertIsNot(result, original)
        self.assertIsNot(result["tags"], original["tags"])

    def test_duplicates(self):
        self.assertEqual(tagged_copy({"tags": ["x"]}, "x")["tags"], ["x", "x"])


if __name__ == "__main__":
    unittest.main()
