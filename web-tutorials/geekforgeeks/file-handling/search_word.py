# Python Program to obtain the line number in which given word is present

word_to_search = "line1"
count = 0

with open("lines.txt") as fd:
    for line in fd.readlines():
        count += 1
        if word_to_search in line.split():
            print("string "+ word_to_search +" found in line: ", count)
        else:
            print("No matching string found")