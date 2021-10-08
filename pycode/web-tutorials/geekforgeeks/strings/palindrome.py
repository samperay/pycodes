# Python program to check if a string is palindrome or not
string = "madama"

if string == string[::-1]:
    print("Method-1: Palindrome")
else:
    print("Method-1: Not Palindrome")

# Python program to check whether the string is Symmetrical or Palindrome

i = 0
j = len(string) - 1

while i<j:
    if string[i] != string[j]:
        print("String is symmetrical")
        break
    else:
        i = i + 1
        j = j - 1
    print("String is palindrome")