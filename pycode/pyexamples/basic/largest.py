# Given the three integer values find out the largest, second largest and the smallest.
# These values to be provided dynamicall from the the system
import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])

# Find the largest, second largest
if a>b:
    l=a
    sl=b
else:
    l=b
    sl=a

# Compare between largest and the third vars
if c>l:
    s=sl
    sl=l
    l=c
elif l>c:
    l=l
    sl=b
    s=c

print("Largest:", l)
print("Second Largest:", sl)
print("Smallest:", s)
