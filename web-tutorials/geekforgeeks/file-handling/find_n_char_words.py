# Python | Finding ‘n’ Character Words in a Text File

n = 5

with open("words.txt") as f:
    for line in f.readlines():
        for word in line.split("\n"):
            if len(word) == 5:
                print(word)
