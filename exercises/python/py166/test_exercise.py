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
    def test_order(self):
        self.assertEqual(apply_pipeline(4,[lambda n:n+2,lambda n:n*3]),18)

    def test_identity(self):
        value=[]
        self.assertIs(apply_pipeline(value,[]),value)

    def test_calls_errors(self):
        first,second=Mock(return_value=5),Mock(return_value=9)
        steps=[first,second]
        self.assertEqual(apply_pipeline(2,steps),9)
        first.assert_called_once_with(2)
        second.assert_called_once_with(5)
        self.assertEqual(len(steps),2)
        with self.assertRaises(ZeroDivisionError):
            apply_pipeline(1,[lambda n:n/0])


if __name__ == "__main__":
    unittest.main()
