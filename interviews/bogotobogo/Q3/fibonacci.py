# Fibonacci I - iterative, recursive, and via generator
# Write a code that prints out n Fibonacci numbers.

# iterative
def fibi(n):
    a,b=0,1
    for i in range(0,n):
        a,b=b,a+b
    return a

fibilist=[]
for i in range(5):
    fibilist.append(fibi(i))
print("iterative method:",fibilist)


# recursive
def fibr(n):
    if n==0: return 0
    if n==1: return 1
    return fibr(n-2)+fibr(n-1)

fibrlist=[]
for i in range(5):
    fibrlist.append(fibr(i))
print("recursive method:",fibrlist)

# generator
def fibg(n):
    a,b=0,1
    for i in range(n):
        yield "({},{})".format(i,a)
        a,b=b,a+b

for i in fibg(5):
    print(i)
