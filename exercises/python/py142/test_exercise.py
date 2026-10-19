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
    def test_directions(self):
        self.assertEqual(roster_changes(["a","b"],["b","c"]), {"added":{"c"},"removed":{"a"},"stayed":{"b"}})

    def test_duplicates_empty(self):
        self.assertEqual(roster_changes([], ["x","x"]), {"added":{"x"},"removed":set(),"stayed":set()})

    def test_no_mutation(self):
        old, new = {"a"}, {"b"}
        roster_changes(old, new)
        self.assertEqual(old, {"a"})
        self.assertEqual(new, {"b"})


if __name__ == "__main__":
    unittest.main()
