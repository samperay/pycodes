# Count the occurances of char in each word

sentence='The Mississippi River'
# convert sentence into small letters

s=sentence.lower()
print("Method-1")
for c in s:
    print(c,":",s.count(c))

# Method 2
print("Method-2")
list1=str(s)
list2=list(map(s.count,s))
map_list=list(zip(list1,list2))
for list_tuple in map_list:
    print(list_tuple)

# Method 3
print("Method-3")
d={}.fromkeys([x for x in s],0)
print(d)

# Method 4
print("Method-4")
d1=dict((c,s.count(c)) for c in s)
print(d1)
