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
    def test_correct(self):
        self.assertIsNone(verify_double(lambda value: value * 2))

    def test_constant_impostor(self):
        with self.assertRaises(AssertionError):
            verify_double(lambda value: 8)

    def test_negative_bug(self):
        with self.assertRaises(AssertionError):
            verify_double(lambda value: abs(value) * 2)

    def test_zero_bug(self):
        with self.assertRaises(AssertionError):
            verify_double(lambda value: 1 if value == 0 else value * 2)


if __name__ == "__main__":
    unittest.main()
