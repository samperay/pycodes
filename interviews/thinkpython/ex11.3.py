"""
Exercise 11.3. Dictionaries have a method called keys that returns the keys of the dictionary, in
no particular order, as a list.
Modify print_hist to print the keys and their values in alphabetical order.
"""

def print_hist(ss):
    d={}.fromkeys(ss,0)
    for letter in ss:
        d[letter]+=1
    print(d)

print_hist('brontosaurus')
