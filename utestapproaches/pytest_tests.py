# -*- coding: utf-8 -*-
"""Unit tests for sorting algotithm."""

from main import ssort as sort_algorithm


def is_not_in_descending_order(a: list) -> bool:
    """Check if the list is not descending order."""
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True


def test_simple_cases():
    cases = ([], [0], [1, 2], [1, 2, 3, 4, 5],
             [4, 1, 3, 5, 2], [4, 3, 4, 3, 5],
             list(range(20)), list(range(20, 1, -1)))
    for b in cases:
        a = sort_algorithm(b)
        assert len(a) == len(b), \
            'The number of elements has changed: ' + str(a)
        assert is_not_in_descending_order(a), 'List not sorted: ' + str(a)


def test_stability():
    cases = ([[99] for i in range(5)],
             [[1, 2], [1, 2], [2, 2], [2, 2], [3, 2], [3, 2]],
             [[0, 1] for i in range(50)] + [[20, 10] for i in range(50)])
    for b in cases:
        a = sort_algorithm(b)
        b.sort()
        assert all(x is y for x, y in zip(a, b)), \
            'Sorting algorith changed equal value.'


def test_universality():
    cases = (list('qwerty'), [1.0 / i for i in range(1, 11)],
             [[1], [1, 2], [1, 2, 3], [2, 3], [], [0]],
             [True, False])
    for b in cases:
        a = sort_algorithm(b)
        assert len(a) == len(b), \
            'The number of elements has changed: ' + str(a)
        assert is_not_in_descending_order(a), 'List not sorted: ' + str(a)


def test_scalability(max_scale=100):
    cases = (
        list(range(max_scale)), list(range(max_scale, 0, -1)),
        list(range(max_scale // 2, max_scale)) + list(range(max_scale // 2))
    )
    for b in cases:
        a = sort_algorithm(b)
        assert len(a) == len(b), \
            'The number of elements has changed: ' + str(a)
        assert is_not_in_descending_order(a), 'List not sorted: ' + str(a)
