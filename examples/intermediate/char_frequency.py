# Find the occurances of the char in the words

s="Mississippi borders Tennessee"

# init dict
d={}.fromkeys(s,0)

for c in s:
    d[c]+=1
print(d)
