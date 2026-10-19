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
    def test_fee_once(self):
        self.assertEqual(billed_total(10,3,2),32)

    def test_zero_quantity(self):
        self.assertEqual(billed_total(10,0,2),2)

    def test_no_fee(self):
        self.assertEqual(billed_total(7,2,0),14)


if __name__ == "__main__":
    unittest.main()
