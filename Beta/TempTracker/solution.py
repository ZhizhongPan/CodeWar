__author__ = 'Zhizhong Pan'


import unittest


class TempTracker:

    def __init__(self):
        # initialize instance variables
        pass

    def insert(self, temperature):
        # insert new temperature
        pass

    def get_max(self):
        # return max temp ever added
        pass

    def get_min(self):
        # return min temp ever added
        pass

    def get_mean(self):
        # return mean of all temps added
        pass

    def get_mode(self):
        # return mode of all temps added
        pass


class TestCheckChooseMethods(unittest.TestCase):
    def test_multiples2(self):
        temp_tracker = TempTracker()
        self.assertEquals(temp_tracker.insert(), "Fizz")
        self.assertEquals(temp_tracker.insert(), "Fang")
        self.assertEquals(TempTracker.insert(), "Foo")
        self.assertEquals(TempTracker.insert(), "Far")


if __name__ == '__main__':
    unittest.main()