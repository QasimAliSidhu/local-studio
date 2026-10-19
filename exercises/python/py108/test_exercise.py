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


class MissionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        output=StringIO()
        try:
            with redirect_stdout(output):
                cls.state=runpy.run_path(str(Path(__file__).with_name("main.py")),run_name="__main__")
        finally:
            cls.output=output.getvalue()
            result_file=os.environ.get("STUDIO_SCRIPT_OUTPUT")
            if result_file:
                Path(result_file).write_text(json.dumps({"stdout":cls.output}),encoding="utf-8")
            else:
                print(cls.output,end="",flush=True)
    def test_conversion(self):
        self.assertIs(type(self.state.get("count")),int)
        self.assertEqual(self.state.get("count"),8)
        self.assertEqual(self.state.get("raw"),"8")

    def test_output(self):
        self.assertEqual(self.output,"10\n")


if __name__ == "__main__":
    unittest.main()
