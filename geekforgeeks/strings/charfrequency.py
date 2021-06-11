# Python – Least Frequent Character in String
from collections import defaultdict
string = "Words Frequency in String"
d = defaultdict(int)

for word in string.split():
    for char in word:
        d[char] += 1

print("Least frequency of words used in string: ")
for k, v in d.items():
    if v <= 1:
        print(k, ":", v)

# Python | Maximum frequency character in String

print("Maximum frequency of words used in string: ")
for k, v in d.items():
    if v >1 :
        print(k, ":", v)

