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
        self.assertEqual(drain_batches(8, 3), (3, 0))

    def test_empty(self):
        self.assertEqual(drain_batches(0, 2), (0, 0))

    def test_exact(self):
        self.assertEqual(drain_batches(12, 4), (3, 0))


if __name__ == "__main__":
    unittest.main()
