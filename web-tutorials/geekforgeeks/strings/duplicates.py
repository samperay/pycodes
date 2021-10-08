# Python | Check if a Substring is Present in a Given String

string = "Sunil Kumar Amperayani"
substr = "Sunilsss"

for word in string.split("\n"):
    if substr in word:
        print("Substring present in the string")
    else:
        print("Substring not found in string")