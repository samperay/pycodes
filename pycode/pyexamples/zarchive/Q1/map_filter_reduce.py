l = [x for x in range(10) if x%2 == 0 ]
print("List of Even Numbers using list comphrensions:", l)

m = list(filter(lambda x:x %2 ==0, [x for x in range(10)]))
print("List of Even Numbers using filter:",m)

n = list(map(lambda  x: x**2, m))
print("Square of Even Numbers:",n)

o = reduce(lambda x,y:x+y,l)
import functools
p = reduce(lambda x,y:x+y,o)
print(p)


"""
>>> integers = [ x for x in range(11)]
>>> filter(lambda x: x % 2 == 0, integers)
[0, 2, 4, 6, 8, 10]
>>> map(lambda x: x**2, integers)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> reduce(lambda x, y: x + y, integers)
55
>>>


In the first example, filter() calls our lambda function for each element of the list, and returns a new list that
contains only those elements for which the function returned "True". In this case, we get a list of all even numbers.

In the second example, map() is used to convert our list. The given function is called for every
element in the original list, and a new list is created which contains the return values
from our lambda function. In this case, it computes x^2 for every element.


Finally, reduce() is somewhat special. The function for this one must accept two arguments (x and y), not just one.
The function is called with the first two elements from the list, then with the result of that call and the third element,
and so on, until all of the list elements have been handled. This means that our function is called n-1 times
if the list contains n elements. The return value of the last call is the result of the reduce() construct.
In the above example, it simply adds the arguments, so we get the sum of all elements.

"""
