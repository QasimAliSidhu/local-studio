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
    def test_returned(self):
        self.assertEqual(plus_two(10),12)
        self.assertEqual(plus_two(-2),0)

    def test_quiet(self):
        with redirect_stdout(StringIO()) as output:
            plus_two(0)
        self.assertEqual(output.getvalue(),"")


if __name__ == "__main__":
    unittest.main()
