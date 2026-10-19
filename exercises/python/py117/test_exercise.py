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
    def test_below(self):
        self.assertTrue(can_join(4, 5))

    def test_exactly_full(self):
        self.assertFalse(can_join(5, 5))

    def test_zero_and_overfull(self):
        self.assertFalse(can_join(0, 0))
        self.assertFalse(can_join(8, 5))


if __name__ == "__main__":
    unittest.main()
