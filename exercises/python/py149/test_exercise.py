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
    def test_mean(self):
        self.assertEqual(average([2, 5, 8]), 5.0)
        self.assertIsInstance(average([2]), float)

    def test_empty(self):
        self.assertEqual(average([]), 0.0)
        self.assertIsInstance(average([]), float)

    def test_annotations(self):
        hints = get_type_hints(average)
        self.assertEqual(hints["values"], list[int])
        self.assertIs(hints["return"], float)


if __name__ == "__main__":
    unittest.main()
