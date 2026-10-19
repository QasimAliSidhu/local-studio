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
    def test_values(self):
        self.assertEqual(list(even_stream(iter([-4,-1,0,3,6]))),[-4,0,6])

    def test_empty(self):
        self.assertEqual(list(even_stream(iter([]))),[])

    def test_lazy(self):
        consumed=[]
        def source():
            for value in [1,2,4]:
                consumed.append(value)
                yield value
        stream=even_stream(source())
        self.assertEqual(consumed,[])
        self.assertIs(iter(stream),stream)
        self.assertEqual(next(stream),2)
        self.assertEqual(consumed,[1,2])
        self.assertEqual(next(stream),4)


if __name__ == "__main__":
    unittest.main()
