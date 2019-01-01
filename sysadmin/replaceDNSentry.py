""" Change your DNS entry from one IP to another using this simple script
You need to define your existing IP and put your 'Replacement IP'
"""

def searchReplace(filename,search,replace):
    """ Search the ip address and replace in files"""

    with open(filename) as file:
        filedata = file.read()

    filedata = filedata.replace(search,replace)

    with open(filename,'w') as file:
        file.write(filedata)

if __name__ == '__main__':
    """ Program starts from here """

    # Define your /etc/resolv.conf
    filename = './etc/res____.conf'

    # Pass your file , Existing IP, replacement IP
    searchReplace(filename,'206.223.27.2','20.2.2.2')
    searchReplace(filename,'206.223.27.1','192.168.122.2')