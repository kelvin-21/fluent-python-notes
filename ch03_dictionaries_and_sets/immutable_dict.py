from types import MappingProxyType
from collections import defaultdict

"""
This mapping proxy is designed to make a copy of dict to provide read-only access
"""

d = {'a': 1, 'b': 2, 'c': 3}
d_proxy = MappingProxyType(d)

assert 'a' in d_proxy
assert 'b' in d_proxy
assert 'c' in d_proxy

d['d'] = 4

assert 'd' in d_proxy


"""
However default dict will break the read-only mechanism
"""

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d_proxy = MappingProxyType(d)

assert d_proxy['a'] == 1
assert d_proxy['b'] == 2

assert d_proxy['c'] == 0  # default dict will create zero value when called with a missing key
assert 'c' in d
