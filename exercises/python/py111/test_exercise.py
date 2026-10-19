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
    def test_normal(self):
        self.assertEqual(checkout(105, 20), 135)

    def test_default(self):
        self.assertEqual(checkout(0), 0)

    def test_uses_helper(self):
        with patch("challenge.service_fee", return_value=7) as helper:
            self.assertEqual(checkout(100, 2), 109)
            helper.assert_called_once_with(100)


if __name__ == "__main__":
    unittest.main()
