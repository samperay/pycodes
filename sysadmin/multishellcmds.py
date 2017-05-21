import subprocess

def multiplecmds(*args):
    for cmd in args:
        p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        output=p.stdout.read()
        print(output)

multiplecmds("df -h","ls -l /tmp")
