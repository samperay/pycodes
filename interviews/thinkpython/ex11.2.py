def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

output = histogram('brontosaurus')
print(output)

"""
Exercise 11.2. Dictionaries have a method called get that takes a key and a default value. If the
key appears in the dictionary, get returns the corresponding value; otherwise it returns the default
value.
"""

# write above code using get from dictionaries
