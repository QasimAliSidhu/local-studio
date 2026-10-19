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
    def test_missing_none(self):
        self.assertEqual(get_timeout({}),30)
        self.assertEqual(get_timeout({"timeout":None},8),8)

    def test_falsy(self):
        for value in [0, False, ""]:
            self.assertIs(get_timeout({"timeout":value}), value)

    def test_ordinary_preserved(self):
        settings = {"timeout":5}
        self.assertEqual(get_timeout(settings),5)
        self.assertEqual(settings,{"timeout":5})


if __name__ == "__main__":
    unittest.main()
