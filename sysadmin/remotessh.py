import subprocess
import configparser

""" 
We use SSH for command to execute in remote machines 
"""

def readConfigFile(file="config.ini"):
    """ Extract IP address and Command form config file and returns tuple """
    ips = []
    cmds = [] 
    Config = configparser.ConfigParser()
    Config.read(file)
    machines = Config.items("MACHINES")
    commands = Config.items("COMMANDS")
    for  ip in machines:
        ips.append(ip[1])
    for cmd in commands:
        cmds.append(cmd[1])
    return ips,cmds

ips,cmds = readConfigFile()

for ip in ips:
    for cmd in cmds:
        subprocess.call("ssh -q -o StrictHostkeychecking=no root@{} {}".format(ip,cmd),shell=True)
