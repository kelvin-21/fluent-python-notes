from collections import defaultdict
from ch02_an_array_of_sequence.immutable_tuple import ImmutableTuple


def default_element_examples():
    classes = (
        int,
        float,
        str,
        list,
        tuple,
        set,
        dict,
        ImmutableTuple,
    )

    for cls in classes:
        default_element = defaultdict(cls)['dummy']
        print(f'Default element of {cls} is <{default_element}>')


def default_dict_of_default_dict():
    """ Default dict of default dict is simplay default dict of dict """

    print('\nDefault dict of default dict is simplay default dict of dict')

    d = defaultdict(defaultdict)
    print(d[0])
    assert isinstance(d[0], defaultdict)
    try:
        d[0][0]
    except KeyError:
        print('Error')


def correct_way_define_default_dict_default_dict():
    """ The default dict takes a callable as the input, and then call it to create new instance """

    d = defaultdict(lambda: defaultdict(int))
    print(d[0])
    print(d[0][0])
    assert isinstance(d[0], defaultdict)
    assert d[0][0] == 0


default_element_examples()
default_dict_of_default_dict()
