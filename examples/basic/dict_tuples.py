# Create dict using tuples

# First Method
list_of_tuple = [('one',1),('two',2),('three',3)]
d={}
for t in list_of_tuple:
    d[t[0]]=t[1]
print("First Method: ",d)

# Second Method
print("Second Method: ",dict(list_of_tuple))
