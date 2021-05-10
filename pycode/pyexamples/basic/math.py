# Calculate sum to range of numbers
print("Sum ",sum(list(range(10))))

# Calculate sum of even numbers
# 0+2+4+6+8
print("Sum of even-1",sum(list(range(0,10,2))))
print("Sum of even-2",sum(x for x in range(10) if x%2 == 0))
print("Sum of even-3",sum(filter(lambda x:x%2 ==0, [x for x in range(10)])))

sums=0
for i,v in enumerate(range(10)):
    if i%2 == 0:
        sums+=v
print("Sum of even-4",sums)

# Calculate sum of odd numbers
#1+3+5+7+9
print("Sum of odd-1",sum(list(range(1,10,2))))

# Product/Multiply
# We have an array of integers, and for each index we want to find the product of
# every integer except the integer at that index

l1=[5,7,3,4]
output=[]
for i,e1 in enumerate(l1):
    prod=1
    for j,e2 in enumerate(l1):
        if i!=j:
            prod*=e2
    output.append(prod)
    print("Product List:",output)
print("Final Result:",prod)

# List of even numbers using list comprehension
L=list(range(20))
even_out=[]
list_of_even_num=[x for x in L[::2] if x%2 ==0 ]
print("List of even numbers #1:", list_of_even_num)
for i,v in enumerate(L):
    if i%2 == 0:
        even_out.append(v)
print("List of even numbers #2:", even_out)

                #   or
print("List of even numbers #3:",[v for i,v in enumerate(L) if i%2 == 0 ])

# Define list of integers divisible by 5

def divisor(n,div):
    for i in range(n):
        if i%div == 0:
            yield i

dividor=5
number=51
print("Numbers for multiplications of 5:",[i for i in divisor(number,dividor)])

# Count the number of times number iterated from the list
from collections import Counter
newlist = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
counter_items=dict((Counter(newlist).items()))
# only for keys -> counter_items.keys()
# only for values -> counter_items.values()
print("{keys:value}:",dict(counter_items))
