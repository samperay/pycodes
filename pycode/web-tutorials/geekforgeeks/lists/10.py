# Python program to print even numbers in a list

l = [4, 6, 1, 8, 5, 2, 3, 10, 0]

print("List of all even numbers: ")
for each in l:
    if each % 2 == 0:
        print(each, end = ' ')

# Python program to print all even numbers in a range

print("List of even numbers in range ..")
even_list = []
for i in range(0, 10, 2):
    even_list.append(i)
print(even_list)