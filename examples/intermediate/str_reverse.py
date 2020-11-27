# String reverse

# Method 1
string="When you know better, you do better."
print("revstr Method:1",string[::-1])

# Method 2
for i in range(len(string)):
    print(''.join(string[-i-1]))
