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
    def test_representation(self):
        self.assertTrue(approximately_equal(0.1 + 0.2, 0.3))

    def test_outside(self):
        self.assertFalse(approximately_equal(10.2, 10.0, 0.1))

    def test_absolute_and_exact(self):
        self.assertTrue(approximately_equal(-5, -5, 0))
        self.assertFalse(approximately_equal(1000001, 1000000, 0.1))


if __name__ == "__main__":
    unittest.main()
