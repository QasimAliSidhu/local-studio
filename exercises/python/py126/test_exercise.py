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
    def test_families(self):
        for code, expected in [(101,"info"),(204,"success"),(302,"redirect"),(404,"client"),(503,"server")]:
            self.assertEqual(status_family(code), expected)

    def test_boundaries(self):
        for code, expected in [(199,"info"),(200,"success"),(399,"redirect"),(400,"client"),(500,"server")]:
            self.assertEqual(status_family(code), expected)

    def test_high(self):
        self.assertEqual(status_family(599), "server")


if __name__ == "__main__":
    unittest.main()
