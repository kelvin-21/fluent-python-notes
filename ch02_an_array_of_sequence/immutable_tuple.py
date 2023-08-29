from typing import Iterable, Generator


class ImmutableTuple(tuple):

    def __new__(cls, seq: Iterable = tuple(), *args, **kwargs):
        t = tuple(seq) if isinstance(seq, Generator) else seq
        for i, item in enumerate(t):
            if not cls.__is_hashable(item):
                raise TypeError(f'Item {item} at index({i}) has unhashable type {type(item)}')
        return tuple.__new__(cls, t)

    @staticmethod
    def __is_hashable(obj) -> bool:
        try:
            hash(obj)
        except TypeError:
            return False
        return True
