string = "sunil"

# first method of reverse of the string
print("Method-1: ", string[::-1])

# second method of reverse
strlen = len(string)
j = strlen - 1
revlist = []

i = 0
while i<=j:
    revlist.append(string[j])
    j = j - 1

print("Method-2: ", end=' ')
print("".join(revlist))

