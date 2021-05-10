sentence='The Mississippi River'

def count_char(s):
    count = list(map(s.count,s))
    print(count)
    return (max(count))

print(count_char(sentence))

s1=sentence.lower()
d={}.fromkeys([x for x in s1],0)
print(d)

for char in s1:
    d[char]+=1
print(d)

d1={}
for c in s1:
    d1[c]=d.get(c,0)+1
print(d1)
