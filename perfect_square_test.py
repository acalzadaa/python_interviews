import unittest
from perfect_square import is_square

class TestPerfectSquare(unittest.TestCase):
    
    def test_perfect_square(self):
        self.assertEqual(is_square(-1),False)
        self.assertEqual(is_square(0),True)
        self.assertEqual(is_square(4),True)
