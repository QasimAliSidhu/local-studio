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
    def test_leaf(self):
        self.assertEqual(nested_sum(-3),-3)
        self.assertEqual(nested_sum(0),0)

    def test_nested(self):
        self.assertEqual(nested_sum([1,[2,[-3,4]],5]),9)

    def test_empty_preserved(self):
        node=[[],[0,[]],2]
        original=deepcopy(node)
        self.assertEqual(nested_sum(node),2)
        self.assertEqual(nested_sum([]),0)
        self.assertEqual(node,original)


if __name__ == "__main__":
    unittest.main()
