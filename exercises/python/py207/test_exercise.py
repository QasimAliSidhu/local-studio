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
    def test_forwarded(self):
        operation=Mock(return_value="ok")
        self.assertEqual(forward_call(operation,(1,),{"x":2}),"ok")
        operation.assert_called_once_with(1,x=2)

    def test_empty(self):
        self.assertEqual(forward_call(lambda:7,(),{}),7)

    def test_unchanged(self):
        args,kwargs=(1,),{"x":2}
        forward_call(Mock(),args,kwargs)
        self.assertEqual(args,(1,))
        self.assertEqual(kwargs,{"x":2})


if __name__ == "__main__":
    unittest.main()
