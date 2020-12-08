"""
Exercise 8.1. Write a function that takes a string as an argument and displays the letters backward,
one per line.
"""

def letter_backward(s):
    """
    print letter backward
    """
    reverseword=""
    index = len(s)-1
    while index >= 0:
        reverseword=reverseword+s[index]
        index-=1
    return reverseword

print("lettes in backwards:",letter_backward('sunil'))


# fruit = 'banana'
#
# print("using while loop")
# index=0
# while index < len(fruit):
#     print(fruit[index])
#     index+=1

# print("Using for loop")
# for char in fruit:
#     print(char)


"""
Exercise 8.2. Modify the program to fix this error.

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    print letter + suffix
The output is:
Jack
Kack
Lack
Mack
Nack
Oack
Pack
Qack
"""

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter+'u'+suffix)
    else:
        print(letter+suffix)
