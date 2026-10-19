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
    def test_per_project(self):
        self.assertEqual(dependency_usage({"web":["a","a"],"api":["a","b"]}), {"a":2,"b":1})

    def test_empty(self):
        self.assertEqual(dependency_usage({}), {})
        self.assertEqual(dependency_usage({"web":[]}), {})

    def test_preserve(self):
        projects = {"x":["b","a","b"]}
        self.assertEqual(dependency_usage(projects), {"a":1,"b":1})
        self.assertEqual(projects, {"x":["b","a","b"]})


if __name__ == "__main__":
    unittest.main()
