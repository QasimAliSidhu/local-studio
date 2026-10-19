import unittest
from exercise import *

class PageTests(unittest.TestCase):
    def test_pages(self):
        self.assertEqual(paginate([1,2,3,4,5],2,2),[3,4])
        self.assertEqual(paginate([1,2,3,4,5],3,2),[5])
        self.assertEqual(paginate([1],5,2),[])
    def test_invalid(self):
        for page,size in [(0,2),(1,0),(-1,2),(True,2),(1,1.5)]:
            with self.assertRaises(ValueError): paginate([],page,size)


if __name__ == "__main__":
    unittest.main()
