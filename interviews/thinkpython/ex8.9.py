# compare two words and find the reverse of the words

"""
Exercise 8.9. Starting with this diagram, execute the program on paper, changing the values of i
and j during each iteration. Find and fix the second error in this function.
"""
# string is out of index, as len would return exact value of the string, inorder to find the index
# length -1
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)-1  # fixing the code in this line
    while j > 0:
        if word1[i] != word2[j]:
            return False
            i = i+1
            j = j-1
    return True

res = is_reverse('pots','stop')
print(res)
