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
    def test_first_not_smallest(self):
        self.assertEqual(first_even_job([-2, 9, 8, 2]), 8)

    def test_zero(self):
        self.assertEqual(first_even_job([3, 0, 4]), 0)

    def test_none(self):
        self.assertIsNone(first_even_job([]))
        self.assertIsNone(first_even_job([-4, 1, 3]))

    def test_preserved(self):
        values = [7, 4, 2]
        first_even_job(values)
        self.assertEqual(values, [7, 4, 2])


if __name__ == "__main__":
    unittest.main()
