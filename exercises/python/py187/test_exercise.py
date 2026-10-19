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
    def test_local(self):
        self.assertEqual(local_label(),"local")

    def test_outer_unchanged(self):
        local_label()
        import challenge
        self.assertEqual(challenge.label,"global")


if __name__ == "__main__":
    unittest.main()
