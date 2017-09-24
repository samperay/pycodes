# This script would append an entry at the end of the config file and ensures that
# there exists only one entry.
# script works fine on CentOS/Redhat/Solaris.

import os
import platform
import shutil
import datetime
import re

entry1 ='local1.info;local5.info;auth.debug;authpriv.* @192.168.10.111:514\n'
entry2 ='local1.info;local5.info;auth.debug;authpriv.* @192.168.10.112:514\n'

rsyslogfile='/etc/rsyslog.conf'
rsyslogmasterbackup='/etc/rsyslog.conf.original'
rsyslogdupcopy='/etc/rsyslog.conf-'+str(datetime.date.today())

sylogfile='/etc/syslog.conf'
syslogmasterbackup='/etc/syslog.conf.original'
syslogdupcopy='/etc/syslog.conf-'+str(datetime.date.today())


def skipCommentsConfigFile(file):
    """ generator which would skip all blank lines and '#' char """
    for line in file:
        if not line.strip().startswith('#'):
            yield line

def findMajorversion():
    """Determine the major version """
    if platform.system() == 'Linux':
        infile = open('/etc/redhat-release','r')
        lines = infile.read()
        version = re.findall(r'\d+',lines)
        infile.close()
        return version[0]
    elif platform.system() == 'SunOS':
        infile = open('/etc/release','r')
        lines = infile.read()
        version = re.findall(r'\d+',lines)
        infile.close()
        return version[0]

def restartService():
    """ restart service once your config file changed """
    import subprocess

    if platform.system() == 'Linux':
        majorversion = findMajorversion()
        fnull = open(os.devnull,'w')
        if (majorversion == '5') or (majorversion == '2') or (majorversion == '3'):
            output = subprocess.call('/sbin/service syslog restart',shell=True,stdout=fnull)
        elif ( majorversion == '6' ):
            output = subprocess.call('/sbin/service rsyslog restart',shell=True, stdout=fnull)
        elif (majorversion == '7' ):
            output = subprocess.call('/bin/systemctl restart rsyslog.service',shell=True,stdout=fnull)
        fnull.close()

        if output == 0:
            print platform.node().strip()+";"+platform.system().strip()+';success;entry_added;service_restart_ok'
        else:
            print platform.node().strip()+";"+platform.system().strip()+';failed;entry_added;service_restart_notok'
    elif platform.system()=='SunOS':
        majorversion=findMajorversion()
        fnull = open(os.devnull, 'w')
        if (majorversion == '8' ) or (majorversion == '9' ):
            output=subprocess.call('/etc/init.d/syslog stop && /etc/init.d/syslog start',shell=True,stdout=fnull)
        else:
            output=subprocess.call('/usr/sbin/svcadm restart system/system-log:default',shell=True, stdout=fnull)
        fnull.close()

        if output == 0:
            print platform.node().strip()+";"+platform.system().strip()+';success;entry_added;service_restart_ok'
        else:
            print platform.node().strip()+";"+platform.system().strip()+';failed;entry_added;service_restart_notok'

def verifyParameterExists(configfile):
    """check if the defined parameter exists from non-commented files in the config file """

    oldentryfound=0
    newentryfound=0
    alllines=[]

    fp = open(configfile,'r')
    for line in skipCommentsConfigFile(fp):
        alllines.append(line)
    fp.close()

    for item in alllines:
        if entry1 in item:
            oldentryfound = 1

    for item1 in alllines:
        if entry2 in item1:
            newentryfound=1

    if (oldentryfound == 0) and (newentryfound == 0):
        return 'WriteBothEntries'
    elif oldentryfound == 0:
        return 'WriteOldEntry'
    elif newentryfound == 0:
        return 'WriteNewEntry'
    else:
        return True

def writeConfigFile(firstentry,secondentry,configfile):
    """ On successful return from the paramExists required to write change to the config file
    once after backup your config file"""
    if (platform.system() == 'Linux') and ( findMajorversion() == '6' or findMajorversion() == '7' ):
        makeBackupCopy(configfile,rsyslogmasterbackup,rsyslogdupcopy)
    elif (platform.system() == 'SunOS') or ((platform.system()=='Linux') and (findMajorversion() == '5' or  findMajorversion() == '3' or  findMajorversion() == '2')):
        makeBackupCopy(configfile,syslogmasterbackup,syslogdupcopy)

    outfile = open(configfile,'a')
    outfile.write(firstentry)
    outfile.write(secondentry)
    outfile.close()

    # once you write your config file call restart definition
    restartService()

def makeBackupCopy(configfile,masterbackupcopy,duplicatecopy):
    """checks if there is master backup and if it exists then take afresh
    copy else take master backup copy"""

    if os.path.isfile(masterbackupcopy):
        shutil.copy(configfile,duplicatecopy)
    else:
        shutil.copy(configfile,masterbackupcopy)

def main():
    """Start of the program"""
    if (platform.system() == 'Linux') and (findMajorversion() == '6' or findMajorversion() == '7' ):
        retval = verifyParameterExists(rsyslogfile)
        if retval == 'WriteBothEntries':
            writeConfigFile(entry1,entry2,rsyslogfile)
        elif retval == 'WriteOldEntry':
            writeConfigFile(entry1,'',rsyslogfile)
        elif retval == 'WriteNewEntry':
            writeConfigFile(entry2,'',rsyslogfile)
        else:
            print platform.node().strip()+';'+platform.system().strip()+';success;entry_already_exists'
    elif platform.system()== 'SunOS' or ((platform.system()=='Linux') and (findMajorversion() == '5' or  findMajorversion() == '3' or  findMajorversion() == '2')):
        retval = verifyParameterExists(sylogfile)
        if retval == 'WriteBothEntries':
            writeConfigFile(entry1,entry2,sylogfile)
        elif retval == 'WriteOldEntry':
            writeConfigFile(entry1,'',sylogfile)
        elif retval == 'WriteNewEntry':
            writeConfigFile(entry2,'',sylogfile)
        else:
            print platform.node().strip()+';'+platform.system().strip()+';success;entry_already_exists'

if __name__ == '__main__':
    main()