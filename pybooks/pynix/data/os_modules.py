#listing import of os modules.
import os

#list operations on files and directories
os.getpwd() # print the current working directoy
os.mkdir() # create new directory in current path
os.listdir() # list files in current directory
os.stat() # get stats of file or directory
os.rename() # rename directory
os.rmdir() # remove directory

# Copying, Moving, Renaming, deleteing data
os.chdir("/tmp") # change dir
os.makedirs("/tmp/test1/test2") # create multiple dirs ~ mkdir -p

import shutil
shutil.copytree("test", "test-copy") # copy multiple recursive ~ cp -Rv
shutil.move("test-copy","test-copy-moved") # move directory
shutil.rmtree("test-copy-moved") # Remove directory
