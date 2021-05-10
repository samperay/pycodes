# Print the factorial of the number

# Method 1 - iterative

def fact():
    n=5
    f=1
    for i in range(1,n+1):
        f*=i
    return(f)

print("factorial-method-1:",fact())

# Method 2 - recursive

def fact1(n):
    if n==0: return 1
    return n*fact1(n-1)

print("factorial-method-2:",fact1(5))
