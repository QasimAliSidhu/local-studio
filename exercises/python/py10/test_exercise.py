import unittest
from exercise import *

class SearchTests(unittest.TestCase):
    def test_edges(self):
        for values,target,result in [([],1,-1),([5],5,0),([1,3,5,7],1,0),([1,3,5,7],7,3),([1,3,5,7],4,-1)]: self.assertEqual(find_index(values,target),result)
    def test_duplicates(self):
        values=[1,2,2,2,3]; index=find_index(values,2); self.assertIn(index,[1,2,3])
    def test_logarithmic_access(self):
        class VirtualSequence:
            def __init__(self): self.reads=0
            def __len__(self): return 1000000
            def __getitem__(self,index):
                self.reads+=1
                if self.reads > 100: raise AssertionError('Too many element reads; use binary search')
                return index*2
        values=VirtualSequence(); self.assertEqual(find_index(values,1999998),999999)


if __name__ == "__main__":
    unittest.main()
