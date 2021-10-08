# Python program to Reverse a single line of a text file

original_string = []
reverse_string = []

with open("single_line.txt") as fread:
    for line in fread.readlines():
        for each_word in line.split():
            original_string.append(each_word)

reverse_string = " ".join(original_string[::-1])
print("Reverse of the single line: ", reverse_string)

# Python program to reverse the content of a file and store it in another file

with open("line_reverse.txt", "w") as fd:
    fd.writelines(reverse_string)
print("written to the file in reverse..")