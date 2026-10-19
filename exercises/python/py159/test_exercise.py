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
    def test_filter_order(self):
        self.assertEqual(open_ticket_lines([{"id":3,"title":"C","done":False},{"id":1,"title":"A","done":False},{"id":2,"title":"B","done":True}]), ["1: A","3: C"])

    def test_zero_empty(self):
        self.assertEqual(open_ticket_lines([{"id":0,"title":"","done":False}]), ["0: "])
        self.assertEqual(open_ticket_lines([]), [])

    def test_preserve(self):
        tickets = [{"id":2,"title":"B","done":False},{"id":1,"title":"A","done":False}]
        original = deepcopy(tickets)
        open_ticket_lines(tickets)
        self.assertEqual(tickets, original)


if __name__ == "__main__":
    unittest.main()
