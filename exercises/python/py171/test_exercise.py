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
    def test_aggregate(self):
        self.assertEqual(csv_balances("account,cents\nA,100\nB,-20\nA,50\n"),{"A":150,"B":-20})

    def test_quoted(self):
        self.assertEqual(csv_balances('account,cents\n"Tea, Ltd",125\n"Tea, Ltd",-25\n'),{"Tea, Ltd":100})

    def test_header_only(self):
        self.assertEqual(csv_balances("account,cents\n"),{})


if __name__ == "__main__":
    unittest.main()
