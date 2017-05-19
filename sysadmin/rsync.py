""" rsync command used to synchronize two directories 
and once they are completed they would email to you..

"""

import subprocess
import sys
import time

# Define your source and the destination directories along with
# 'rsync' arguments

source = "/tmp/testdir1/"
destination = "/tmp/testdir2"
rsync = "rsync"
args = "-av"
cmd = "{0} {1} {2} {3}".format(rsync,args,source,destination)

#If we are trying to sync too large directories, it could
# sometimes process might die which it need again to start
# process.

# we could overcome by trying to sync directories until
# its completed and email once its synced.

def sync():
    while True:
        retry = subprocess.call(cmd, shell=True)
        if retry !=0:
            print("re-submitting job")
            time.sleep(30)
        else:
            proc1=subprocess.Popen("echo rsync was succesful ...",shell=True,stdout=subprocess.PIPE)
            proc2=subprocess.Popen("mail -s 'rsync successful' sunlnx@localhost.com",shell=True,stdin=proc1.stdout,stdout=subprocess.PIPE)
            sys.exit(0)
sync()