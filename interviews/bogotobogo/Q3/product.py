# We have an array of integers, and for each index we want to find the product
# of every integer except the integer at that index.

# example
# [5, 7, 3, 4] out function should return the product of [7*3*4, 5*3*4, 5*7*4, 5*7*3]

a = [5, 7, 3, 4]
out=[]
for i,e1 in enumerate(a):
    prod=1
    for j,e2 in enumerate(a):
        if i!=j:
            prod*=e2
    out.append(prod)
print(out)
