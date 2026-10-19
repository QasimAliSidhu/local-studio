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
    def test_ordering(self):
        self.assertEqual(leaderboard([{"name":"Z","score":2},{"name":"B","score":5},{"name":"A","score":5}]), [{"name":"A","score":5},{"name":"B","score":5},{"name":"Z","score":2}])

    def test_new_records(self):
        records=[{"name":"A","score":1,"secret":"x"}]
        original=deepcopy(records)
        result=leaderboard(records)
        self.assertEqual(records,original)
        self.assertIsNot(result[0],records[0])
        self.assertNotIn("secret",result[0])

    def test_empty(self):
        self.assertEqual(leaderboard([]),[])


if __name__ == "__main__":
    unittest.main()
