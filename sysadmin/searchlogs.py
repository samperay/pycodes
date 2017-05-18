from os import listdir
from os.path import isfile,join

# Create list of all files 


# By default, all the logs location on the Linux system would be 
# at /var/log and hence by default would chosse those ..

logpath = '/var/log/'

#Get input from user about what is being searched for 
re_string = input('Enter your search pattern:')

logfiles = [f for f in listdir(logpath) if isfile(join(logpath,f)) and f.endswith(".log")]

for file in logfiles:
    print("{}: \n-----------\n".format(file))
    with open(logpath+file,'r') as f:
        for line in f:
            if re_string in line:
                print(line)
