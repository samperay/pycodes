# Hashable
# The key of a dictionary should be unique and the key is transferred as hash function and then
# become an index to a memory where the value is stored.

# That's why we always use hashable objects as keys. Hashable objects are integers, floats, strings, tuples,
# and frozensets.
# Note that all hashable objects are also immutable objects.

# Mutalbe objects are lists, dictoroaries, and sets.

d={}

t1 = (1,2)
t2 = (3,4,5)

d[t1] = 2
d[t2] = 3
print(d)
print(d[t1], d[t2])
