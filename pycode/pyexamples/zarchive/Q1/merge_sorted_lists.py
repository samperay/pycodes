# Merging two sorted list

a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21, 0]
c = []

# join the two lists as one and sort the list and store in third list
a.extend(b)
c=sorted(a)
print(c)
