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
    def test_present(self):
        self.assertEqual(first_ticket([0, 9]), 0)
        self.assertEqual(first_ticket([-1]), -1)

    def test_missing(self):
        self.assertIsNone(first_ticket([]))

    def test_annotations_input(self):
        ids = [8,2]
        self.assertEqual(first_ticket(ids), 8)
        self.assertEqual(ids, [8,2])
        hints = get_type_hints(first_ticket)
        self.assertEqual(hints["ids"], list[int])
        self.assertEqual(hints["return"], int | None)


if __name__ == "__main__":
    unittest.main()
