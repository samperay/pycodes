"""
11.10 Exercises
"""

"""
Exercise 11.9. If you did Exercise 10.8, you already have a function named has_duplicates that
takes a list as a parameter and returns True if there is any object that appears more than once in the
list.
Use a dictionary to write a faster, simpler version of has_duplicates.
"""

def has_duplicates(l):
    d={}
    for word in l:
        d[word]=d.get(word,0)+1

    for k,v in d.items():
        if v>=2:
            return k
        else:
            return False

result = has_duplicates(['brontosaurus','thinkpython','brontosaurus'])
print("Items repeating in list:", result)


"""
Exercise 11.10. Two words are “rotate pairs” if you can rotate one of them and get the other (see
rotate_word in Exercise 8.12).
Write a program that reads a wordlist and finds all the rotate pairs.
"""
