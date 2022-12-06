import unittest
from add import add

class Testing(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(add(2,2), 4)
