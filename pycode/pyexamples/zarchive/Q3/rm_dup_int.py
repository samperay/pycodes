a = [1,2,9,7,5,1,2,3]
print("Current List:",a)
[a.remove(x) for x in a if a.count(x) > 1]
print("Deleted from same list:",a)
