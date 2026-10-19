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
    def test_partial(self):
        self.assertEqual(boxes_needed(13, 5), 3)

    def test_exact(self):
        self.assertEqual(boxes_needed(10, 5), 2)

    def test_zero_and_single(self):
        self.assertEqual(boxes_needed(0, 7), 0)
        self.assertEqual(boxes_needed(1, 100), 1)


if __name__ == "__main__":
    unittest.main()
