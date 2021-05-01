# Find the prime numbers for given numbers
# A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number
# 2, 3, 5, 7 etc. are prime numbers as they do not have any other factors. But 6 is not prime (it is composite) since, 2 x 3 = 6


num = int(input("Enter number to display which are prime in your list:"))

for num in range(0,num):
    if num>1:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
            print(num)
