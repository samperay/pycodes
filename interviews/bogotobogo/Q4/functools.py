# Sometimes we just want to use a function with no name (without def).

# get odd numbers
print("Odd Nums:",list(filter(lambda x: x%2 !=0, [x for x in range(10)])))
print("Even Nums:",list(filter(lambda x: x%2 ==0, [x for x in range(10)])))

# using map functions create list of squares and cubes
print("Sqaure of Odds:",list(map(lambda x: x**2, [x for x in range(10)])))
print("Cube of Even:",list(map(lambda x: x**3, [x for x in range(10)])))
