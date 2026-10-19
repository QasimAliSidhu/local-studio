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
    def test_order(self):
        self.assertEqual(sort_by_name([{"name":"B"},{"name":"A"}]),[{"name":"A"},{"name":"B"}])

    def test_new_list(self):
        records=[{"name":"B"},{"name":"A"}]
        result=sort_by_name(records)
        self.assertEqual(records,[{"name":"B"},{"name":"A"}])
        self.assertIsNot(result,records)

    def test_empty(self):
        self.assertEqual(sort_by_name([]),[])


if __name__ == "__main__":
    unittest.main()
