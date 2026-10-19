import unittest
from exercise import *

class PortTests(unittest.TestCase):
    def test_valid(self):
        for text,value in [(' 8080 ',8080),('1',1),('65535',65535),('0080',80)]: self.assertEqual(parse_port(text),value)
    def test_invalid(self):
        for text in ['', '0','65536','-1','+80','3.5','abc','１２']:
            with self.subTest(text=text):
                with self.assertRaises(ValueError): parse_port(text)


if __name__ == "__main__":
    unittest.main()
