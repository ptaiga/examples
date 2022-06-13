# -*- coding: utf-8 -*-
"""Testing module."""


import unittest

from main import primefactor


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        cases = ['str', 3.14, [1, 2, 3], {}]
        for x in cases:
            with self.subTest(case=x):
                self.assertRaises(TypeError, primefactor, x)

    def test_negative(self):
        cases = [-1, -10, -100]
        for x in cases:
            with self.subTest(case=x):
                self.assertRaises(ValueError, primefactor, x)

    def test_zero_and_one_cases(self):
        cases = [0, 1]
        for x in cases:
            with self.subTest(case=x):
                self.assertEqual(primefactor(x), (x,))

    def test_simple_numbers(self):
        cases = [3, 5, 11, 17]
        for x in cases:
            with self.subTest(case=x):
                self.assertEqual(primefactor(x), (x,))

    def test_two_simple_factors(self):
        cases = [(6, (2, 3)), (15, (3, 5)), (169, (13, 13))]
        for x in cases:
            with self.subTest(case=x):
                self.assertEqual(primefactor(x[0]), x[1])

    def test_many_factors(self):
        cases = [(105, (3, 5, 7)), (128009973, (3, 7, 13, 19, 23, 29, 37))]
        for x in cases:
            with self.subTest(case=x):
                self.assertEqual(primefactor(x[0]), x[1])


if __name__ == '__main__':
    unittest.main()
