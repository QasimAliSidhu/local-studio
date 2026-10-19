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
    def test_default(self):
        self.assertEqual(route_label("api"), "local/api")

    def test_override(self):
        self.assertEqual(route_label("api", "west"), "west/api")
        self.assertEqual(REGION, "local")

    def test_explicit_empty(self):
        self.assertEqual(route_label("api", ""), "/api")


if __name__ == "__main__":
    unittest.main()
