# -*- coding: utf-8 -*-
"""Main module."""


def primefactor(x: int) -> list:
    """Factorize positive integer and return its factors.

    :type x: int,>=0
    :rtype: tuple[N],N>0

    """
    if isinstance(x, (str, float)):
        raise TypeError
    if x < 0:
        raise ValueError

    res = []
    p = 2
    while x >= p**2:
        if x % p == 0:
            res.append(p)
            x = int(x / p)
        else:
            p += 1

    res.append(x)
    return tuple(res)


if __name__ == '__main__':
    print(primefactor(128009973))
