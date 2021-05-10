"""
filter() takes two args: (fn, sequence), and returns a list
The filter() will return all items from the list a which return True
when passed to the function check()
"""

a = [1,2,4,1,2,3]
s = set(a)

def check(n):
   if n in s:
      return True
   else:
      return False

print(list(filter(check, a)))
