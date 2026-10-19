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
    def test_success(self):
        resource = Mock()
        resource.read.return_value = "data"
        self.assertEqual(use_resource(resource), "data")
        resource.read.assert_called_once_with()
        resource.close.assert_called_once_with()

    def test_failure(self):
        resource = Mock()
        resource.read.side_effect = RuntimeError("offline")
        with self.assertRaisesRegex(RuntimeError, "offline"):
            use_resource(resource)
        resource.close.assert_called_once_with()

    def test_falsy_result(self):
        resource = Mock()
        resource.read.return_value = None
        self.assertIsNone(use_resource(resource))
        resource.close.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
