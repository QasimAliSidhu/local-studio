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
    def test_valid(self):
        self.assertEqual(try_integer(" -12 "), -12)
        self.assertEqual(try_integer("0"), 0)

    def test_malformed(self):
        for raw in ["", "12.5", "twelve", "7x"]:
            self.assertIsNone(try_integer(raw))

    def test_missing(self):
        self.assertIsNone(try_integer(None))


if __name__ == "__main__":
    unittest.main()
