import os

path="E:\/"
filelist=[]
for root,dirname,filename in os.walk(path):
    for f in filename:
        filelist.append(f)
print(filelist)
