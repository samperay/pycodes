# reverse an integer

# Method 1
def rev1(n):
  r = 0
  for i in range(len(str(n))):
     r += n % 10
     n = n // 10
     # promote digits except the last digit
     if (n > 0):
       r = r * 10
  return(r)

# Method 2
def rev2(n):
    sn=str(n)
    r = ''.join(sn[-i-1] for i in range(len(sn)))
    return(r)

def rev3(n):
    return str(n)[::-1]

n=12345
print(rev1(n))
print(rev2(n))
print(rev3(n))
