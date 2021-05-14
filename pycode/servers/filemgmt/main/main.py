#!/usr/bin/python
from pycode.servers.filemgmt.utils.fileutils import FileOps
import pycode.servers.filemgmt.main.display as display

def main():
    files = FileOps()
    choice = display.displayMenu()
    if choice == 1:
        filepath = input("Enter your path to list files: ")
        print("List of all the files in %s" %filepath)
        listofallfiles = files.listfiles(filepath)
        display.displayOutput(listofallfiles)
    elif choice == 2:
        dirpath = input("Enter your path to list directory: ")
        print("List of all the dirs in %s" % dirpath)
        listofalldirectory = files.listdirectory(dirpath)
        display.displayOutput(listofalldirectory)
    else:
        print("Invalid Choice, exiting")
        exit(1)

if __name__ == '__main__':
    main()
