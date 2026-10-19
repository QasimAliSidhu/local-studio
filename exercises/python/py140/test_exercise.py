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
    def test_unique(self):
        self.assertEqual(invert_labels({"a":"A","b":"B"}), {"A":"a","B":"b"})

    def test_collision(self):
        self.assertEqual(invert_labels({"old":"x","new":"x"}), {"x":"new"})

    def test_empty_preserved(self):
        self.assertEqual(invert_labels({}), {})
        labels = {"a":"A"}
        result = invert_labels(labels)
        self.assertEqual(labels, {"a":"A"})
        self.assertIsNot(result, labels)


if __name__ == "__main__":
    unittest.main()
