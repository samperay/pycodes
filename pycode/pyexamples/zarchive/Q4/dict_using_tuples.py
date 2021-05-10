list_of_tuple = [('one',1),('two',2),('three',3)]
d = {}
for item in list_of_tuple:
    d[item[0]]=item[1]
print("Dictionary of List",d)
