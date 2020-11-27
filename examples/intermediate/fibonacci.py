# Create a fibonacci series

# Method 1 - Iterative
def fib1(n):
    iter=[]
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a

# Method 2 - Recursive
def fib2(n):
    if n==0: return 0
    if n==1: return 1
    return fib2(n-1)+fib2(n-2)

# main func
for i in range(10):
    print("Fib #1:",fib1(i))
    print("Fib #2:",fib2(i))
