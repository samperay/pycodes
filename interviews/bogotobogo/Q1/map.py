# map(aFunction, aSequence)
import functools

""" The first argument is a function to be executed for all the elements of the iterable given as the second argument.
If the function given takes in more than 1 arguments, then many iterables are given. """

def square(x):
    return x**2

items = [ x for x in range(10)]
print(list(map(square,items)))
