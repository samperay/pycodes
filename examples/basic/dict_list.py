# Create dictionary of list

# Dictionary
elem={23:'James',42:'Julie',18:'Jane',31:'Julie', 55:'Joshua',34:'James'}

# converting to a dict of list
#{'Jane': [18], 'James': [34, 23], 'Julie': [42, 31], 'Joshua': [55]}

from collections import defaultdict
d=defaultdict(list)
for k,v in elem.items():
    d[v].append(k)

# Creating dictionary of list
print(dict(d))

# convert to a list
print(list(d))
