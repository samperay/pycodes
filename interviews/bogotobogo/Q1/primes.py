def isprime(n):
    if n == 1 :
        return False
    for t in range(2,n):
        if n % t == 0:
            return False
    return True

def primes(n=1):
    while n < 100:
        if isprime(n):
            yield n
        n+=1

for n in primes():
    print(n)
