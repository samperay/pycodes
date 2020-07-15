numbers = [1,256,64,65536,186000,1024,8,16,1905,9,88,8888,888]
d={}
for n in numbers:
    d.setdefault(len(str(n)),[]).append(n)
print(d)

"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 3,
between 1 and 100 (both included). The numbers obtained should be printed in a colon(:)-separated sequence
on a single line as shown below
"""

l = []
for n in range(1,101):
    if n % 7 == 0 and n % 3 != 0:
        l.append(str(n))
print(':'.join(l))
