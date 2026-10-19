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
    def test_order(self):
        self.assertEqual(grid_cells(2, 2), [(0,0),(0,1),(1,0),(1,1)])

    def test_empty(self):
        self.assertEqual(grid_cells(0, 3), [])
        self.assertEqual(grid_cells(2, 0), [])

    def test_rectangle(self):
        self.assertEqual(grid_cells(1, 3), [(0,0),(0,1),(0,2)])


if __name__ == "__main__":
    unittest.main()
