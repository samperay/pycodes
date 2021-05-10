# we did not modify the decorated function, price(), at all.
def dollar(function):
    def new(*args):
        return '$'+str(function(*args))
    return new

@dollar
def price(amount, tax_rate):
    return amount + amount*tax_rate

print(price(100,0.1))

# Write a code doubling the return value from oldFnc() just by adding a decorator like this:

def doubleIt(function):
    def new(*args):
        return function(*args)**2
    return new

@doubleIt
def oldFnc(n):
   return n

print("Square of function:",oldFnc(5))
