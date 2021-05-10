# usual code to return from function

# def f(n):
#     #list comphrensions
#     return [x**2 for x in range(5)]

# you can also use generator so as not to return value
def f(n):
    for x in range(n):
        yield(x**2)

for x in f(5):
    print(x)
