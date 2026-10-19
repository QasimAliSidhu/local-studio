import unittest
from exercise import *

class ScopeTests(unittest.TestCase):
    def test_discount(self): self.assertEqual(apply_discount([1000,999],25),[750,749])
    def test_no_mutation(self):
        prices=[1000,2500]; result=apply_discount(prices,0)
        self.assertEqual(prices,[1000,2500]); self.assertIsNot(result,prices)
        self.assertEqual(DEFAULT_PRICES,[1000,2500])
    def test_boundaries(self): self.assertEqual(apply_discount([12],100),[0])
    def test_invalid(self):
        for percent in [-1,101]:
            with self.assertRaises(ValueError): apply_discount([],percent)


if __name__ == "__main__":
    unittest.main()
