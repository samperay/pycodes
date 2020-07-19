"""
Exercise 6.2. Use incremental development to write a function called hypotenuse that returns the
length of the hypotenuse of a right triangle given the lengths of the two legs as arguments. Record
each stage of the development process as you go.
"""
import math

def sqr(x):
    return x*x

def hypotenuse(x,y):
    """
    find length of hypotenuse
    """
    result = int(math.sqrt(sqr(x)+sqr(y)))
    return result

print("Lenght of Hypotenuse",hypotenuse(3,4))
