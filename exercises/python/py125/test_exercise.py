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
    def test_ticket_or_staff(self):
        self.assertTrue(may_enter(True, False, False))
        self.assertTrue(may_enter(False, True, False))

    def test_ban_wins(self):
        self.assertFalse(may_enter(True, True, True))
        self.assertFalse(may_enter(False, True, True))

    def test_no_credentials(self):
        self.assertFalse(may_enter(False, False, False))


if __name__ == "__main__":
    unittest.main()
