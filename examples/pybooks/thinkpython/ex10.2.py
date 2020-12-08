"""
Exercise 10.2. Use capitalize_all to write a function named capitalize_nested that takes
a nested list of strings and returns a new nested list with all strings capitalized.
"""

def capitalize_nested(l):
    newcaplist = []

    for word in l:
        newcaplist.append(word.capitalize())

    return newcaplist

def uppercase_nested(l):
    uppercaselist = []
    for word in l:
        uppercaselist.append(word.upper())
    return uppercaselist

output = capitalize_nested(["python","program"])
print("Captilize List of Strings: ",output)

uppercaseout = uppercase_nested(["python","program"])
print("Uppercase output",uppercaseout)
