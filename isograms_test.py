import unittest
from isograms import is_isogram


class TestIsograms(unittest.TestCase):

    def test_is_isogram(self):
        self.assertEqual(is_isogram("abc"), True)
        self.assertEqual(is_isogram("abcB"), False)
        self.assertEqual(is_isogram("aA"), False)
        self.assertEqual(is_isogram("abBA"), False)
        self.assertEqual(is_isogram("aaabc"), False)
        self.assertEqual(is_isogram("1j2"), True)
        self.assertEqual(is_isogram(""), True)
