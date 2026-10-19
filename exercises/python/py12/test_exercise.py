import unittest
from exercise import *

class CacheTests(unittest.TestCase):
    def test_deadline(self):
        cache=Cache(); cache.set('a',0,5,10)
        self.assertEqual(cache.get('a',14),0); self.assertIsNone(cache.get('a',15))
    def test_replace(self):
        cache=Cache(); cache.set('a','old',1,0); cache.set('a','new',10,0); self.assertEqual(cache.get('a',2),'new')
    def test_missing_zero_and_invalid(self):
        cache=Cache(); self.assertIsNone(cache.get('x',0)); cache.set('x',1,0,0); self.assertIsNone(cache.get('x',0))
        with self.assertRaises(ValueError): cache.set('x',1,-1,0)
    def test_independent(self):
        first=Cache(); second=Cache(); first.set('x',1,10,0); self.assertIsNone(second.get('x',0))


if __name__ == "__main__":
    unittest.main()
