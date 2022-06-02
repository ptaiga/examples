# -*- coding: utf-8 -*-
"""Self-writing tests for sorting algorithm."""

from random import shuffle

from main import ssort as sort_algorithm


def test_sort():
    print('Test sorting algorithm:')
    passed = True
    passed &= test_sort_works_in_simple_cases()
    passed &= test_sort_algorithm_stable()
    passed &= test_sort_algorithm_is_universal()
    passed &= test_sort_algorithm_scalability()
    print('Summary:', 'Ok' if passed else 'Fail')


def test_sort_works_in_simple_cases():
    print(' - sort algorithm works in simple cases:', end=' ')
    passed = True

    cases = ([], [0], [1, 2], [1, 2, 3, 4, 5],
             [4, 1, 3, 5, 2], [4, 3, 4, 3, 5],
             list(range(20)), list(range(20, 1, -1)))
    for case in cases:
        A2 = sorted(case)
        A1 = sort_algorithm(case)
        passed &= all(x == y for x, y in zip(A1, A2))

    print('Ok' if passed else 'Fail')
    return passed


def test_sort_algorithm_stable():
    print(' - sort algorithm is stable:', end=' ')
    passed = True

    cases = ([[99] for i in range(5)],
             [[1, 2], [1, 2], [2, 2], [2, 2], [3, 2], [3, 2]],
             [[0, 1] for i in range(50)] + [[20, 10] for i in range(50)])
    for case in cases:
        shuffle(case)
        A2 = sorted(case)
        A1 = sort_algorithm(case)
        passed &= all(x is y for x, y in zip(A1, A2))

    print('Ok' if passed else 'Fail')
    return passed


def test_sort_algorithm_is_universal():
    print(' - sort algorithm is universal:', end=' ')
    passed = True

    cases = (list('qwerty'), [i**0.5 for i in range(10)],
             [[1], [1, 2], [1, 2, 3], [2, 3], [], [0]])
    for case in cases:
        shuffle(case)
        A2 = sorted(case)
        A1 = sort_algorithm(case)
        passed &= all(x == y for x, y in zip(A1, A2))

    print('Ok' if passed else 'Fail')
    return passed


def test_sort_algorithm_scalability(max_scale=100):
    print(f' - sort algorithm on scale={max_scale}:', end=' ')
    passed = True

    cases = (
        list(range(max_scale)), list(range(max_scale, 0, -1)),
        list(range(max_scale // 2, max_scale)) + list(range(max_scale // 2)))
    for case in cases:
        shuffle(case)
        A2 = sorted(case)
        A1 = sort_algorithm(case)
        passed &= all(x == y for x, y in zip(A1, A2))

    print('Ok' if passed else 'Fail')
    return passed


if __name__ == '__main__':
    test_sort()
