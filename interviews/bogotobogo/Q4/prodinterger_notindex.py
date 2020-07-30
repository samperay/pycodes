# Product of every integer except the integer at that index
#We have a list of integers, and for each index we want to find the product of
#every integer except the integer at that index.

#  [2, 3, 5, 4] ==> [60, 40, 24, 30]

def product(a):
    prod=1
    result=[]
    for x in a:
        prod*=x
    for x in a:
        result.append(int(prod/x))
    return result

print(product([2, 3, 5, 4]))
