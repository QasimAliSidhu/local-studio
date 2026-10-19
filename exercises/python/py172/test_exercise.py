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
    def test_order_concurrency(self):
        async def scenario():
            started=[]
            gate=asyncio.Event()
            async def fetch(name):
                started.append(name)
                if len(started)==3:
                    gate.set()
                await asyncio.wait_for(gate.wait(),timeout=1)
                return name.upper()
            result=await collect_statuses(["b","a","c"],fetch)
            self.assertEqual(result,["B","A","C"])
            self.assertCountEqual(started,["a","b","c"])
        asyncio.run(scenario())

    def test_empty(self):
        async def fetch(name):
            raise AssertionError("must not fetch")
        self.assertEqual(asyncio.run(collect_statuses([],fetch)),[])

    def test_errors(self):
        async def fetch(name):
            raise RuntimeError("offline")
        with self.assertRaisesRegex(RuntimeError,"offline"):
            asyncio.run(collect_statuses(["api"],fetch))


if __name__ == "__main__":
    unittest.main()
