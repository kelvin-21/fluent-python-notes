from functools import partial


def add(a, b):
    return a + b


add10 = partial(add, 10)
assert add10(20) == 30
