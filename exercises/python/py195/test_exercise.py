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
    def test_count(self):
        self.assertEqual(job_count(["a","b"]),2)

    def test_empty(self):
        self.assertEqual(job_count([]),0)

    def test_items_not_characters(self):
        jobs=["a long job name"]
        self.assertEqual(job_count(jobs),1)
        self.assertEqual(jobs,["a long job name"])


if __name__ == "__main__":
    unittest.main()
