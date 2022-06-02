# -*- coding: utf-8 -*-
"""Sorting algorithm with docstring-testing."""


def ssort(a: list) -> list:
    """Slow sorting of the list using Bubble Sort algorithm.

    >>> ssort([4, 3, 5])
    [3, 4, 5]

    """
    a_sorted = list(a)
    for _ in range(len(a) - 1):
        for k in range(len(a) - 1):
            if a_sorted[k] > a_sorted[k + 1]:
                a_sorted[k], a_sorted[k + 1] = a_sorted[k + 1], a_sorted[k]
    return a_sorted


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(ssort([4, 3, 2]))
