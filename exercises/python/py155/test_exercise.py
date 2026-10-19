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
    def test_per_user(self):
        self.assertEqual(admit_requests(["a","b","a","a","b"],2), [True,True,True,False,True])

    def test_zero_empty(self):
        self.assertEqual(admit_requests(["a","b"],0), [False,False])
        self.assertEqual(admit_requests([],2), [])

    def test_reset(self):
        users = ["a","a"]
        self.assertEqual(admit_requests(users,1), [True,False])
        self.assertEqual(admit_requests(users,1), [True,False])
        self.assertEqual(users, ["a","a"])


if __name__ == "__main__":
    unittest.main()
