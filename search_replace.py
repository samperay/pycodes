""" The script would be used to search a particular pattern and 
from the file are-write into same original file. 
We would append the original file with our required
contents to the file and close.
"""

import re
import fileinput
import time

curdate= time.strftime("%d%m%Y")
srcfilename = '/tmp/testfstab'
bkpfilename = '/tmp/testfstab.'+curdate
pattern='admin'
appendstr="testprd.com /mymount ext4 defaults 0 0"

# Deletes the line containing the pattern
for line in fileinput.input(srcfilename,backup='.'+curdate, inplace=True):
    if not re.search(pattern,line):
        print(line,end="")

#appends the file with your content to write
with open(srcfilename,'a') as myfile:
     myfile.write(appendstr)