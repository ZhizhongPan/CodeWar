__author__ = 'zhizhong pan'

import unittest
import math



def round_to_next_5(n):
    n = math.ceil(n / 5.0) * 5
    return n


class TestCheckChooseMethods(unittest.TestCase):
    def test_round_to_next_5(self):
        self.assertEqual(round_to_next_5(0), 0)
        self.assertEqual(round_to_next_5(2), 5)
        self.assertEqual(round_to_next_5(3), 5)
        self.assertEqual(round_to_next_5(11), 15)

if __name__ == "__main__":
    unittest.main()
