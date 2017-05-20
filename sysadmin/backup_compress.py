""" 
this would take a backup copy of all the contents on the /etc 
and would compress in the .gzip format 
"""

import os
import tarfile

# mention your path to have compressed zip image
source = "/tmp"

destination = "/tmp/"

# create a tar file and compress
tar = tarfile.open("{}".format(destination)+"temp.tar.gz","w|gz")

for root, dir, files in os.walk(source):
    for file in files:
        fullpath = os.path.join(root,file)
        tar.add(fullpath)

tar.close()

