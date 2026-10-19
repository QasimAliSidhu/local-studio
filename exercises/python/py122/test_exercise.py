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
    def test_growth(self):
        self.assertEqual(backoff(3, 2, 100), 12)

    def test_first_attempt(self):
        self.assertEqual(backoff(5, 0, 100), 5)

    def test_cap(self):
        self.assertEqual(backoff(5, 10, 30), 30)
        self.assertEqual(backoff(0, 4, 10), 0)


if __name__ == "__main__":
    unittest.main()
