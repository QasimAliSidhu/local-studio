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
    def test_normal(self):
        self.assertEqual(adjusted_total(10,2),12)

    def test_fresh(self):
        self.assertEqual(adjusted_total(10,2),12)
        self.assertEqual(adjusted_total(10,2),12)
        self.assertEqual(adjusted_total(0,0),0)

    def test_signed(self):
        self.assertEqual(adjusted_total(-2,5),3)


if __name__ == "__main__":
    unittest.main()
