l = list(range(10))
print("Original List: ", l)

# 1. Python program to interchange first and last elements in a list

first_index = 0
last_index = len(l)-1

first_ele=l[first_index]
last_ele=l[last_index]


l[last_index] = first_ele
l[first_index] = last_ele

print("After Modifying first and last element in list: ", l)

