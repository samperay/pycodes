import collections
a = [10,30,50,70,70,30,40,30,10]

# manual method to see collections.Counter(list) output
b=collections.Counter(a)
print(b)

# first method
for k,v in collections.Counter(a).items():
    print(k,v)

# second method
# print single list to find out duplicates in the list
print([k for k,v in collections.Counter(a).items() if v>1 ])

# third method
# intialize the dict with key:value pair
d={}
for k in a:
    d[k]=0

for k in a:
    d[k]+=1
print([k for k,v in d.items() if v>1])

# fourth method
d1={}
for key in a:
    d1[key]=d1.get(key,0)+1
print([k for k,v in d1.items() if v>1])

# fifth method
s=set(a)
print([k for k in s if a.count(k)>1])
