"""
Exercise 10.5. Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None
"""

def chop(l):
    f_index=0
    # remove the first elmenet using the index
    l.pop(f_index)
    # by default, pop always remove the last element
    l.pop()

    # return the final list which is same as the original list
    return l

result = chop([1,2,3,4])
print("chopped values of first and last index of the same list:", result)
