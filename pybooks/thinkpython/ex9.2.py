"""
Exercise 9.2.
Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in
it.
Modify your program from the previous section to print only the words that have no “e” and compute
the percentage of the words in the list have no “e.”
"""

# fp=open('E:\projects\practice-python\interviews\/thinkpython\words.txt','r')
# noletter='e'
# for eachword in fp.readlines():
#     if 'e' not in eachword:
#         print(eachword)
# fp.close()


"""
Exercise 9.3. Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.

Modify your program to prompt the user to enter a string of forbidden letters and then print the
number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?
"""

def avoid(word,forbid):
    for letter in word:
        if letter == forbid:
            return False
    return True
print(avoid('sunil','m'))


"""
Exercise 9.4. Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. Can you make a sentence using only
the letters acefhlo? Other than “Hoe alfalfa?”
"""


"""
Exercise 9.5. Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many words are
there that use all the vowels aeiou? How about aeiouy?
"""


"""
Exercise 9.6. Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok). How many abecedarian words are there?
"""
