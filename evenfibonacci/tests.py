# -*- coding: utf-8 -*-
"""Unittest module.

Usage:
`$ python tests.py`

"""

import unittest

from contracts.interface import ContractNotRespected

from main import even_fib


class TestEvenFib(unittest.TestCase):
    def test_usage(self):
        cases = {
            0: [],
            1: [0],
            2: [0, 2],
            5: [0, 2, 8, 34, 144],
        }

        for key, val in cases.items():
            with self.subTest(case=key):
                self.assertEqual(even_fib(key), val)

    def test_type(self):
        for elem in even_fib(10):
            self.assertIsInstance(elem, int)

    def test_even(self):
        for elem in even_fib(100):
            self.assertTrue(elem % 2 == 0)

    def test_raises(self):
        cases = [-1, 'abc', 3.14, 2.0]
        for case in cases:
            with self.subTest(case=case):
                self.assertRaises(ContractNotRespected, even_fib, case)


if __name__ == '__main__':
    unittest.main()
