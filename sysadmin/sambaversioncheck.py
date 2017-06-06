# This script would find out :
    # - samba installed 
    # - samba service running
        # - if running, print major and minor number

import os
import subprocess
import platform

if platform.system() == 'Linux':
    #check if samba is installed
    if os.path.isfile('/usr/sbin/smbd'):
        # if samba, then check if its running
        allprocess=os.popen("ps -Af").read()
        processcount = allprocess.count('smbd')
        # if smbd daemon running, then find the version
        if processcount >0:
            p = subprocess.Popen("/usr/sbin/smbd -V", stdout=subprocess.PIPE,shell=True)
            (output,err) = p.communicate()
            pkgversion = (output[8::]).split('.')
            pkgmajorversion = int(pkgversion[0])
            pkgminorversion = int(pkgversion[1])
            
            print(pkgmajorversion)
            print(pkgminorversion)
        else:
            print("Info: smb service not running")
    else:
        print("Info: samba package not installed")
else:
    print("Info: Not an Linux OS")