# Testing approaches

Write a simple sorting algorithm and apply various testing approaches:
- [Doctest](#doctest)
- [Contracts](#contracts)
- [Self-written tests](#self-written-tests)
- [Unittest](#unittest)
- [Pytest](#pytest)

The code of the function is placed in `main.py`:
```
def ssort(a: list) -> list:
    """ Slow sorting of the list using Bubble Sort algorithm."""

    a_sorted = list(a)
    for _ in range(len(a) - 1):
        for k in range(len(a) - 1):
            if a_sorted[k] > a_sorted[k + 1]:
                a_sorted[k], a_sorted[k + 1] = a_sorted[k + 1], a_sorted[k]
    return a_sorted
```


## Doctest

Add the following lines to the function description (docstring):
```
>>> ssort([4, 3, 5])
[3, 4, 5]
```
Now it can possible to test the value function returns using `doctest` module (https://docs.python.org/3/library/doctest.html):

`$ python main.py`


## Contracts

As an example of testing preconditions and postconditions, use the _Pycontracts_ (https://andreacensi.github.io/contracts/) that allows to declare constraints on function parameters and return values.

Contracts can be specified in three ways. It is enough to use one of:

1. __Using the `@contract` decorator__:
```
@contracts.contract(a='list[N]', returns='list[N]')
def ssort(a):
    ...
```
The input parametr and the return value of the function are lists of the same length: `list[N]`.

2. __Using annotations__:
```
def ssort(a: list) -> list:
    ...
```
The values can be specified as in previous option. But the may be a problem with cheking the code by the linter. 

3. __Using docstrings, with the `:type:` and `:rtype:` tags__:
```
def ssort(a: list) -> list:
    """Slow sorting of the list using Bubble Sort algorithm.

    :type a: list[N]
    :rtype: list[N]

    """
```
If the project necessarily uses docstrings, then this option is probably most suitable.

To run: `$ python contract_tests.py`

In production, all checks can be disabled using the function `contracts.disable_all()`


## Self-written tests

Check the following features of algorithm: 
 - working with simple cases, 
 - stability, 
 - universality, 
 - scalability.

To beging with, write unit tests without using any specialized libraries or frameworks for testing:

`$ python sw_tests.py`


## Unittest

Use `unittest` module (https://docs.python.org/3/library/unittest.html) to rewrite the same tests:

`$ python unit_tests.py`


## Pytest

_Pytest_ library (https://docs.pytest.org/) understands tests written using `unittest` module. But the documentation [recommends](https://docs.pytest.org/how-to/unittest.html) using plain `assert`-statement to check conditions:

`$ pytest pytest_tests.py`
