import unittest
from disemvowel_trolls import disemvowel

class TestDisemvowelTrolls(unittest.TestCase):
    
    def test_find_it(self):
        self.assertEqual(disemvowel("This site is for losers"),"Ths st s fr lsrs")
