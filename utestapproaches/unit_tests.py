# -*- coding: utf-8 -*-
"""Using unittest library to test sorting algorithm."""

import sys
import unittest

from main import ssort as sort_algorithm


def is_not_in_descending_order(a: list) -> bool:
    """Check if the list is not descending order."""
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True


class TestSort(unittest.TestCase):
    def test_simple_cases(self):
        cases = ([], [0], [1, 2], [1, 2, 3, 4, 5],
                 [4, 1, 3, 5, 2], [4, 3, 4, 3, 5],
                 list(range(20)), list(range(20, 1, -1)))
        for b in cases:
            with self.subTest(case=b):
                a = sort_algorithm(b)
                self.assertCountEqual(
                    a, b, msg='The number of elements has changed: ' + str(a))
                self.assertTrue(is_not_in_descending_order(a),
                                msg='List not sorted: ' + str(a))

    def test_stability(self):
        cases = ([[99] for i in range(5)],
                 [[1, 2], [1, 2], [2, 2], [2, 2], [3, 2], [3, 2]],
                 [[0, 1] for i in range(50)] + [[20, 10] for i in range(50)])
        for b in cases:
            with self.subTest(case=b):
                a = sort_algorithm(b)
                b.sort()
                self.assertTrue(all(x is y for x, y in zip(a, b)),
                                msg='Sorting algorith changed equal value.')

    def test_universality(self):
        cases = (list('qwerty'), [1.0 / i for i in range(1, 11)],
                 [[1], [1, 2], [1, 2, 3], [2, 3], [], [0]],
                 [True, False])
        for b in cases:
            with self.subTest(case=b):
                a = sort_algorithm(b)
                self.assertCountEqual(
                    a, b, msg='The number of elements has changed: ' + str(a))
                self.assertTrue(is_not_in_descending_order(a),
                                msg='List not sorted: ' + str(a))

    def test_scalability(self, max_scale=100):
        cases = (
            list(range(max_scale)), list(range(max_scale, 0, -1)),
            list(range(max_scale // 2, max_scale)) +
            list(range(max_scale // 2))
        )
        for b in cases:
            with self.subTest(case=b):
                a = sort_algorithm(b)
                self.assertCountEqual(
                    a, b, msg='The number of elements has changed: ' + str(a))
                self.assertTrue(is_not_in_descending_order(a),
                                msg='List not sorted: ' + str(a))


def doing_nothing(a: list) -> list:
    """Doing nothing with the list"""
    return a


def sort_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestSort('test_simple_cases'))
    suite.addTest(TestSort('test_stability'))
    suite.addTest(TestSort('test_universality'))
    suite.addTest(TestSort('test_scalability'))
    return suite


if __name__ == '__main__':
    # unittest.main()

    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    for algo in doing_nothing, sort_algorithm:
        print('Testing function ', algo.__doc__.strip())
        test_suite = sort_test_suite()
        sort_algorithm = algo
        runner.run(test_suite)
