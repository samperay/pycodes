#!/usr/bin/python
import os
import shutil


class FileOps:
    """
    file operations:

    listFiles: list files in the path specified
    listDirectory: list all the directories in path specified
    createDirectory: Create a directory in the path specified
    copyDirectory: Copy directory
    renameDirectory: Rename directory
    deleteDirectory: Delete directory
    """
    # Defaults to users home directory
    def __init__(self):
        path = os.path.expanduser("~")
        self.path = path

    # List the files in the current directory
    def listFiles(self,path):
        self.path = path
        listofallfiles = []
        for _,_,listoffiles in os.walk(self.path):
            for eachfile in listoffiles:
                listofallfiles.append(eachfile)
        return listofallfiles

    # List the directories in the present working directory
    def listDirectory(self, path):
        self.path = path
        listofalldirs = []
        for _,listofdirs,_ in os.walk(self.path):
            for eachdirectory in listofdirs:
                if eachdirectory.startswith("."):
                    continue
                else:
                    listofalldirs.append(eachdirectory)
        return listofalldirs

    # Verify directory exists
    def directoryExists(self, directory):
        self.directory = directory
        if os.path.isdir(self.directory):
            return True
        else:
            return False

    # Create Directory
    def createDirectory(self, directory):
        self.directory = directory
        try:
            os.makedirs(self.directory)
            return True
        except OSError as error:
            print(error)
            return False

    # Copy Directory
    def copyDirectory(self, directory, newdirectory):
        self.directory = directory
        self.newdirectory = newdirectory
        try:
            if shutil.copytree(self.directory, self.newdirectory):
                return True
        except OSError as error:
            print(error)
        return False

    # Rename Directory
    def renameDirectory(self, directory, newdirectory):
        self.directory = directory
        self.newdirectory = newdirectory
        try:
            if shutil.move(self.directory, self.newdirectory):
                return True
        except OSError as error:
            print(error)
        return False

    # Delete Directory
    def deleteDirectory(self, directory):
        self.directory = directory
        try:
            if os.rmdir(self.directory):
                return True
        except OSError as error:
            print(error)
        return False