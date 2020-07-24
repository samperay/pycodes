"""
Exercise 10.4. Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. So middle([1,2,3,4]) should return [2,3].
"""

def middle(l):
    newlist=[]
    index=1
    while index<len(l)-1:
        newlist.append(l[index])
        index+=1
    return newlist


result = middle([1,2,3,4])
print("List left with only middle values:", result)
