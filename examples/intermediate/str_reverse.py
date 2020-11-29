# String reverse

# # Method 1
# string="When you know better, you do better."
# print("revstr Method:1",string[::-1])
#
# # Method 2
# for i in range(len(string)):
#     print(''.join(string[-i-1]))

# Reverse the sentence
string1 = "My name is Sunil Kumar"
# Output = Kumar Sunil is name My

liststr=string1.split()
r_words=liststr[::-1]

for word in r_words:
    print(''.join(word))

print(word)
