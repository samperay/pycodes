# this would append the parameter in the config file if
# the entry don't exist.

# if the entry already in the config file it would just exit

configfile='/etc/httpd/conf/httpd.conf'
param ='ServerName www.fedora.com:80'

def skipComments(file):
    """generator which would skip all blank lines and '#' char"""
    for line in file:
        if not line.strip().startswith('#'):
            yield line

def paramExists():
    """check if the defined parameter exists from non-commented files in the config file"""
    with open(configfile,'r') as fp:
        for line in skipComments(fp):
            paramcount=line.count(param)

        if paramcount != 0:
            return True
        else:
            return False

def changeConfigFile():
    """
    On successful return from the paramExists required to write change to the 
    config file """

    with open(configfile,'a') as fp:
        fp.write("\n"+param)
        print("Info:'{}' added to {}'".format(param,configfile))

def restartService():
    """ restart service once your config file changed"""
    import subprocess
    output = subprocess.call(["sudo systemctl restart httpd.service"],shell=True)
    if output == 0:
        print('Info: service restart successful')
    else:
        print('Info: service restart failed')

if __name__ == '__main__':

    retval = paramExists()
    if retval == True:
        print("Info:'{}' already exists in '{}'".format(param, configfile))
    else:
        changeConfigFile()
    restartService()


