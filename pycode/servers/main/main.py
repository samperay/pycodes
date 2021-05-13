#!/usr/bin/python

from pycode.servers.utils.fileutils import FileOps


def main():
    files = FileOps()
    choice = input("Enter your choice: ")
    filepath = input("1. Enter your path to list files: ")
    dirpath = input("2. Enter your path to list directory: ")
    if choice == 1:
        files.listfiles(filepath)
    elif choice == 2:
        files.listdirectory(dirpath)
    else:
        print("Defaults to current home directory")


if __name__ == '__main__':
    main()
