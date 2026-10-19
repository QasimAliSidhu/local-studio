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
    def test_fifo(self):
        self.assertEqual(serve_next(["a","b","c"]), ("a", ["b","c"]))

    def test_empty(self):
        self.assertEqual(serve_next([]), (None, []))

    def test_no_mutation(self):
        waiting = [0,1]
        served, remaining = serve_next(waiting)
        self.assertEqual(served, 0)
        self.assertEqual(waiting, [0,1])
        self.assertIsNot(waiting, remaining)


if __name__ == "__main__":
    unittest.main()
