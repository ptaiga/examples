# -*- coding: utf-8 -*-
"""Main module.

To start execution, use:
`$ python main.py`

"""

import doctest

from contracts import contract, new_contract


@new_contract
def even(x: int) -> None:
    """Check even numbers."""
    if x % 2 != 0:
        raise ValueError('The number {0} is not even.'.format(x))


@contract(n='int,>=0', returns='list[>=0](int,>=0,even)')
def even_fib(n: int) -> list:
    """Return a list of n even numbers of the Fibonacci sequence.

    >>> even_fib(4)
    [0, 2, 8, 34]

    """
    if n == 0:
        return []

    f = [0, 1]
    res = [0]
    while len(res) < n:
        f[0], f[1] = f[1], sum(f)
        if f[1] % 2 == 0:
            res.append(f[1])
    return res


if __name__ == '__main__':
    doctest.testmod()
    print("Five even Fibonacci numbers:", even_fib(5))
