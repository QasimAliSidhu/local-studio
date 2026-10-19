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
    def test_state(self):
        worker = Worker("Pip")
        self.assertEqual(worker.name,"Pip")
        self.assertEqual(worker.finish(7),1)
        self.assertEqual(worker.finish(8),2)
        self.assertEqual(worker.completed,[7,8])

    def test_independent(self):
        a,b = Worker("A"),Worker("B")
        a.finish(1)
        self.assertEqual(b.completed,[])
        self.assertIsNot(a.completed,b.completed)

    def test_duplicates(self):
        worker = Worker("A")
        worker.finish(0)
        self.assertEqual(worker.finish(0),2)
        self.assertEqual(worker.completed,[0,0])


if __name__ == "__main__":
    unittest.main()
