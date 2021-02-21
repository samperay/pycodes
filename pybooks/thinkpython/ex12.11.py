"""
12.11 Exercises
"""

"""
Exercise 12.3. Write a function called most_frequent that takes a string and prints the letters
in decreasing order of frequency. Find text samples from several different languages and see
how letter frequency varies between languages. Compare your results with the tables at http: //
en. wikipedia. org/ wiki/ Letter_ frequencies . Solution: http: // thinkpython. com/
code/ most_ frequent. py .
"""

"""
Exercise 12.4. More anagrams!
1. Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of
words that are anagrams.
Here is an example of what the output might look like:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
Hint: you might want to build a dictionary that maps from a set of letters to a list of words
that can be spelled with those letters. The question is, how can you represent the set of letters
in a way that can be used as a key?

2. Modify the previous program so that it prints the largest set of anagrams first, followed by the
second largest set, and so on.

3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on
the board, to form an eight-letter word. What set of 8 letters forms the most possible bingos?
Hint: there are seven.
"""

"""
Exercise 12.5. Two words form a “metathesis pair” if you can transform one into the other by
swapping two letters; for example, “converse” and “conserve.” Write a program that finds all of
the metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and don’t test all possible
swaps. Solution: http: // thinkpython. com/ code/ metathesis. py . Credit: This exercise is
inspired by an example at http: // puzzlers. org .
Exercise 12.6. Here’s another Car Talk Puzzler (http: // www. cartalk. com/ content/
puzzlers ):
What is the longest English word, that remains a valid English word, as you remove its
letters one at a time?
Now, letters can be removed from either end, or the middle, but you can’t rearrange any
of the letters. Every time you drop a letter, you wind up with another English word. If
you do that, you’re eventually going to wind up with one letter and that too is going
to be an English word—one that’s found in the dictionary. I want to know what’s the
longest word and how many letters does it have?
I’m going to give you a little modest example: Sprite. Ok? You start off with sprite,
you take a letter off, one from the interior of the word, take the r away, and we’re left
with the word spite, then we take the e off the end, we’re left with spit, we take the s off,
we’re left with pit, it, and I.
Write a program to find all words that can be reduced in this way, and then find the longest one.
This exercise is a little more challenging than most, so here are some suggestions:
1. You might want to write a function that takes a word and computes a list of all the words that
can be formed by removing one letter. These are the “children” of the word.
2. Recursively, a word is reducible if any of its children are reducible. As a base case, you can
consider the empty string reducible.
3. The wordlist I provided, words.txt, doesn’t contain single letter words. So you might want
to add “I”, “a”, and the empty string.
4. To improve the performance of your program, you might want to memoize the words that are
known to be reducible.
Solution: http://thinkpython.com/code/reducible.py
"""
