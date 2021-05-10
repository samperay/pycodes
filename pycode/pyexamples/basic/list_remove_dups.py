# Remove duplicates from the list

# Method 1
a = [1,2,9,7,5,1,2,3]
print("Meth1:After dup removal,",set(a))

# Method 2
[a.remove(i) for i in a if a.count(i)>1]
print(a)
