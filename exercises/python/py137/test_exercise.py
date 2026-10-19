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
    def test_present(self):
        self.assertEqual(configured_value({"x": 7}, "x", 9), 7)

    def test_meaningful_falsy(self):
        for value in [None, False, 0, ""]:
            self.assertIs(configured_value({"x": value}, "x", 9), value)

    def test_missing(self):
        settings = {"x": 1}
        self.assertEqual(configured_value(settings, "y", 3), 3)
        self.assertEqual(settings, {"x": 1})


if __name__ == "__main__":
    unittest.main()
