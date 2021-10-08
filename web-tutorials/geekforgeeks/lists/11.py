# Python program to print positive numbers in a list
l = [4, 6, 1, 8, 5, 2, 3, 10, 0, -1, -10, -2, -3, -11]

positive = []
negative = []

for item in l:
    if item >= 0:
        positive.append(item)
    else:
        negative.append(item)

print("positive number list: ", positive)
print("negative number list: ", negative)

# Python program to find Cumulative sum of a list of positive numbers and negative numbers

postivi_sum = 0
for item in positive:
    postivi_sum+=item

negative_sum = 0
for item in negative:
    negative_sum+=item

print("Sum of positive numbers: ", postivi_sum)
print("Sum of negative numbers: ", negative_sum)
