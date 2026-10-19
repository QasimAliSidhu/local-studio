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
        self.assertEqual(endpoints([8, 2, 5]), (8, 5))

    def test_empty_single(self):
        self.assertIsNone(endpoints([]))
        self.assertEqual(endpoints([0]), (0, 0))

    def test_tuple_preserved(self):
        values = ("b", "a")
        self.assertEqual(endpoints(values), ("b", "a"))
        self.assertEqual(values, ("b", "a"))


if __name__ == "__main__":
    unittest.main()
