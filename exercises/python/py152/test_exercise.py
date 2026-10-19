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
    def test_shape(self):
        self.assertEqual(new_ticket(7,"Fix robot"), {"id":7,"title":"Fix robot","done":False})

    def test_exact_fresh(self):
        a, b = new_ticket(0," "), new_ticket(0," ")
        self.assertIsNot(a, b)
        self.assertEqual(a["title"], " ")
        self.assertIs(a["done"], False)

    def test_annotations(self):
        self.assertEqual(get_type_hints(Ticket), {"id":int,"title":str,"done":bool})
        self.assertIs(get_type_hints(new_ticket)["return"], Ticket)


if __name__ == "__main__":
    unittest.main()
