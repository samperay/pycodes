# factorial for iterative and recursive

# iterative
def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

# recursive
def fact2(n):
   if n == 0:
      return 1
   return n * fact(n-1)

n = 5
for n in range(n):
   print('%s:%s %s' %(n, fact(n), fact2(n)))
