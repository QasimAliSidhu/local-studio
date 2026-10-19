import unittest
from exercise import *

class QueueTests(unittest.TestCase):
    def test_fifo(self):
        queue=JobQueue(); queue.push('a'); queue.push('b')
        self.assertEqual(len(queue),2); self.assertEqual(queue.pop(),'a'); self.assertEqual(queue.pop(),'b')
        with self.assertRaises(IndexError): queue.pop()
    def test_independent(self):
        first=JobQueue(); second=JobQueue(); first.push(None)
        self.assertEqual(len(second),0); self.assertIsNone(first.pop())


if __name__ == "__main__":
    unittest.main()
