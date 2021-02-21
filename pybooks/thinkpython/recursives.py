# this code would be for all the functions which has recursive funtcions

# check if numbers are integeres only
def checkint(int n):
    if n > 0:
        return True

# simple count down of numbers
def countdown(n):
    if n<0:
        print('Boom...')
    else:
        print(n)
        countdown(n-1)

countdown(3)

# factorial
def fact(n):
    # check for only integers - contraints
    if not checkint(n):
        print('Only integer values, exiting')
        return None
    elif n<0:
        return -1
    elif n==0:
        return 1
    else:
        n=n*fact(n-1)
    return n

result = fact(-5)
print("factorial of number",result)

# fibonacci
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n)+fib(n-1)
