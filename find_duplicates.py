"""Finding duplicate files in a directory

This program would take a directory as a input and will create 
a dictionary of hash value of files with their paths as a value.
Join two dictionaries and check for duplicates and print result.

"""
import os,sys
import hashlib

def findDup(mainfolder):
    """ Create a dictionary and add key as hash value and value with
    filename. if hash key append to dictionary or if no entry add."""
    dups = {}
    for dirname, subdirs, filenames in os.walk(mainfolder):
        print('checking  %s directory ...' %dirname)
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

def joinDicts(dict1, dict2):
    """ Join two dictionaries as together"""
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]

def hashfile(path, blocksize=65536):
    """ Create a hash value of each file and return"""
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.hexdigest()

def printResults(dict1):
    """ Prints the results for duplicates """
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('\nDuplicates Found.. names could differ but content identical ..')
        for result in results:
            for subresult in result:
                print('%s' % subresult)
    else:
        print('No duplicate files found.')

if __name__ == '__main__':
        dups = {}
        folders= input("Enter directory to find out duplicates: ")
        # check if the directory exists and if so iterate the folders
        if os.path.isdir(folders):
        # Find the duplicated files and append them to the dups
            joinDicts(dups, findDup(folders))
        else:
            print('Invalid Folder:%s' %folders)
            sys.exit()
        printResults(dups)
