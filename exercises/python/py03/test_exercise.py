import unittest
from exercise import *

class UniqueTests(unittest.TestCase):
    def test_order(self): self.assertEqual(unique_jobs(['b','a','b','A','a']),['b','a','A'])
    def test_empty(self): self.assertEqual(unique_jobs([]),[])
    def test_no_mutation(self):
        ids=['x','x']; unique_jobs(ids); self.assertEqual(ids,['x','x'])


if __name__ == "__main__":
    unittest.main()
