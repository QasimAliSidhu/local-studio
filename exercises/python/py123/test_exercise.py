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
    def test_single(self):
        self.assertTrue(has_flags(0b101, 0b001))
        self.assertFalse(has_flags(0b101, 0b010))

    def test_all_required(self):
        self.assertFalse(has_flags(0b001, 0b011))
        self.assertTrue(has_flags(0b111, 0b011))

    def test_empty_requirement(self):
        self.assertIs(has_flags(0, 0), True)
        self.assertIs(has_flags(12, 0), True)


if __name__ == "__main__":
    unittest.main()
