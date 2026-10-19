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
    def test_paths(self):
        self.assertIs(is_absolute_route("/jobs"), True)
        self.assertIs(is_absolute_route("jobs"), False)

    def test_empty(self):
        self.assertIs(is_absolute_route(""), False)

    def test_missing(self):
        self.assertIs(is_absolute_route(None), False)


if __name__ == "__main__":
    unittest.main()
