# factorial of the number
fact=1
n = int(input("Enter number to find the factorial: "))
while n!=0:
    print(n)
    fact = fact * n
    n=n-1

print("factorial of the number: ", fact)
