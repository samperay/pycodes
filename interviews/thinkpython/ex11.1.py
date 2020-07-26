"""
Exercise 11.1. Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary.
"""
def dictfile(searchitem):
    d={}
    fp = open("E:\projects\practice-python\interviews\/thinkpython\words.txt")
    for line in fp.readlines():
        key=line.rsplit('\n')[0]
        d[key]=key
    if searchitem in d:
        return True
    else:
        return False

print(dictfile("abc"))
