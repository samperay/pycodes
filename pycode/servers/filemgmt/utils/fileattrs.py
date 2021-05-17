#!/usr/bin/python

# Module to display file attribute
import os
import pwd
import grp

class FileAttributes:
    """
    Display File attributes
    """

    def getOwnerNameOfFile(self, filename):
        self.filename = filename
        file_uid = os.stat(self.filename).st_uid
        file_uid_name = pwd.getpwuid(file_uid).pw_name
        return file_uid_name

    def getGroupNameOfFile(self, filename):
        self.filename = filename
        file_gid = os.stat(self.filename).st_gid
        file_gid_name = grp.getgrgid(file_gid).gr_name
        return file_gid_name




