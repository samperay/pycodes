# Convertions

# Convert list to strings
L=["Sunil","Kumar"]
print(" ".join(L))

# Convert list of integers
L1=list(range(10))
print(' '.join(str(n) for n in L1))

# Convert list to a dict
L2=["Welcome","to","India",1,2,3]
print(dict(zip(L2[:3],L2[3:])))
