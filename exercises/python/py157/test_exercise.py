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
    def test_content(self):
        self.assertEqual(append_audit({"id":2,"events":["a"]},"b"), {"id":2,"events":["a","b"]})

    def test_references(self):
        record = {"events":[]}
        result = append_audit(record,"x")
        self.assertIsNot(result, record)
        self.assertIsNot(result["events"], record["events"])
        self.assertEqual(record, {"events":[]})

    def test_repeat(self):
        self.assertEqual(append_audit({"events":["x"]},"x")["events"], ["x","x"])


if __name__ == "__main__":
    unittest.main()
