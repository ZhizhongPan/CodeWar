__author__ = 'rockrollroger'

import unittest


def order_weight(strng):
    if not strng:
        return ""
    weight_list = strng.split(" ")
    weight_number_list = map(int, [reduce(lambda x, y: int(x)+int(y), weight)
                                   for weight in weight_list])
    weight_list = [x for (y, x) in sorted(zip(weight_number_list, weight_list))]
    return " ".join(weight_list)


def order_weight_best(_str):
    return " ".join(sorted(_str.split(" "), key=lambda x: (sum(int(c) for c in x), x)))

class TestCheckChooseMethods(unittest.TestCase):
    def test_order_weight(self):
        self.assertEqual(order_weight_best(""), "")
        self.assertEqual(order_weight_best("6 3 4"), "3 4 6")
        self.assertEqual(order_weight_best("103 123 4444 99 2000"), "2000 103 123 4444 99")
        self.assertEqual(order_weight_best("2000 10003 1234000 44444444 9999 11 11 22 123"),
                         "11 11 2000 10003 22 123 1234000 44444444 9999")
        self.assertEqual(order_weight_best('16 38 95 1131268 49455 347464 59544965313 496636983114762 85246814996697 3 9'),
                         '3 16 9 38 95 1131268 49455 347464 59544965313 496636983114762 85246814996697')




if __name__ == "__main__":
    unittest.main()
