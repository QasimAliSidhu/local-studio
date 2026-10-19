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
    def test_mixed(self):
        self.assertEqual(reconcile([{"account":"tea","cents":500},{"account":"cake","cents":-100},{"account":"tea","cents":-125}]), {"tea":375,"cake":-100})

    def test_zero_account(self):
        self.assertEqual(reconcile([{"account":"a","cents":0}]), {"a":0})
        self.assertEqual(reconcile([]), {})

    def test_repeatable(self):
        entries = [{"account":"a","cents":3}]
        self.assertEqual(reconcile(entries), reconcile(entries))
        self.assertEqual(entries, [{"account":"a","cents":3}])


if __name__ == "__main__":
    unittest.main()
