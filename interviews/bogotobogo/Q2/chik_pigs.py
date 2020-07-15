"""
We have a count of 35 heads and 94 legs among the chickens and pigs in a farm.
How many pigs and how many chickens do we have?
"""

# 35 heads and 94 legs among the chickens and pigs
# c + p = 35
# 2*c + 4*p = 94
heads = 35
legs = 94
for c in range(heads):
    p = 35-c
    if 2*c + 4*p == 94:
        print(c,p)
