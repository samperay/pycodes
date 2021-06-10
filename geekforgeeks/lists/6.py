# Python | Reversing a List

l = [1, 2, 3, 4, 5, 6]

print("actual list: ", l)
print("Method-1: reverse list: ", l[::-1])

l1=[]
count = len(l)-1
while count>=0:
    l1.append(l[count])
    count-=1

print("Method-2: reverse list:", l1)

