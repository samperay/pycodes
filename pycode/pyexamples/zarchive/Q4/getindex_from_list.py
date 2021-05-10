# get index from list
mylist='abc'

for i in range(len(mylist)):
    v=mylist[i]
    print(i,v)

for i,v in enumerate(mylist):
    print(i,v)
