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
    def test_wrapped_call(self):
        history=[]
        def add(a,b=0):
            return a+b
        wrapped=logged(add,history)
        self.assertEqual(wrapped(3,b=4),7)
        self.assertEqual(history,[(3,)])
        self.assertEqual(wrapped.__name__,"add")

    def test_repeat(self):
        history=[]
        operation=Mock(return_value=2)
        operation.__name__="operation"
        wrapped=logged(operation,history)
        wrapped(1)
        wrapped(0)
        self.assertEqual(history,[(1,),(0,)])
        self.assertEqual(operation.call_count,2)

    def test_failed_call_logged(self):
        history=[]
        def fail(value):
            raise ValueError("offline")
        with self.assertRaisesRegex(ValueError,"offline"):
            logged(fail,history)(7)
        self.assertEqual(history,[(7,)])


if __name__ == "__main__":
    unittest.main()
