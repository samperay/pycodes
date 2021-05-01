import oswalk

# if the path of oswalk.py are in some folder, let's assume os, then import statement would be different
# from os import oswalk
# code from the same as above could work easily

# Trying to import from the oswalk.py in same directory.
listtmppfiles=oswalk.OsWalk("/tmp")
print("File Full paths: ")
for filefullpaths in listtmpfiles.getAbsoluteFilePaths():
    print(filefullpaths)
