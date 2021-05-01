# String reverse

# # Method 1
# string="When you know better, you do better."
# print("revstr Method:1",string[::-1])
#
# # Method 2
# for i in range(len(string)):
#     print(''.join(string[-i-1]))

# Reverse the sentence
string1 = "My name is Sunil Kumar"
# Output = Kumar Sunil is name My

liststr=string1.split()
r_words=liststr[::-1]

for word in r_words:
    print(''.join(word))

print(word)

# using list comphrension, we can get the reverse of the string. 
print(''.join(string[i] for i in range(len(string1-1,-1,-1)))

# Print the revese of the string in an iteratvive method.
# You can either define the argument in the code or taken from CLI
print("--------------")
print("iterative way")
print("--------------")

import sys

if len(sys.argv)>1:
  string=str(sys.argv[1])
else:
  string="sunil"

# The index of the array of the string starts always from 0
# 0 to len(str)-1
strlen=len(string)
j=strlen-1

while (j>=0):
    print(string[j])
    j-=1
