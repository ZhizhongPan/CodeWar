__author__ = 'zhizhong Pan'


import unittest
import numbers


def uniqify(iterable):
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item

def undefined_filter(iterable):
    for item in iterable:
        if isinstance(item, numbers.Number) or isinstance(item, basestring):
            yield item

def list_de_dup(list_):
    if isinstance(list_, list):
        return list(undefined_filter(uniqify(list_)))
    else:
        print "Not a list"


class TestCheckChooseMethods(unittest.TestCase):
    def test_list_de_dup(self):
        self.assertEqual(list_de_dup([1, None, 1, 2, 2, 'asd', 'asd', "dsa"]), [1, 2, 'asd', 'dsa'])

if __name__ == "__main__":
    unittest.main()
