from typing import NamedTuple


class Person(NamedTuple):
    name: str
    age: int

    def aging(self):
        self.age += 1


j = Person('jason', 20)
