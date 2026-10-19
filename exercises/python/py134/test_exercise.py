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
    def test_tail(self):
        self.assertEqual(recent_items([1,2,3,4], 2), [3,4])

    def test_zero(self):
        self.assertEqual(recent_items([1,2], 0), [])

    def test_oversize_copy(self):
        values = [1,2]
        result = recent_items(values, 9)
        self.assertEqual(result, [1,2])
        self.assertIsNot(result, values)
        self.assertEqual(values, [1,2])


if __name__ == "__main__":
    unittest.main()
