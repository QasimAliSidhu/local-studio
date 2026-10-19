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
    def test_accepted(self):
        self.assertEqual(normalize_id(" 12 "), 12)
        self.assertEqual(normalize_id(0), 0)

    def test_types(self):
        for value in [True, 1.2, None, []]:
            with self.assertRaises(TypeError):
                normalize_id(value)

    def test_values(self):
        for value in ["x", "", -1, "-3"]:
            with self.assertRaises(ValueError):
                normalize_id(value)

    def test_annotations(self):
        self.assertEqual(get_type_hints(normalize_id), {"value":int | str,"return":int})


if __name__ == "__main__":
    unittest.main()
