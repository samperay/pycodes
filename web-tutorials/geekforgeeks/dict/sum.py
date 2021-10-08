# Python program to find the sum of all items in a dictionary

d = {'one': 1, 'two': 2}

sum = 0
for k, v in d.items():
    sum = sum + v

print("Sum using dicts:", sum)