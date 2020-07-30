import unittest
from vowels_count import get_count

class TestVowelsCount(unittest.TestCase):
    
    def test_perfect_square(self):
        self.assertEqual(get_count("a"),1)
        self.assertEqual(get_count("ab"),1)
        self.assertEqual(get_count("b"),0)
        self.assertEqual(get_count("aeiou"),5)
        self.assertEqual(get_count("aaeei"),5)
        self.assertEqual(get_count("aEioU"),5)
        self.assertEqual(get_count("aAeei"),5)

