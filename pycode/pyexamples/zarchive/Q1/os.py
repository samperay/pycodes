import os


print("MyCurrentWorkingDirectory",os.getcwd())
print("My Base(root) Directory:",os.path.dirname('/E/mydir'))
print("My Current File:",os.path.basename('/E/mydir/testfile.py'))
f_path,f_file=os.path.split('/E/mydir/testfile.py')
print("path:",f_path)
print("Filename:",f_file)

# To combile complete path
complete_path = os.path.join(f_path,f_file)
print("Complete_path=",complete_path)
