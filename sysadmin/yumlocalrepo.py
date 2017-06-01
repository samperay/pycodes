# This would mainly create an local yum repository.

# There were few of the checks being considered:
# - Check for Linux RPM based distributions
# - To be executed by root only
# - Verify ISO image being mounted
# - verify for the local repo directory created
# - verify there is enough space to copy contents from ISO to local directory
# - Backup all the repo files if already existing and create a local repository

import os
import shutil


def rpmDistro():
    """Only for RPM distributions"""

    import platform
    if (platform.system() == 'Linux') and (platform.dist()[0] == 'centos' or 'redhat'):
        return True
    else:
        return False


def rootExecute():
    """Check for effective user ID running this script.."""

    if os.geteuid() == 0:
        print("Info: root privileges continue..")
        return True
    else:
        print("Error: script requires root privileges to execute exiting..")
        exit(1)


def mountVerify():
    """Verify CD/DVD/ISO image already in the optical drive"""

    with open('/etc/mtab', 'r') as f:
        mounts = [line.split()[0] for line in f.readlines()]
        if '/dev/sr0' in mounts:
            print('Info: Optical drive mounted...')
            return True
        else:
            print("Info: Optical drive not mounted trying to mount...")
            if mountOptical() == True:
                print("Info: mounted successfully..")
                return True
            else:
                print("Error: Please insert DVD/ISO image and try again exiting")
                exit(1)


def mountOptical():
    """ Mounting optical drive"""

    os.system("sudo mount /dev/sr0 /media" + ">/dev/null 2>&1")

    # check mount was successful ..
    if os.path.ismount('/media'):
        return True
    else:
        return False


def validateDiskSapce():
    """ Check the directory space to copy data to created disk folder"""

    diskspace = os.statvfs('/var')
    diskspace_gb = (diskspace.f_bavail * diskspace.f_bsize) / 1024 / 1024 / 1024

    if diskspace_gb < 4.5:
        print('Error: No sufficient space available to copy contents exiting..')
        return False
    else:
        print("Info: There is enough space to copy packages to '/var/yumlocalrepo' ")
        return True


def copyData():
    """ Dump all the media contents to a local repository file"""

    src = '/media'
    dst = '/var/yumlocalrepo'
    if os.path.isdir(dst):
        shutil.rmtree(dst)

    print("Info: Copying data...")
    shutil.copytree(src, dst)
    print("Info: Copy completed")


def backupYumrepoFiles():
    """Take a backup copy for all the files inside '/etc/yum.repos.d' """

    sourcedir = '/etc/yum.repos.d'
    backupdir = '/etc/yum.repos.d/repobkp'

    try:
        os.mkdir(backupdir)
    except FileExistsError:
        print("Info: Backup directory already exists..")

    for files in os.listdir(sourcedir):
        if files.endswith("repo"):
            fullfilepath = os.path.join(sourcedir, files)
            shutil.move(fullfilepath, backupdir)
    print("Info: Backed up all '*.repo' files")


def writeLocalrepofile():
    """Write the definition of local repository file"""

    repofile = '/etc/yum.repos.d/localrepo.repo'
    try:

        with open(repofile, 'w') as fp:
            fp.write('[yumlocalrepo]\n')
            fp.write('Name=Local repository\n')
            fp.write('baseurl=file:///var/yumlocalrepo\n')
            fp.write('gpgcheck=0\n')
            fp.write('enabled=1')
        print("Info: Local repository file created..")
    except IOError:
        print("Error: Could not open file..")


def installdepspkg():
    """Before Repository creation few of the dependencies packages to be installed.."""

    os.system("rpm -ivh /var/yumlocalrepo/libxml2-python-*.rpm" + ">/dev/null 2>&1")
    os.system("rpm -ivh /var/yumlocalrepo/deltarpm-*.rpm" + ">/dev/null 2>&1")
    os.system("rpm -ivh /var/yumlocalrepo/python-deltarpm-*.rpm" + ">/dev/null 2>&1")
    os.system("rpm -ivh /var/yumlocalrepo/createrepo-*.rpm" + ">/dev/null 2>&1")
    print("Info: Dependent necessary packages have been installed successfully..")

    os.system("createrepo /var/yumlocalrepo" + ">/dev/null 2>&1")
    print("Info: Local repository created")


if __name__ == '__main__':
    # if rpmDistro() and rootExecute():
    if rpmDistro():
        print("Info: Linux RPM based distribution ")
    else:
        print("Error: Not Linux/RPM based distribution exiting ..")

    # check root is executing this script else exit here....
    rootExecute()

    if mountVerify() == True:
        validateDiskSapce()
        copyData()
        installdepspkg()
        backupYumrepoFiles()
        writeLocalrepofile()
