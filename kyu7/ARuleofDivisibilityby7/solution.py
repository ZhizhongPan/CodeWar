__author__ = 'zhizhong pan'


import unittest

def seven(m):
    counter = 0
    while m > 99:
        m = m / 10 - 2 * (m % 10)
        counter += 1

    return m, counter


def seven_best(m, step=0):
    if m < 100:
        return m, step
    x, y, step = m // 10, m % 10, step + 1
    res = x - 2 * y
    return seven(res, step)

class TestSevenMethods(unittest.TestCase):
    def test_seven(self):
        self.assertEqual(seven(1603), (7, 2))
        self.assertEqual(seven(371), (35, 1))
        self.assertEqual(seven(483), (42, 1))
        self.assertEqual(seven(477557101), (28, 7))


if __name__ == '__main__':
    unittest.main()






