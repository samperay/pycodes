# convert list to tuple
print("Convertion from List to Tuple:",tuple(range(10)))


newlist=[1,2,3,4]
print("Convertion from List to Tuple:",tuple(newlist))

# convert list to a string
L = ["Imagination", "is", "more", "important", "than", "knowledge"]
string="".join(L)
print("Convert list to String: ",string)

# convert list of string
N=[1,2,3,4]
print("Convert Integer number to string: ","".join(str(n) for n in N))

# convert a list to dictionary
number = ['eins','zwei','drei',1,2,3]
newdict=dict((zip((number[:3]),(number[3:]))))
print("Convert list to dictionary:",newdict)
