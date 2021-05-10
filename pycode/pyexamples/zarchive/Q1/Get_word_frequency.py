ss = """I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time"""

# initialized the dictionary with 0 using fromkeys()

# first way
words = ss.split()
d = {}.fromkeys(words,0)
for i in words:
    d[i]+=1
print("Firstway: ",d)

# second way
d = {}
for w in ss.split():
    d[w]=d.get(w,0)+1
print(d)

# third method
from collections import defaultdict
d = defaultdict(int)
for w in ss.split():
    d[w] += 1
print(d)
