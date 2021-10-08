# find the cube of first natural numbers
import math
num = int(input("Enter number to get squares: "))

# using generators
cubes = [i**3 for i in range(num)]
print("Square of numbers: ", cubes)

cubesum = 0
for i in cubes:
    cubesum += i
print("Sum of cubes: ", cubesum)

