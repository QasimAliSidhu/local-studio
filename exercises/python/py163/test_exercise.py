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
    def test_base(self):
        self.assertEqual(Job(7).cost(),7)

    def test_subtype(self):
        job=PriorityJob(7,3)
        self.assertIsInstance(job,Job)
        self.assertEqual(job.units,7)
        self.assertEqual(job.cost(),10)

    def test_zero(self):
        self.assertEqual(PriorityJob(0,0).cost(),0)
        self.assertEqual(Job(0).cost(),0)


if __name__ == "__main__":
    unittest.main()
