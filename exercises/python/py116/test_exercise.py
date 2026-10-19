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
    def test_sequence(self):
        counter = make_ticket_counter()
        self.assertEqual([counter(), counter(), counter()], [1, 2, 3])

    def test_custom_start(self):
        counter = make_ticket_counter(10)
        self.assertEqual(counter(), 11)

    def test_independent(self):
        a, b = make_ticket_counter(2), make_ticket_counter(20)
        self.assertEqual(a(), 3)
        self.assertEqual(b(), 21)
        self.assertEqual(a(), 4)


if __name__ == "__main__":
    unittest.main()
