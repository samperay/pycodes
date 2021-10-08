# Python program to copy odd lines of one file to other

current_file = "lines.txt"
new_file = "newfile.txt"

with open(current_file,"r") as fread:
    with open(new_file,"w") as fwrite:
        fwrite.writelines(fread)
print("Copied file from old to new")

appendlines = "\nthis is the last line to append to the file\n"

with open(new_file,'a') as fappend:
    fappend.writelines(appendlines)
print("Appended the lines to the files")
