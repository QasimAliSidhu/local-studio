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
    def test_union(self):
        self.assertEqual(merged_tags([["a","b"],["b","c"]]), {"a","b","c"})

    def test_exact_empty(self):
        self.assertEqual(merged_tags([]), set())
        self.assertEqual(merged_tags([["US","us",""]]), {"US","us",""})

    def test_no_alias(self):
        group = {"a"}
        result = merged_tags([group, ["b"]])
        self.assertEqual(group, {"a"})
        self.assertIsNot(result, group)


if __name__ == "__main__":
    unittest.main()
