"""
For a given pair of numbers (row x column), create an array. For example, for (4,5) pair, we want to create the following 4x5 matrix:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12]]
"""

row=4
column=5

l=[]
for r in range(row):
    l.append([c*r for c in range(column)])
print(l)
