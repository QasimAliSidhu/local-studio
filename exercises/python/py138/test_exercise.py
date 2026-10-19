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
    def test_override(self):
        self.assertEqual(patched_record({"x":1,"y":2}, {"x":3}), {"x":3,"y":2})

    def test_none(self):
        self.assertEqual(patched_record({"x":1}, {"x":None}), {"x":None})

    def test_new_and_preserved(self):
        base, changes = {"x":1}, {"y":2}
        result = patched_record(base, changes)
        self.assertEqual(base, {"x":1})
        self.assertEqual(changes, {"y":2})
        self.assertIsNot(result, base)
        self.assertIsNot(result, changes)


if __name__ == "__main__":
    unittest.main()
