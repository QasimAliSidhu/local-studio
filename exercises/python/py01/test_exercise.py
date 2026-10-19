import unittest
from exercise import *

class InvoiceTests(unittest.TestCase):
    def test_total(self): self.assertEqual(invoice_total([(125, 3),(200,2)]),775)
    def test_empty(self): self.assertEqual(invoice_total([]),0)
    def test_zero(self): self.assertEqual(invoice_total([(10,0)]),0)
    def test_negative(self):
        for value in [[(-1,1)],[(1,-1)]]:
            with self.assertRaises(ValueError): invoice_total(value)


if __name__ == "__main__":
    unittest.main()
