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
        self.assertEqual(sum_through(5), 15)

    def test_empty_and_one(self):
        self.assertEqual(sum_through(0), 0)
        self.assertEqual(sum_through(1), 1)

    def test_larger(self):
        self.assertEqual(sum_through(100), 5050)


if __name__ == "__main__":
    unittest.main()
