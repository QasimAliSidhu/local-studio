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
        wallet = Wallet(5)
        self.assertEqual(wallet.deposit(3),8)
        self.assertEqual(wallet.balance,8)
        self.assertEqual(wallet.deposit(0),8)

    def test_invariant(self):
        with self.assertRaises(ValueError):
            Wallet(-1)
        wallet=Wallet(5)
        with self.assertRaises(ValueError):
            wallet.deposit(-2)
        self.assertEqual(wallet.balance,5)

    def test_read_only(self):
        wallet=Wallet()
        with self.assertRaises(AttributeError):
            wallet.balance=99
        self.assertEqual(wallet.balance,0)


if __name__ == "__main__":
    unittest.main()
