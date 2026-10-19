import unittest
from exercise import *

class AggregateTests(unittest.TestCase):
    def test_sum(self): self.assertEqual(sum_successful([{'status':'ok','amount':5},{'status':'fail','amount':100},{'status':'ok','amount':-2},{}]),3)
    def test_empty(self): self.assertEqual(sum_successful([]),0)
    def test_immutable(self):
        event={'status':'ok','amount':5}; sum_successful([event]); self.assertEqual(event,{'status':'ok','amount':5})


if __name__ == "__main__":
    unittest.main()
