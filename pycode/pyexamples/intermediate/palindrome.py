# check for palindrome

# Method 1
word = "mom"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

   # Or
# The same code above can be used as terenary operator
word1 = "mom1"
print("Palindrome") if word1 == word1[::-1] else print("Not a palindrome")
# or range(len,stop_index,step_size)
print("Palindrome") if word1 == ''.join([word1[i] for i in range(len(word1)-1,-1,-1)]) else print("Not a palindrome")
