def binary(n):
    b=[]
    while n > 0:
        b.append(str(n%2))
        n=n//2
    print(b)
    return b[::-1]

bb=binary(21)
print(''.join(bb))
