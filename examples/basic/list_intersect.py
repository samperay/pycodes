# Find out the intersection of the lists

# Method - 1
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
output = [i for i in a if i in b]
print("Method -1: ",output)

# Method - 2
output1= list(set(a) & set(b))
print("Method -2: ",output1)
