"""
This script will check if the entry exists in the pam.d config file and will write the entry if for 
locking wrong password attempts. 

The entry to be added are in two of the files 
1. /etc/pam.d/system-auth
2. /etc/pam.d/password-auth

In both files, it requires an entry 
- auth        required      pam_tally2.so file=/var/log/tallylog deny=10 unlock_time=1800
- account     required      pam_tally2.so

"""

import os
import platform
import datetime
import fileinput

class ConfigChanges:
    """Modify Configuration Changes"""
    hostname = platform.node()
    version = platform.system()

    def __init__(self):
        """ Initilizing Config Files"""
        self.system_auth = "system-auth"
        self.password_auth = "password-auth"
        self.system_auth_original = "system-auth.original"
        self.password_auth_original = "password-auth.original"
        self.multiple_sysauth_runs = "system-auth."+str(datetime.date.today())
        self.multiple_passwd_runs = "password-auth."+str(datetime.date.today())
        self.add_string_1 = 'auth        required      pam_tally2.so file=/var/log/tallylog deny=10 unlock_time=1800\n'
        self.add_string_2 = 'account     required      pam_tally2.so\n'

    def printConfigChanges(self):
        print(self.hostname)

    def configurationBackup(self):
        """ Take configuration backup """
        import shutil
        if os.path.isfile(self.system_auth_original) or os.path.isfile(self.password_auth_original):
            shutil.copyfile(self.system_auth,self.multiple_sysauth_runs)
            shutil.copyfile(self.password_auth,self.multiple_passwd_runs)
        else:
            shutil.copyfile(self.system_auth,self.system_auth_original)
            shutil.copyfile(self.password_auth,self.password_auth_original)

    def verifyIfEntryAlreadyExists(self,string,entry):
        """verify if parameter already exists """
        self.string=string
        self.entry = entry

        alllines = []
        alllines = open(string,'r').readlines()

        if alllines.count(self.entry) == 0:
            return False
        else:
            return True

    def writeConfigChange(self,configfile,addentry,matchword):
        """ Writing to Config Change"""
        self.configfile = configfile
        self.addentry = addentry
        self.matchword = matchword

        found = False
        for line in fileinput.input(self.configfile,inplace=True):
            if not found and line.startswith(self.matchword):
                print(addentry,end='')
                found=True
            print(line,end='')


if __name__ == '__main__':
    filechanges=ConfigChanges()

    if filechanges.version == 'Linux':
        filechanges.configurationBackup()

        if filechanges.verifyIfEntryAlreadyExists(filechanges.system_auth,filechanges.add_string_1) == False:
            filechanges.writeConfigChange(filechanges.system_auth,filechanges.add_string_1,'auth')

        if filechanges.verifyIfEntryAlreadyExists(filechanges.system_auth,filechanges.add_string_2) == False:
            filechanges.writeConfigChange(filechanges.system_auth,filechanges.add_string_2,'account')

        if filechanges.verifyIfEntryAlreadyExists(filechanges.password_auth,filechanges.add_string_1) == False:
            filechanges.writeConfigChange(filechanges.password_auth,filechanges.add_string_1,'auth')

        if filechanges.verifyIfEntryAlreadyExists(filechanges.password_auth,filechanges.add_string_2) == False:
            filechanges.writeConfigChange(filechanges.password_auth,filechanges.add_string_2,'account')
    else:
        print('Un-supported OS')




