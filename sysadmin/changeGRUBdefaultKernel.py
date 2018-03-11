# lists the kernel versions and enter to boot to your default kernels

import platform

def findDefaultGrubLevel():
    """Find out default grub entry"""
    with open('/boot/grub/grub.conf', 'r') as file:
        # filedata = file.read().replace('default=2','default='+str(choice))
        for line in file.readlines():
            if 'default' in line:
                currentdefaultgurb = line.split('=')[1]
                return  currentdefaultgurb

def changeGrubDefaultConfig(choice):
    """Pass the entry to change default booting config for the grub"""
    filedata = None

    defaultgrubentry=findDefaultGrubLevel()
    srcstring='default='+defaultgrubentry
    deststring='default='+choice+"\n"

    with open('/boot/grub/grub.conf','r') as file:
        filedata = file.read().replace(srcstring,deststring)

    with open('/boot/grub/grub.conf','w') as file1:
        file1.write(filedata)

def displayKernelsInstalled():
    """Print default kernels installed in system"""
    defaultkernelslist=[]
    count = 0
    with open('/boot/grub/grub.conf') as f:
        print("----" * 20)
        print('Default','|','Kernels available to boot')
        print("----" * 20)
        for line in f.readlines():
            if 'title' in line:
                print(count,"\t\t|", line.strip())
                count+=1
        print("----" * 20)
        #defaultkernelslist.append(count)

        for i in range(count):
            defaultkernelslist.append(i)

    choice = input('Enter your choice to boot kernel by default next time: ')
    if (int(choice) <= count):
        print('Choice entered',choice)
        if int(choice) in defaultkernelslist:
            changeGrubDefaultConfig(choice)
    else:
        print('No such grub entry found')

if __name__ == '__main__':
    if platform.platform().split('-')[6][0] == '6':
        print('Current your GRUB default entry:', findDefaultGrubLevel())
        displayKernelsInstalled()
    else:
        print('Not supported')





