# print fibonacci numbers

num = int(input("Enter number you want fibonacci numbers: "))

a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= num):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b

# Python Program for How to check if a given number is Fibonacci number?
# A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square











