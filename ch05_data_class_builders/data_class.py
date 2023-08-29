from dataclasses import dataclass


@dataclass()
class Person:
    name: str
    age: int

    def aging(self):
        self.age += 1


@dataclass(frozen=True)
class PersonImmutable:
    name: str
    age: int

    def aging(self):
        self.age += 1


j = Person('jason', 20)
p = PersonImmutable('peter', 21)
