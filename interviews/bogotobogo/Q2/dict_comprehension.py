# List comp
L = [l for l in range(10) if l%2 == 0 ]
print("List Comphrension, list of all even numbers: ",L )

# Dict comp
D = {k:k**2 for k in L}
print("Dict Comphrension",D)

total_sum = sum(range(100))
print("Total Sum of numbers",total_sum)

even_sum = sum(i for i in range(100) if i%2 ==0 )
print("Even Sum",even_sum)

odd_sum = sum(i for i in range(100) if i%2 !=0 )
print("Odd Sum",odd_sum)
