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
    def test_required_all(self):
        self.assertTrue(permission_check(["r","w"],["r","w"],[]))
        self.assertFalse(permission_check(["r"],["r","w"],[]))

    def test_forbidden_wins(self):
        self.assertFalse(permission_check(["r","danger"],["r"],["danger"]))

    def test_empty(self):
        self.assertIs(permission_check([], [], []), True)


if __name__ == "__main__":
    unittest.main()
