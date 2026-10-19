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
    def test_order_duplicates(self):
        self.assertEqual(roundtrip_names(["B","A","B"]),["B","A","B"])

    def test_data_not_sql(self):
        names=["Pip's desk", "x'); DROP TABLE workers;--"]
        self.assertEqual(roundtrip_names(names),names)

    def test_empty(self):
        self.assertEqual(roundtrip_names([]),[])


if __name__ == "__main__":
    unittest.main()
