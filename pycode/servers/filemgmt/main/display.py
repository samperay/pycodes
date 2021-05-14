def displayMenu():
    """
    Display the menu for the user to enter choices
    """

    print("Enter choice: ")
    print("Enter '1' to list files")
    print("Enter '2' to list directory")
    choice = int(input("Enter your choice: "))
    return choice

def displayOutput(listoffiles):
    """
    Display output
    """
    print("-" * 40)
    for eachfile in listoffiles:
        print(eachfile)
    print("-" * 40)

