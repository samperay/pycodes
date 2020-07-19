# find the letter in the word

def find(word, letter):
    index=0
    while index<len(word):
        if word[index] == letter:
            return True
        index+=1
    return -1

res=find('search','h')
print("Plain search results starting index from 0:",res)

"""
Exercise 8.4. Modify find so that it has a third parameter, the index in word where it should start
looking.
"""

def findindex(word,letter,position):
    index=position
    print('Staring index from position:',index)
    while index<len(word):
        if word[index] == letter:
            return True
        index+=1
    return False

respos=findindex('search','n',3)
print("Search index from position:",respos)
