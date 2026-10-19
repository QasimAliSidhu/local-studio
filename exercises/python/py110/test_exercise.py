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
        self.assertEqual(badge("Pip"), "Pip [learner]")

    def test_keyword(self):
        self.assertEqual(badge(role="operator", name="Mira"), "Mira [operator]")

    def test_explicit_empty(self):
        self.assertEqual(badge("Pip", ""), "Pip []")


if __name__ == "__main__":
    unittest.main()
