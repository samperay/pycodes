# Exercise 10.2 Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.

# def chop(l):
  
#   x=[]
#   x=l.pop(0)
#   x=l.pop(len(l)-1)
#   print(l)
#   return None

# chop(['1','2','3'])


# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def middle(l):
  x=l
  x.pop(0)
  x.pop(len(l)-1)
  return(x)

print(middle(['1','2','3']))