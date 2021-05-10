# Create a new list of union

L1=list(range(10))
L2=list(range(11,20))
L3=[]

# Union of list - Method 1
for item in L1:
    L3.append(item)
L3.extend(L2)
print("Method-1: ",L3)

# Union of list - Method 2

L1.append(L2)
print("Method-2: ",L1)
