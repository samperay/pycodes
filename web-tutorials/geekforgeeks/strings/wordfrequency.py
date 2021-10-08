# Python – Words Frequency in String Shorthands

from collections import defaultdict
string = "Words Frequency in String in"
d = defaultdict(int)

for word in string.split():
    d[word] += 1

print("word frequency: ", dict(d))
