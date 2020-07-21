import unittest
from list_filtering import filter_list

class TestListFiltering(unittest.TestCase):
    
    def test_list_filtering(self):
        self.assertEqual(filter_list([1,2,'a','b']),[1,2])
        self.assertEqual(filter_list([1,'a','b',0,15]),[1,0,15])
        self.assertEqual(filter_list([1,2,'aasf',123]),[1,2,123])
