""" This script used to remove the **only files which are older 
than N days.. you are required to use this program with 
caution.

"""



from path import path
import time

# Days which you need to remove files ...

DAYS = 90
rm_count = 0

# You could replace with your directory
dir_path = path("/tmp/testdir")

# convert days in seconds and subtract from actual time
DAYS_IN_SEC = DAYS * 24 * 60 * 60

time_in_sec = time.time() - DAYS_IN_SEC

#we could log all deleted files

with open("/var/tmp/delete_files_.txt",'w') as fd:

    for file in dir_path.walk():
        if file.isfile():
            if file.mtime <= time_in_sec:
                fd.write(file + '\n')
                file.remove()
                rm_count+=1

print("Total files older than {0} days: {1}".format(DAYS,rm_count))
