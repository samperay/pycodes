#!/usr/bin/python
import os.path
from pycode.servers.filemgmt.utils.fileutils import FileOps
import pycode.servers.filemgmt.main.display as display

def main():
    files = FileOps()

    choice = display.displayMenu()
    if choice == 1:
        filepath = input("Enter your path to list files: ")
        print("List of all the files in %s" %filepath)
        listofallfiles = files.listFiles(filepath)
        display.displayListOfFilesInDirectory(listofallfiles)
    elif choice == 2:
        dirpath = input("Enter your path to list directory: ")
        print("List of all the dirs in %s" % dirpath)
        listofalldirectory = files.listDirectory(dirpath)
        display.displayListOfFilesInDirectory(listofalldirectory)
    elif choice == 3:
        parentdirectory = input("Enter your path for which directory has to be created: ")
        directoryname  = input("Enter name of the directory to be created in current path: ")
        createdir = os.path.join(parentdirectory, directoryname)
        status = files.createDirectory(createdir)
        display.displayFileOperations(choice, status)
    elif choice == 4:
        srcdirectory = input("source directory: ")
        dstdirectory = input("destination directory to be copied: ")
        status = files.copyDirectory(srcdirectory, dstdirectory)
        display.displayFileOperations(choice, status)
    elif choice == 5:
        srcdirectory = input("source directory: ")
        dstdirectory = input("Enter the destination directory to : ")
        status = files.renameDirectory(srcdirectory, dstdirectory)
        display.displayFileOperations(choice, status)
    elif choice == 6:
        srcdirectory = input("directory to be deleted: ")
        status = files.deleteDirectory(srcdirectory)
        display.displayFileOperations(choice,status)
    else:
        print("Invalid Choice, exiting")
        exit(1)

if __name__ == '__main__':
    main()
