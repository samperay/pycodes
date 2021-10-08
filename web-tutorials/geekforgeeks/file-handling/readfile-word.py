# Python program to read file word by word

count = 0
with open('lines.txt') as fd:
    for line in fd.readlines():
        count += 1
        eachwords = line.split()
        print(eachwords)

# Count number of lines in a text file in Python
print("Total number of lines: ", count)