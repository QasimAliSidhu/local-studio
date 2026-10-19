import unittest
from exercise import *

class TaskTests(unittest.TestCase):
    def test_default(self): self.assertEqual(normalize_task({'title':' work ','id':9}),{'title':'work','done':False})
    def test_done(self): self.assertEqual(normalize_task({'title':'x','done':True}),{'title':'x','done':True})
    def test_invalid(self):
        for data in [{},{'title':' '},{'title':1},{'title':'x','done':1},{'title':'x','done':'false'}]:
            with self.assertRaises(ValueError): normalize_task(data)


if __name__ == "__main__":
    unittest.main()
