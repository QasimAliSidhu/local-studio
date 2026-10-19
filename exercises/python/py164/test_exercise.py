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
    def test_record(self):
        self.assertEqual(Notice("a","hi"), Notice("a","hi"))
        with self.assertRaises(AttributeError):
            Notice("a","hi").text="bye"

    def test_collaborator(self):
        transport=Mock()
        transport.send.return_value="queued"
        self.assertEqual(Dispatcher(transport).deliver(Notice("a","hi")),"queued")
        transport.send.assert_called_once_with("a","hi")

    def test_error(self):
        transport=Mock()
        transport.send.side_effect=RuntimeError("offline")
        with self.assertRaisesRegex(RuntimeError,"offline"):
            Dispatcher(transport).deliver(Notice("a","hi"))


if __name__ == "__main__":
    unittest.main()
