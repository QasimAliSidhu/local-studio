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
    def test_callback(self):
        operation=Mock(return_value=9)
        self.assertEqual(apply_once(4,operation),9)
        operation.assert_called_once_with(4)

    def test_different_types(self):
        self.assertEqual(apply_once("hi",str.upper),"HI")

    def test_propagates(self):
        operation=Mock(side_effect=ValueError("no"))
        with self.assertRaisesRegex(ValueError,"no"):
            apply_once(1,operation)


if __name__ == "__main__":
    unittest.main()
