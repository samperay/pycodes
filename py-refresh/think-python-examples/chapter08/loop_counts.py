# word = 'banana'
# count = 0
# for letter in word:
#   if letter == 'a':
#     count = count + 1
#   print count

# Exercise 8.5 Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

def count(word, letter):
  count=0
  for eachletter in word:
    if letter == eachletter:
      count=count+1 
  return count

print(count("Sunilll",'i'))

