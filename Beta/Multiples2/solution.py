__author__ = 'Zhizhong Pan'


import unittest

def multiples2(val):
    if val % 49 == 0 and val % 3 == 0:
        return "Fang"
    if val % 7 == 0:
        return "Fizz"
    if val % 15 == 0:
        return "Foo"
    return "Far"



class TestCheckChooseMethods(unittest.TestCase):
    def test_multiples2(self):
        self.assertEquals(multiples2(49), "Fizz")
        self.assertEquals(multiples2(147), "Fang")
        self.assertEquals(multiples2(30), "Foo")
        self.assertEquals(multiples2(51), "Far")
