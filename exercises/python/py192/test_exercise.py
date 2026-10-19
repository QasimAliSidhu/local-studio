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
    def test_ordinary(self):
        self.assertEqual(double_number(5),10)

    def test_zero_negative(self):
        self.assertEqual(double_number(0),0)
        self.assertEqual(double_number(-3),-6)

    def test_repeatable(self):
        self.assertEqual(double_number(7),14)
        self.assertEqual(double_number(7),14)


if __name__ == "__main__":
    unittest.main()
