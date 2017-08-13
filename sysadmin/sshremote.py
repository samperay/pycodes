""" this would copy files from the remote machine to local machine """

import paramiko
from scp import SCPClient



def createSSHClient(server, port, user,sshkey):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, sshkey)
    return client


def copyRemoteToLocal(hostlist,port,user,sshkey):
    for server in hostlist:
        ssh=createSSHClient(server,port,user,sshkey)
        scp = SCPClient(ssh.get_transport())
        scp.get('/home/sunlnx/rhelbaseimg','/tmp/')

def main():
    """Define all tha parameters in the main function"""
    hostlist = ['192.168.122.14']
    port = 22
    user = 'sunlnx'
    sshkeyfile = '/home/sunlnx/.ssh/id_rsa.pub'
    copyRemoteToLocal(hostlist, port, user,sshkeyfile)

if __name__ == '__main__':
    main()
    