# This script would revert the entry on the mail config file only if the file has a backup.
# script works fine on CentOS/Redhat/Solaris.

import os
import platform
import shutil
import re

rsyslogfile='/etc/rsyslog.conf'
rsyslogmasterbackup='/etc/rsyslog.conf.original'

syslogfile='/etc/syslog.conf'
syslogmasterbackup='/etc/syslog.conf.original'

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
        if ( majorversion == '5' ) or ( majorversion == '2' ) or ( majorversion == '3' ):
            output = subprocess.call('/sbin/service syslog restart',shell=True,stdout=fnull)
        elif ( majorversion == '6'):
            output = subprocess.call('/sbin/service rsyslog restart',shell=True, stdout=fnull)
        elif (majorversion == '7'):
            output = subprocess.call('/bin/systemctl restart rsyslog.service',shell=True,stdout=fnull)
        fnull.close()

        if output == 0:
            print platform.node().strip()+";"+platform.system().strip()+';success;reverted;service_restart_ok'
        else:
            print platform.node().strip()+";"+platform.system().strip()+';failed;reverted;service_restart_notok'
    elif platform.system()=='SunOS':
        majorversion=findMajorversion()
        fnull = open(os.devnull, 'w')
        if (majorversion == '8' ) or (majorversion == '9' ):
            output=subprocess.call('/etc/init.d/syslog stop && /etc/init.d/syslog start',shell=True,stdout=fnull)
        else:
            output=subprocess.call('/usr/sbin/svcadm restart system/system-log:default',shell=True,stdout=fnull)
        fnull.close()

        if output == 0:
            print platform.node().strip()+";"+platform.system().strip()+';success;reverted;service_restart_ok'
        else:
            print platform.node().strip()+";"+platform.system().strip()+';failed;reverted;service_restart_notok'


def revertConfig():
    """revert the configuration file from original"""
    if (platform.system()=='Linux') and (findMajorversion() == '6' or findMajorversion() == '7' ):
        if os.path.isfile(rsyslogmasterbackup):
            shutil.copy2(rsyslogmasterbackup,rsyslogfile)
            restartService()
        else:
            platform.node().strip()+';'+platform.system().strip()+';failed;backupfile_not_found'
    elif (platform.system()=='SunOS') or ((platform.system()=='Linux') and (findMajorversion() == '5' or  findMajorversion() == '3' or  findMajorversion() == '2')):
        if os.path.isfile(syslogmasterbackup):
            shutil.copy2(syslogmasterbackup,syslogfile)
            restartService()
        else:
            platform.node().strip()+';'+platform.system().strip()+';failed;backupfile_not_found'

if __name__ == '__main__':
    revertConfig()