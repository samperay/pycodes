# looping and counting

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print("Total count of letter in word: ",count)

"""
Exercise 8.5. Encapsulate this code in a function named count, and generalize it so that it accepts
the string and the letter as arguments.
"""

def count(string,letter):
    """
    counts the letter in string
    """
    found = 0
    for eachchar in string:
        if eachchar == letter:
            found+=1
    return found

res = count('banana','a')
print("Count of letter from functions", res)


"""
Exercise 8.6. Rewrite this function so that instead of traversing the string, it uses the threeparameter
version of find from the previous section.
"""


"""
Exercise 8.7. There is a string method called count that is similar to the function in the previous
exercise. Read the documentation of this method and write an invocation that counts the number of
as in 'banana'.
"""
