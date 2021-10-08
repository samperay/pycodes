# Python | Program to print duplicates from a list of integers
import collections

l = [4, 6, 1, 8, 5, 2, 3, 10, 0, 4, 6, 1, 3]

b = collections.Counter(l)
print("Method-1: ")
for k,v in b.items():
    if v >1:
        print(k, end= ' ')
print("\n")

# use generators for the above code
print("Method-2 print:")
print([k for k,v in b.items() if v>1 ])


