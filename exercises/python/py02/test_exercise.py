import unittest
from exercise import *

class StatusTests(unittest.TestCase):
    def test_repeats(self): self.assertEqual(count_statuses([200,404,200,500]),{200:2,404:1,500:1})
    def test_empty(self): self.assertEqual(count_statuses([]),{})
    def test_input_preserved(self):
        codes=[200,200]; count_statuses(codes); self.assertEqual(codes,[200,200])


if __name__ == "__main__":
    unittest.main()
