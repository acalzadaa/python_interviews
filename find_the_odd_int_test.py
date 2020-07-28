import unittest
from find_the_odd_int import find_it

class TestFindIt(unittest.TestCase):
    
    def test_find_it(self):
        self.assertEqual(find_it([-1,-2,3,3,7,10]),[-1,-2,7,10])
        self.assertEqual(find_it([1,2,2,3]),[1,3])
        self.assertEqual(find_it([1,1,2,3,3,4,5,5,99]),[2,4,99])
        self.assertEqual(find_it([10]),[10])

