"""
Exercise 9.1. Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace).
"""

fp=open('E:\projects\practice-python\interviews\/thinkpython\words.txt','r')
for line in fp.readlines():
    if len(str(line)) > 20:
        print(line)
fp.close()
