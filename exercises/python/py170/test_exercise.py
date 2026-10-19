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
    def test_valid(self):
        self.assertEqual(load_job_ids("[0, 7, 7]"),[0,7,7])
        self.assertEqual(load_job_ids("[]"),[])

    def test_invalid_shape(self):
        for text in ["{}","null","[true]","[-1]","[1.5]",'["7"]']:
            with self.assertRaises(ValueError):
                load_job_ids(text)

    def test_malformed(self):
        with self.assertRaises(json.JSONDecodeError):
            load_job_ids("[not json")


if __name__ == "__main__":
    unittest.main()
