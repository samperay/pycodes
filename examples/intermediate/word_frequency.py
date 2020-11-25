# Find out the frequency of the word in a sentence using dictionary

ss = """Nory was a Catholic because her mother was a Catholic, 
and Nory's mother was a Catholic because her father was a Catholic, 
and her father was a Catholic because his mother was a Catholic, 
or had been."""

from collections import defaultdict

# initilize the default dictionary
d=defaultdict(int)

for word in ss.split():
    d[word]+=1

print("word frequency = ",dict(d))
