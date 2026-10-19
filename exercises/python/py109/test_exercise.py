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
        self.assertEqual(order_total(125, 4, 50), 550)

    def test_zero_quantity(self):
        self.assertEqual(order_total(500, 0, 20), 20)

    def test_no_printing(self):
        with redirect_stdout(StringIO()) as output:
            self.assertEqual(order_total(1, 1, 0), 1)
        self.assertEqual(output.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
