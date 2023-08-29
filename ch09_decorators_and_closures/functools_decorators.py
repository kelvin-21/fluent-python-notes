from functools import cache, lru_cache, singledispatch
from collections import abc

from ch09_decorators_and_closures.clock_deco import clock


@cache
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


@clock
@lru_cache(maxsize=2)
def cube(n):
    print(f'Computing squared({n})...')
    return n ** 3


@singledispatch
def square(*args, **kwargs):
    raise TypeError(f'[Base function] Input is not supported\n\targs: {args}\n\tkwargs: {kwargs}')


@square.register
def _(x: int) -> int:
    result = x ** 2
    print(f'Compute int square<{type(x).__name__}>({x}) -> {result}')
    return result


@square.register
def _(x: float) -> float:
    result = x ** 2
    print(f'Compute float square<{type(x).__name__}>({x}) -> {result}')
    return result


@square.register
def _(x: complex) -> complex:
    result = x ** 2
    print(f'Compute complex square<{type(x).__name__}>({x}) -> {result}')
    return result


@singledispatch
def add_one(x):
    result = x + 1
    print(f'Compute base add_one<{type(x).__name__}>({x}) -> {result}')
    return result


@add_one.register(int)
def _(x):
    result = x + 1
    print(f'Compute int add_one<{type(x).__name__}>({x}) -> {result}')
    return result


@add_one.register(float)
def _(x):
    result = x + 1
    print(f'Compute float add_one<{type(x).__name__}>({x}) -> {result}')
    return result


if __name__ == '__main__':
    square(5)
    square(5.0)
    square(complex(1, 2))
    # square([1, 2.0, 3])
    # square('abc')
