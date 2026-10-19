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
    def test_repeat_calls(self):
        self.assertEqual(sum_request([2, 3]), 5)
        self.assertEqual(sum_request([2, 3]), 5)

    def test_empty_after_work(self):
        sum_request([9])
        self.assertEqual(sum_request([]), 0)

    def test_no_shared_mutation(self):
        values = [-2, 5]
        self.assertEqual(sum_request(values), 3)
        self.assertEqual(values, [-2, 5])
        import challenge
        self.assertEqual(challenge.AUDIT_TOTAL, 0)


if __name__ == "__main__":
    unittest.main()
