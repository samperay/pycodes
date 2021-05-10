L = [x*10 for x in range(10)]
print(L)

# list every second item in the list
print("First Method:",L[::2])

#second method
L1=[]
for k,v in enumerate(L):
    if k%2 ==0:
        L1.append(v)
print("Second Method:",L1)
