import unittest
from move_zeroes_to_right import move_zeroes


class TestMoveZeroes(unittest.TestCase):

    def test_move_zeroes(self):
        self.assertEqual(move_zeroes([False, 1, 0, 1, 2, 0, 1, 3, "a"]), [
                         False, 1, 1, 2, 1, 3, "a", 0, 0])
        self.assertEqual(move_zeroes([False, 1, 0, True, 2, 0, 1, 3, "a"]), [
                         False, 1, True, 2, 1, 3, "a", 0, 0])
        self.assertEqual(move_zeroes([5, 8, -4, 10, 0, -10, '0', -8, -8, True, 2, 'y', 0, 8, 8, -6, 0, 0, 'y', True, -7, -7, 0, -10, True, 'y', 0]), [5, 8, -4, 10, -10, '0', -8, -8, True, 2, 'y', 8, 8, -6, 'y', True, -7, -7, -10, True, 'y', 0, 0, 0, 0, 0, 0])        



