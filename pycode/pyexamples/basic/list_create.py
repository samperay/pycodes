# Generate lists

# Firts method of making a list
L = list(range(10))
print("List-Method1:",L)

# second method of making a list
L1=[]
for i in range(10):
    L1.append(i)
print("List-Method2:",L1)

# Use generators for creationg list
print("List-Method3:",[x for x in range(10)])

# List comprehension
L = list(range(10))
L1 = [x**2 for x in L]
L2 = [x**2 for x in range(10)]
print("List of Squares:",L1)
print("List of Squares:",L2)
