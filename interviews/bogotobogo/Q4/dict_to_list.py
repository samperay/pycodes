# Using list as the default_factory, we can group a sequence of key-value pairs into a dictionary of lists.
# For example, we need to convert the following:


elem = {23:'James',42:'Julie',18:'Jane',31:'Julie', 55:'Joshua',34:'James'}

# first method
from collections import defaultdict
d = defaultdict(list)
for k,v in elem.items():
    d[v].append(k)
print(d)

# second method
d = {}
for k,v in elem.items():
    d.setdefault(v,[]).append(k)
print(d)
