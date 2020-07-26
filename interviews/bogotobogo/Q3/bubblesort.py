L = [3,1,5,7,6,4,2,8,10,9]

sorted=False
while not sorted:
    sorted=True
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            sorted=False
            temp=L[i]
            L[i]=L[i+1]
            L[i+1]=temp
    print(L,sorted)
