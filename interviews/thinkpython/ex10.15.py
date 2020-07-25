"""
10.15 Exercises
"""

"""
Exercise 10.6. Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
the elements of the list can be compared with the relational operators <, >, etc.
For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return False.
"""

def is_sorted(l):
    index=0
    while index < len(l)-1:
        if l[index] <= l[index+1]:
            print('current element smaller than next element')
        else:
            return False
        index+=1
    return True

result = is_sorted([1,2,2])
print("List is sorted: ", result)

"""
Exercise 10.7. Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.
"""

"""
Exercise 10.8. The (so-called) Birthday Paradox:
1. Write a function called has_duplicates that takes a list and returns True if there is any
element that appears more than once. It should not modify the original list.
"""

def has_duplicates(l):
    d={}
    for element in l:
        if element in d:
            return True
        d[element]=True
        print(d)
    return False

result = has_duplicates([1,2,3,4,12,1])
print("Status of Duplicates in list:", result)

"""
2. If there are 23 students in your class, what are the chances that two of you have the same
birthday? You can estimate this probability by generating random samples of 23 birthdays and
checking for matches. Hint: you can generate random birthdays with the randint function
in the random module.
You can read about this problem at http: // en. wikipedia. org/ wiki/ Birthday_ paradox ,
and you can download my solution from http: // thinkpython. com/ code/ birthday. py .
"""

"""
Exercise 10.9. Write a function called remove_duplicates that takes a list and returns a new
list with only the unique elements from the original. Hint: they don’t have to be in the same order.
"""

"""
Exercise 10.10. Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and the other using
the idiom t = t + [x]. Which one takes longer to run? Why?
Hint: use the time module to measure elapsed time. Solution: http: // thinkpython. com/
code/ wordlist. py .
"""

"""
Exercise 10.11. To check whether a word is in the word list, you could use the in operator, but it
would be slow because it searches through the words in order.
Because the words are in alphabetical order, we can speed things up with a bisection search (also
known as binary search), which is similar to what you do when you look a word up in the dictionary.
You start in the middle and check to see whether the word you are looking for comes before the word
in the middle of the list. If so, then you search the first half of the list the same way. Otherwise you
search the second half. Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will
take about 17 steps to find the word or conclude that it’s not there. Write a function called bisect that takes a sorted list and a target value and returns the index of
the value in the list, if it’s there, or None if it’s not. Or you could read the documentation of the bisect module and use that! Solution: http: //
thinkpython. com/ code/ inlist. py .
"""

"""
Exercise 10.12. Two words are a “reverse pair” if each is the reverse of the other. Write a program
that finds all the reverse pairs in the word list. Solution: http: // thinkpython. com/ code/
reverse_ pair.
"""

"""
Exercise 10.13. Two words “interlock” if taking alternating letters from each forms a new
word. For example, “shoe” and “cold” interlock to form “schooled.” Solution: http: //
thinkpython. com/ code/ interlock. py . Credit: This exercise is inspired by an example at
http: // puzzlers. org .
1. Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
2. Can you find any words that are three-way interlocked; that is, every third letter forms a
word, starting from the first, second or third?
"""
