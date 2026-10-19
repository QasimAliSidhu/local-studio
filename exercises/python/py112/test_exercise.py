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
    def test_mixed(self):
        self.assertEqual(split_duration(125), (2, 5))

    def test_boundaries(self):
        self.assertEqual(split_duration(0), (0, 0))
        self.assertEqual(split_duration(60), (1, 0))

    def test_reconstruct(self):
        for total in [1, 59, 61, 3601]:
            minutes, seconds = split_duration(total)
            self.assertEqual(minutes * 60 + seconds, total)
            self.assertTrue(0 <= seconds < 60)


if __name__ == "__main__":
    unittest.main()
