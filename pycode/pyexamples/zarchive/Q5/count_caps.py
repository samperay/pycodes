string="abcdefgHIJKLMOPQrstuvwxyz"

count=0
for char in string:
    if char.isupper():
        count+=1
print("count total number of CAPS using string:",count)

# read from file to count CAPS
flinecount=0
with open("E:\projects\practice-python\interviews\/bogotobogo\Q5\input.txt","r") as fp:
    # you can write below 3 lines of code to get count
    # for line in fp.read():
    #     if line.isupper():
    #         flinecount+=1

    # Combile all the above 3 lines of code to a single code
    flinecount = len([line for line in fp.read() if line.isupper() ])
print("count total number of CAPS using filename",flinecount)
