# TDD on the example of prime factor algorithm

Use [test-driven development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development) approach to write a function that takes non-negative integer as an argument, decomposes this number to prime factors (factorization) and returns a list of these factors.


## Brief intro to TDD

A graphical representation of the test-driven development lifecycle (from [Wikipedia](https://en.wikipedia.org/wiki/Test-driven_development)): 
<img src="https://upload.wikimedia.org/wikipedia/commons/0/0b/TDD_Global_Lifecycle.png">


## Write the tests

Before writing the function code, formalize specification for it in the form of test cases using `unittest` library. See the file `tests.py`.

Check the following test cases:

    1. Wrong types;
    2. Negative numbers;
    3. Simple cases: 0, 1;
    4. Simple numbers;
    5. Two factors;
    6. Many factors.

It is not neccesary to use a specific module for testing. It can be any other (for example, `pytest`) or even manually writing tests. A brief inroduction to unit testing approaches is presented [here](https://github.com/ptaiga/examples/tree/master/utestapproaches).


## Start development

To file `main.py` add a brief description of the function and the processing of incorrect input data.

```
def primefactor(x: int) -> list:
    """Factorize positive integer and return its factors.

    :type x: int,>=0
    :rtype: tuple[N],N>0

    """
    if isinstance(x, (str, float)):
        raise TypeError
    if x < 0:
        raise ValueError
```

Some of the tests will already be passed.


## Implement the algorithm

The flow chart of [prime factor algorithm](https://people.revoledu.com/kardi/tutorial/BasicMath/Prime/Algorithm-PrimeFactor.html): 

<img src="https://people.revoledu.com/kardi/tutorial/BasicMath/Prime/image/Algorithm-PrimeFactor_clip_image002.jpg">

Add the implementation of the described algorithm:
```
def primefactor(x):
    ...
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
```
Now the function is ready and must pass all test cases.

To run the tests: `python tests.py`.


## Used sources

- Test-driven development (TDD): https://en.wikipedia.org/wiki/Test-driven_development

- Approaches to unit testing: https://github.com/ptaiga/examples/tree/master/utestapproaches

- Prime factor algorithm: https://people.revoledu.com/kardi/tutorial/BasicMath/Prime/Algorithm-PrimeFactor.html