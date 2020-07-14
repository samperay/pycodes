try:
    with open('README.mdd','r') as f:
        print(f.read())
except IOError:
    print("Error: No such file or directory, Existing")
