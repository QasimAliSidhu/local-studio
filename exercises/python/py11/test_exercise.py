import unittest
from exercise import *

import sqlite3
import tempfile
from contextlib import closing
from pathlib import Path
class DatabaseTests(unittest.TestCase):
    def setUp(self): self.conn=sqlite3.connect(':memory:'); create_schema(self.conn)
    def tearDown(self): self.conn.close()
    def test_roundtrip(self):
        first=add_task(self.conn,' learn '); second=add_task(self.conn,"x'); DROP TABLE tasks; --")
        self.assertEqual(list_tasks(self.conn),[(first,'learn'),(second,"x'); DROP TABLE tasks; --")])
    def test_empty(self):
        with self.assertRaises(ValueError): add_task(self.conn,' ')
        self.assertEqual(list_tasks(self.conn),[])
    def test_idempotent(self): create_schema(self.conn); self.assertEqual(list_tasks(self.conn),[])
    def test_persistence(self):
        with tempfile.TemporaryDirectory() as directory:
            db=Path(directory)/'tasks.db'
            with closing(sqlite3.connect(db)) as conn: create_schema(conn); ident=add_task(conn,'persistent')
            with closing(sqlite3.connect(db)) as conn: self.assertEqual(list_tasks(conn),[(ident,'persistent')])


if __name__ == "__main__":
    unittest.main()
