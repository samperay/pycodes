# Print the factorial of the number

# Method 1 - iterative

def fact():
    n=5
    f=1
    for i in range(1,n+1):
        f*=i
    return(f)

print("factorial-method-1:",fact())
