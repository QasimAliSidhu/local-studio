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
    def test_group_order(self):
        self.assertEqual(group_tickets([{ "team":"a","id":2},{"team":"b","id":9},{"team":"a","id":1}]), {"a":[2,1],"b":[9]})

    def test_empty_duplicates(self):
        self.assertEqual(group_tickets([]), {})
        self.assertEqual(group_tickets([{"team":"a","id":1}]*2), {"a":[1,1]})

    def test_no_mutation(self):
        tickets = [{"team":"ops","id":7}]
        self.assertEqual(group_tickets(tickets), {"ops":[7]})
        self.assertEqual(tickets, [{"team":"ops","id":7}])


if __name__ == "__main__":
    unittest.main()
