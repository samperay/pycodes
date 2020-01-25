# Exercise 10.3 Write a function called is_sorted that takes a list as a parameter and returns True
# if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
# the elements of the list can be compared with the comparison operators <, >, etc.
# For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return False.

def is_sorted(l):
  i=0
  j=i+1

  index=0


  while index<(len(l)-1):
    if l[i] > l[j]:
      return False
    else:
      j=j+1
      i=i+1
    index=index+1

  return True

print(is_sorted(['4','2','3']))
      
