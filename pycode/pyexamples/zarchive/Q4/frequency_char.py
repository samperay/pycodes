ss = "Mississippi borders Tennessee."

d={}
for word in ss.split():
    d[word]=d.get(word,0)+1
print("Word frequency", d)
