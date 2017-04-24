""" 
Compare two files are similar or not using MD5 digest 
and values returning from their checksum.

reads the file creates checksum of file line by line and then
returns complete checksum total for file 
"""
import hashlib

def createchecksum(filename):
    fp = open(filename,'r')
    checksum = hashlib.md5()
    while True:
        buffer = fp.read(8192)
        if not buffer:break
        checksum.update(str(buffer).encode())
    fp.close()
    checksum = checksum.digest()
    return checksum

if __name__ == '__main__':
    file1 = input("Enter first file: ")
    file2 = input("Enter second file: ")
    if createchecksum(file1) == createchecksum(file2):
        print("Similar files")
    else:
        print("Different file")