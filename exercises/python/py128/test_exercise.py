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
    def test_missing(self):
        self.assertEqual(choose_label(None, "default"), "default")

    def test_falsy_values(self):
        for value in ["", 0, False, []]:
            self.assertIs(choose_label(value, "default"), value)

    def test_ordinary(self):
        self.assertEqual(choose_label("ready", "default"), "ready")


if __name__ == "__main__":
    unittest.main()
