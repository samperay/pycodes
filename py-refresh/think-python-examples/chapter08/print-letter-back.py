# Exercise 8.1 Write a function that takes a string as an argument and displays the letters backward, one per line

#!/usr/bin/python

name = input("Enter String: ")
index = len(name)-1

while index>=0:
  letter = name[index]
  print(letter)
  index=index-1

  