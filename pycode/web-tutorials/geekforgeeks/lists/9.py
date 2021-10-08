# Python program to find smallest number in a list

l = [4, 6, 1, 8, 5, 2, 3, 10, 0]
last_index = len(l)-1
last_second_index = len(l)-2
l.sort()

print("Smallest number in a list: ", l[0])
print("Largest number in a list: ", l[last_index])
print("Second largest number in a list: ", l[last_second_index])
