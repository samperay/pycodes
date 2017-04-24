""" 
We would provide the path name and would ask to choose to display 
1. Both files and directories along with their relative paths
2. Only lists files in the path 
3. Only lists directories in the path 
"""

import os

def listpaths(path):
    """Returns complete path of all files and directories """
    pathcollect = []
    for dirpath, dirname, filename in os.walk(path):
        for file in filename:
            fullpath = os.path.join(dirpath,file)
            pathcollect.append(fullpath)

    return pathcollect

def listfiles(path):
    """Returns only the files in the path"""
    filecollect = []
    for dirpath, dirname, filename in os.walk(path):
        for file in filename:
            filecollect.append(file)

    return filecollect

def dirlist(path):
    """Returns only the directory files"""
    dircollect = []
    for dirpath, dirname, filename in os.walk(path):
        for dir in dirname:
            dircollect.append(dir)

    return dircollect

if __name__ == '__main__':
    paths = input("Enter path to display files & directories: ")
    if os.path.isdir(paths):
        print("1. Do you wish to list files,directory\n2. Do you wish to list only files ? \n3. Do you wish to list only directoroes ?")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("\nRelative path for files and directories")
            print("-----------------------------------")
            for path in listpaths(paths):
                print(path)
        elif choice =='2':
            print("\nListing only files")
            print("---------------------")
            for path in listfiles(paths):
                print(path)
        elif choice =='3':
            print("\nListing directories")
            print("------------------")
            for path in dirlist(paths):
                print(path)
        else:
            print("Invalid choice .. exiting ...")
            exit(1)
    else:
        print("No such path or directory .. exiting")



