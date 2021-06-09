# find the sqr of first natural numbers
import math
num = int(input("Enter number to get squares: "))

# using generators
sqrs = [ i**2 for i in range(num) ]
print("Square of numbers: ",sqrs)

sqrsum = 0
for i in sqrs:
    sqrsum += i
print("Sum of Squares: ", sqrsum)
