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
    def test_workflow(self):
        self.assertEqual(ticket_engine({},[("add",0),("add",2),("close",0)]), {0:True,2:False})

    def test_errors(self):
        for initial, commands in [({1:False},[("add",1)]),({},[("close",1)]),({},[("dance",1)])]:
            with self.assertRaises(ValueError):
                ticket_engine(initial,commands)

    def test_atomic_input(self):
        initial = {1:False}
        with self.assertRaises(ValueError):
            ticket_engine(initial,[("close",1),("dance",1)])
        self.assertEqual(initial,{1:False})
        self.assertIsNot(ticket_engine(initial,[]), initial)


if __name__ == "__main__":
    unittest.main()
