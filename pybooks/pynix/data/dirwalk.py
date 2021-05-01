import os
path="/tmp"

def getAbsoluteFilePaths(path=path):
    # get absolute file names in directory
    dir_collections=[]
    for dirpath,dirnames,filename in os.walk(path):
        for file in filename:
            fullpath=os.path.join(dirpath,file)
            dir_collections.append(fullpath)
    return dir_collections

def getFilesFileNamesInDirectory(path=path):
    files_collections=[]
    for dirpath,dirname,filenames in os.walk(path):
        for eachfile in filenames:
            files_collections.append(eachfile)
    return files_collections

def getDirectoriesInDiectory(path=path):
    directory_collections=[]
    for dirpath,dirname,filenames in os.walk(path):
        for eachdir in dirname:
            directory_collections.append(eachdir)
    return directory_collections

if __name__=="__main__":
    print("File Full paths: ")
    for filefullpaths in getAbsoluteFilePaths():
        print(filefullpaths)

    print("\n")
    print("List of file names: ")
    for filename in getFilesFileNamesInDirectory():
        print(filename)

    print("\n")
    print("List of directories in {} directory: ".format(path))
    for dirname in getDirectoriesInDiectory():
        print(dirname)
