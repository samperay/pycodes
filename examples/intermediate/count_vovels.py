#!/usr/bin/python

#Program to Count the Number of Each Vowel
import sys
a=e=i=o=u=0

if len(sys.argv) != 1: #find the length of arguments passed from command line.
  string=sys.argv[1]
else:
  string="elephant" # No arguments passed, choose this as default string

for eachchar in string:
  if eachchar=='a':
      a+=1
  elif eachchar=='e':
      e+=1
  elif eachchar=='i':
      i+=1
  elif eachchar=='o':
      o+=1
  elif eachchar=='u':
      u+=1

print('a:',a)
print('e:',e)
print('i:',i)
print('o:',o)
print('u:',u)
print("\n")
print("*"*30)

# Second Method of counting vovels using dictionary
print("Second Method using dictionary")
print("*"*30)
vovels='aeiou'

if len(sys.argv) != 1: #find the length of arguments passed from command line.
  string=sys.argv[1]
else:
  string="elephant" # No arguments passed, choose this as default string

vovels_count = {}.fromkeys(vovels,0)

for char in string:
    if char in vovels_count:
        vovels_count[char]+=1
print(vovels_count)

print("\n")
