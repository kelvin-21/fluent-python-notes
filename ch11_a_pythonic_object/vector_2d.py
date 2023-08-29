import math


class Vector2d:
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
