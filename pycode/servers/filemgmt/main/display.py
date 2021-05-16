def displayMenu():
    """
    Display the menu for the user to enter choices
    """

    print("Enter choice: ")
    print("'1.' List Files ")
    print("'2.' List Directory ")
    print("--- Choose the file operations to be performed ---")
    print("'3.'  Create Directory ")
    print("'4.' Copy Directory ")
    print("'5.' Rename Directory ")
    print("'6.' Move Directory ")
    print("'7.' Delete Directory ")
    choice = int(input("Enter your choice: "))
    return choice

def displayListOfFilesInDirectory(listoffiles):
    """
    Display output for list of files and directories in the path
    """
    print("-" * 60)
    for eachfile in listoffiles:
        print(eachfile)
    print("-" * 60)

def displayFileOperations(choice,status):
    """
    Display list of file operations to be performed in the directory
    """
    if choice == 3:
        if status:
            print("Directory CREATE Operation Success !")
        else:
            print("Directory already exists, CREATE Failed !")
    elif choice == 4:
        if status:
            print("Directory COPY Operation Success !")
        else:
            print("Directory COPY Operation Failed !")
    elif choice == 5:
        if status:
            print("Directory RENAME Operation Success !")
        else:
            print("Directory RENAME Operation Failed !")
    elif choice == 6:
        if status:
            print("Directory MOVE Operation Success !")
        else:
            print("Directory MOVE Operation Failed !")
    elif choice == 7:
        if status == 0:
            print("Directory DELETE Operation Success !")
        else:
            print("Directory DELETE Operation Failed !")