s="server"

#first method
print(s[::-1])

# recursive function
def reverse(input):
    print(input)
    if len(input)-1 < 1:
        return input
    return reverse(input[1:])+input[0]
print(reverse(s))

# iteravative function
def rev(input):
    return ''.join([input[i] for i in range(len(input)-1,-1,-1)])
sr='mycomputer'
print(rev(sr))

# condiftional expr(ternary opr)
expected = 1
returned = 0
result = 'pass' if expected == returned else 'fail'
print(result)
