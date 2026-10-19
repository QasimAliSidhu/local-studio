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
    def test_valid_bounds(self):
        self.assertEqual(validate_port(1), 1)
        self.assertEqual(validate_port(65535), 65535)

    def test_wrong_types(self):
        for value in [True, False, "80", 80.0, None]:
            with self.assertRaisesRegex(TypeError, "port"):
                validate_port(value)

    def test_range(self):
        for value in [0, -1, 65536]:
            with self.assertRaisesRegex(ValueError, "port"):
                validate_port(value)


if __name__ == "__main__":
    unittest.main()
