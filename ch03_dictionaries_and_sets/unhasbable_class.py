class BasicPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonWithNameAsId:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)


class PersonWithPermanentName:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    def __eq__(self, other) -> bool:
        return self.name == other.name


class AgingPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def aging(self):
        self.age += 1

    def __eq__(self, other):
        if type(self) is type(other):
            return self.name == other.name and self.age == other.age
        return False

    def __hash__(self):
        return hash(self.name)


def is_hashable(obj) -> bool:
    try:
        hash(obj)
    except TypeError:
        return False
    return True


if __name__ == '__main__':
    p1 = BasicPerson('Jason', 25)
    print(f'p1 id: {id(p1)}')
    print(f'p1 hash: {hash(p1)}')
    print(f'p1 private hash: {p1.__hash__()}')
    assert is_hashable(p1)

    p2 = PersonWithNameAsId('Jason', 25)
    print(f'\np2 id: {id(p2)}')
    print(f'p2 hash: {hash(p2)}')
    assert is_hashable(p2)

    p3 = AgingPerson('Jason', 25)
    print(f'\np3 id: {id(p3)}')
    print(f'p3 hash: {hash(p3)}')
    p3.aging()
    print(f'aged p3 hash: {hash(p3)}')
    # assert not is_hashable(p3)
