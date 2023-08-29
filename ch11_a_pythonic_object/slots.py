import math
from sys import getsizeof
from ch11_a_pythonic_object.vector_2d import Vector2d


class Vector2dSlots:
    """Using __slots__ to save memory. The private attribute __dict__ will no longer present"""
    __slots__ = ('__x', '__y')

    def __init__(self, x, y):
        self.__x = float(x)  # convert to float to catch error early
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.x}, {self.y})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        ...

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        """
        Best practices: (Python won't check it for you. You check.)
        1. Objects having the same hash should be equal, and vice versa
        2. The hashed properties should be immutable throughout the lifetime of the object.
        """
        return hash((self.x, self.y))

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, format_spec=''):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coordinates = (abs(self), self.angle())
            outer_format = '<{}, {}>'
        else:
            coordinates = self
            outer_format = '({}, {})'
        components = (format(c, format_spec) for c in coordinates)
        return outer_format.format(*components)


if __name__ == '__main__':
    v = Vector2d(1, 2)
    v2 = Vector2dSlots(1, 2)
    print(getsizeof(v))
    print(getsizeof(v2))
