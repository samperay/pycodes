# Create a enumerators
# Enumerators are used to get the indexed slices, however we can use below methods to get indexs

# Method 1
L = list(range(10))
for i in L:
    print("Method1:index,item:",i,",",L[i])

# Method 2
L = list(range(11,21))
for index,item in enumerate(L):
    print("Method2:index,item:",index,",",item)
