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
    def test_dedup(self):
        self.assertEqual(invited_domains(["a@Example.org","b@example.org","x@other.net"]), {"example.org","other.net"})

    def test_empty(self):
        self.assertEqual(invited_domains([]), set())

    def test_preserved(self):
        addresses = ["A@X.NET"]
        self.assertEqual(invited_domains(addresses), {"x.net"})
        self.assertEqual(addresses, ["A@X.NET"])


if __name__ == "__main__":
    unittest.main()
