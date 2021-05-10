# For a given string input, make lists for digits and leters:
a="2001: A Space Odyssey"
digit=[]
alpha=[]

for char in a:
    if char.isdigit():
        digit.append(char)
    elif char.isalpha():
        alpha.append(char)
    else:
        pass
print("Digit", digit)
print("Alpha", alpha)
