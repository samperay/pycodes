# List - append vs extend vs concatenate
a = [1,2]
b = [3,4,5]
c = a.append(b) # modifying a
print(a,c)

a = [1,2]
b = [3,4,5]
c = a.extend(b) # modifying a
print(a,c)

a = [1,2]
b = [3,4,5]
c = a + b  # creating a new list
print(a,c)

# use sorted list to keep original list
a = [3,2,1]
# original list retained
a2 = sorted(a)
print(a,a2)
# original list changed
a3 = a.sort()
print(a,a3)

# count from list
L = [1,1,2,3,4,5,6,6,6]
from collections import Counter
print(Counter(L))

#intersection of two list

# method -1
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print("Intersection of two lists - Method 1:",filter(lambda x: x in a, b))

# second method
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print("Intersection of two lists - Method 2:", [x for x in a if x in b])

# third method
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print("Intersection of two lists - Method 3:", list(set(a) & set(b)))


def rotation(a,n):
    return(a[n:]+a[:n])

a = [1,2,3,4,5]

# left
print("Rotating list to left",rotation(a,1))
print("Rotating list to left",rotation(a,2))

# right
print("Rotating list to right",rotation(a,-1))
print("Rotating list to right",rotation(a,-2))
