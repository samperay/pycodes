import os

class OsWalk:
    def __init__(self,path):
        self.path = path

    def getAbsoluteFilePaths(self):
        # get absolute file names in directory
        dir_collections=[]
        for dirpath,dirnames,filename in os.walk(self.path):
            for file in filename:
                fullpath=os.path.join(dirpath,file)
                dir_collections.append(fullpath)
        return dir_collections

    def getFilesFileNamesInDirectory(self):
        files_collections=[]
        for dirpath,dirname,filenames in os.walk(self.path):
            for eachfile in filenames:
                files_collections.append(eachfile)
        return files_collections

    def getDirectoriesInDiectory(self):
        directory_collections=[]
        for dirpath,dirname,filenames in os.walk(self.path):
            for eachdir in dirname:
                directory_collections.append(eachdir)
        return directory_collections

if __name__=="__main__":
    tmp_path=OsWalk("/tmp")

    print("File Full paths: ")
    for filefullpaths in tmp_path.getAbsoluteFilePaths():
        print(filefullpaths)

    print("\n")
    print("List of file names: ")
    for filename in tmp_path.getFilesFileNamesInDirectory():
        print(filename)

    print("\n")
    print("List of directories in {} directory: ".format(path))
    for dirname in tmp_path.getDirectoriesInDiectory():
        print(dirname)
