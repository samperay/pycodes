def palindrome(word1, word2):
  if len(word1) != len(word2):
    return 'No words equal'

  i = 0 
  j = len(word2)-1

  while j>0:
    if word1[i] != word2[j]:
      return "Not a Palindrome"
    i=i+1
    j=j-1

  return "palindrome"

print(palindrome('mom', 'mom'))