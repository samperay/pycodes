# Create dict using tuples

list_of_tuple = [('one',1),('two',2),('three',3)]
d={}
for t in list_of_tuple:
    d[t[0]]=t[1]
print(d)
