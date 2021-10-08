# Python program to check whether a number is Prime or not

num = 5
flag = False

# prime numbers are greater than 1
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print("Not Prime")
else:
    print("prime!")
