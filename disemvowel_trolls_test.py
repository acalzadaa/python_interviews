import unittest
from disemvowel_trolls import disemvowel

class TestDisemvowelTrolls(unittest.TestCase):
    
    def test_find_it(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"),"Ths wbst s fr lsrs LL!")
