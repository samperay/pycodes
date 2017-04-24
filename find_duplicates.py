"""Finding duplicate files in a directory

This program will receive a folder or list of folders
to scan, which is going to traverse the directories given
and find the duplicated files in folder

"""
import os, sys
import hashlib


def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirname, subdirs, filenames in os.walk(parentFolder):
        print('Scanning %s...' % dirname)
        for eachfile in filenames:
            # Get complete path of each file
            path = os.path.join(dirname, eachfile)
            # Calculate hash value of the file
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups


# Joins two dictionaries
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


def hashfile(path, blocksize=65536):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('The following files are identical. The name could differ, but the content is identical')
        print('___________________')
        for result in results:
            for subresult in result:
                print('%s' % subresult)
            print('___________________')
    else:
        print('No duplicate files found.')


if __name__ == '__main__':
        dups = {}
        readdir= input("Enter directory or multiple directory using comma(,): ")
        folders = readdir.split(',')
        #folders = sys.argv[1:]
        for folder in folders:
            # check if the directory exists and if so iterate the folders
            if os.path.isdir(folder):
                # Find the duplicated files and append them to the dups
                joinDicts(dups, findDup(folder))
            else:
                print('Invalid Folder:%s' %folder)
                sys.exit()
            printResults(dups)
