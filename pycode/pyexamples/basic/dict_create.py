# Create a dict
d=dict((k,k**2) for k in range(10))
print("Method-1",d)

d1={k:k**2 for k in range(10)}
print("Method-2",d1)

# create dictionamry of even squares
even={k:k**2 for k in range(10) if k%2==0}
print("Dict of Even Squares: ",even)

# you can create similar list of cube squares.
