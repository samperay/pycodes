# this would append the parameter in the config file if
# the entry don't exist.

# if the entry already in the config file it would just exit

configfile = '/tmp/smb.conf'
param = 'name=value'

def verifyParameter():
    try:
        with open(configfile,'r') as fp:
                if param in fp.read():
                    print("Info:'{}' already exists in '{}'".format(param, configfile))
                    return 1
                else:
                    return 0
    except FileNotFoundError as err:
        print(err)
        return 0

def writeParameter():
        with open(configfile,'a') as fp:
            fp.write("\n"+param)
            print("Info:'{}' added to {}'".format(param,configfile))
            return 1

# def restartService():
#     import subprocess
#     output = subprocess.call(["sudo systemctl restart httpd.service"],shell=True)
#     if output == 0:
#         print('service restart successful')
#     else:
#         print('service restart failed')

if __name__ == '__main__':
    if verifyParameter():
        # entry already in config file.. exting from prog
        exit(0)
        # check file exists if so append entry
    elif writeParameter():
        print("True")
        #restartService()


