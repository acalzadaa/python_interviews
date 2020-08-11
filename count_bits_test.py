import unittest
from count_bits import bits, bits_original

class TestCountBits(unittest.TestCase):

    def test_count_bits_original(self):
        self.assertEqual(bits_original(0),0)
        self.assertEqual(bits_original(4),1)
        self.assertEqual(bits_original(1),1)
        self.assertEqual(bits_original(2),1)
        self.assertEqual(bits_original(3),2)
        self.assertEqual(bits_original(5),2)
        self.assertEqual(bits_original(6),2)
        self.assertEqual(bits_original(7),3)
        self.assertEqual(bits_original(8),1)
        self.assertEqual(bits_original(9),2)
    
    def test_count_bits(self):
        self.assertEqual(bits(0),0)
        self.assertEqual(bits(4),1)
        self.assertEqual(bits(1),1)
        self.assertEqual(bits(2),1)
        self.assertEqual(bits(3),2)
        self.assertEqual(bits(5),2)
        self.assertEqual(bits(6),2)
        self.assertEqual(bits(7),3)
        self.assertEqual(bits(8),1)
        self.assertEqual(bits(9),2)
