# Count the duplicates from the list

a = [10,30,50,70,70,30,40,30,10]

# Method 1
import collections

print("Method 1")
b=collections.Counter(a)
for k,v in b.items():
    if v>1:
        print(k,v)

# Method 2
print("Method 2")
# init dictionary

# d={}.fromkeys(a,0)
# or
d = {x:0 for x in a}

for i in a:
    d[i]+=1

#traverse dictionary
for k,v in d.items():
    if v>1:
        print(k,v)

    # OR

print([k for k,v in d.items() if v>1])
