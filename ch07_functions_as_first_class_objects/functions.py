def factorial(n):
    """returns n!"""
    return 1 if n <= 1 else n * factorial(n - 1)


print(factorial.__doc__)
help(factorial)


"""
Higher order functions are functions that take function as input or return function as output.
e.g. map, filter, reduce
"""


def f1(*, a, b):
    """keyword-only param"""
    return a, b


def f2(a, b, /):
    """positional-only param"""
    return a, b


def f3(a, b, /, c):
    return a, b, c


assert f3(1, 2, 3) == (1, 2, 3)
assert f3(1, 2, c=3) == (1, 2, 3)
