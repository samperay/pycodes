# Class ServerInventory
# abstractions:  display servers, add servers to inventory list, delete servers from inventory

# class ServerAdmins
# abstractions: get server details, add server details, update server info

class ServerInventory:

    def __init__(self, listOfAllServers):
        self.availableservers = listOfAllServers

    def displayServerInventory(self):
        print("Listing all servers: ")
        for eachserver in self.availableservers:
            print(eachserver)

    def searchServerInventory(self,servername):
        if servername in self.availableservers:
            print("server exists in inventory")
        else:
            print("server does not exists in inventory")

    def addServerToInventory(self,servername):
        self.availableservers.append(servername)
        print("Server added to inventory")

    def removeServerFromInventory(self,server):
        self.availableservers.remove(server)
        print("Server removed from inventory")

class ServerAdmin:

    def getServerInfo(self):
        print("Enter the server you need to search: ")
        self.server = input()
        return self.server

    def addServerInfo(self):
        print("Enter server to be added to server: ")
        self.server = input()
        return self.server

    def removeServerInfo(self):
        print("Enter server to be removed from inventory")
        self.server = input()
        return self.server

servers=ServerInventory(['server1.localhost.com', 'server2.localhost.com','server3.localhost.com'])
admin = ServerAdmin()

while True:
    print("1. List all the server inventory")
    print("2. Search server infomation")
    print("3. Add server to inventory")
    print("4. Remove server from inventory")
    print("5. Quit")
    print("\n")
    adminChoice = int(input())
    if adminChoice is 1:
        servers.displayServerInventory()
    elif adminChoice is 2:
        servername = admin.getServerInfo()
        servers.searchServerInventory(servername)
    elif adminChoice is 3:
        servername = admin.addServerInfo()
        servers.addServerToInventory(servername)
    elif adminChoice is 4:
        servername = admin.removeServerInfo()
        servers.removeServerFromInventory(servername)
    else:
        quit()

