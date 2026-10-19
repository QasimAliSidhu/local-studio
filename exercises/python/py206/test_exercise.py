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
    def test_normal(self):
        flag=ManagedFlag()
        self.assertIs(flag.active,False)
        with flag as resource:
            self.assertIs(resource,flag)
            self.assertIs(flag.active,True)
        self.assertIs(flag.active,False)

    def test_error(self):
        flag=ManagedFlag()
        with self.assertRaisesRegex(ValueError,"oops"):
            with flag:
                raise ValueError("oops")
        self.assertIs(flag.active,False)

    def test_reuse(self):
        flag=ManagedFlag()
        with flag:
            pass
        with flag:
            self.assertTrue(flag.active)
        self.assertFalse(flag.active)


if __name__ == "__main__":
    unittest.main()
