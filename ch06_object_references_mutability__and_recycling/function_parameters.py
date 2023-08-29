"""
Function parameters are passed by sharing. 
Each formal parameter of the function gets a copy of each reference in the arguments.
"""


def f(x, y):
    x += y
    return x


a, b = 1, 2
result = f(a, b)
assert a == 1  # value is not changed
assert result == 3

t1, t2 = (1, 2), (3, 4)
result = f(t1, t2)
assert t1 == (1, 2)
assert result == (1, 2, 3, 4)

l1, l2 = [1, 2], [3, 4]
result = f(l1, l2)
assert l1 == [1, 2, 3, 4]  # mutable objects are passed by reference
assert result == [1, 2, 3, 4]
assert result is l1


"""
Mutable types as param default is a bad idea.
"""
