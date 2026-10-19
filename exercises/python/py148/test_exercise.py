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
    def test_valid(self):
        self.assertEqual(withdraw(10, 10), 0)
        self.assertEqual(withdraw(10, 0), 10)

    def test_insufficient(self):
        self.assertTrue(issubclass(InsufficientFunds, ValueError))
        with self.assertRaisesRegex(InsufficientFunds, "insufficient funds"):
            withdraw(3, 4)

    def test_negative(self):
        with self.assertRaises(ValueError) as caught:
            withdraw(10, -1)
        self.assertNotIsInstance(caught.exception, InsufficientFunds)


if __name__ == "__main__":
    unittest.main()
