# Given the list, output the list of frequency of digits
# Initialize the dictionary with list

L = [1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296]

from collections import defaultdict
d=defaultdict(list)

for w in L:
    d[len(str(w))].append(w)

print(dict(d))
