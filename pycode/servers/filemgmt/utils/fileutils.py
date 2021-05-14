#!/usr/bin/python
import os
class FileOps:
    """
    file operations:

    listfiles: list files in the path specified
    listdirectory: list all the directories in path specified
    """
    # Defaults to users home directory
    def __init__(self):
        path = os.path.expanduser("~")
        self.path = path

    def listfiles(self,path):
        self.path = path
        listofallfiles = []
        for _,_,listoffiles in os.walk(self.path):
            for eachfile in listoffiles:
                listofallfiles.append(eachfile)
        return listofallfiles

    def listdirectory(self,path):
        self.path = path
        listofalldirs = []
        for _,listofdirs,_ in os.walk(self.path):
            for eachdirectory in listofdirs:
                if eachdirectory.startswith("."):
                    continue
                else:
                    listofalldirs.append(eachdirectory)
        return listofalldirs
