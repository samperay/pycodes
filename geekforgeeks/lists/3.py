# Python | Ways to find length of list

l = [1, 2, 3, 4, 5, 6]
print("Method-1: ", len(l))

index = 0
length = 0
while index <= len(l)-1:
    length+=1
    index+=1

print("Method-2: ", length)
