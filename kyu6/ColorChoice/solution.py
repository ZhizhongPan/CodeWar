__author__ = 'zhizhong pan'

import unittest
from math import factorial

def combinations(m, n):
    return factorial(m) / (factorial(n) * factorial(m - n))

def check_choose(m, n):
    max_x = n // 2
    min_x = 0

    while min_x <= max_x:
        mid_x = min_x + (max_x - min_x) // 2
        chose = combinations(n, mid_x)
        if chose < m:
            min_x = mid_x + 1
        elif chose > m:
            max_x = mid_x - 1
        else:
            return mid_x

    return -1



class TestCheckChooseMethods(unittest.TestCase):
    def test_combinations(self):
        self.assertEqual(combinations(3, 1), 3)
        self.assertEqual(combinations(5, 2), 10)

    def test_seven(self):

        self.assertEqual(check_choose(47129212243960, 50), 20)


if __name__ == '__main__':
    unittest.main()