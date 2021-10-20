#!/usr/bin/python3

# Class - ServerInventory
# Methods - getServerDetails , addServersDetails, removeServers

# Class - Employee
# Methods - addServer, removeServer

class ServerInventory:

    def __init__(self, inventoryDB):
        self.inventoryDB = inventoryDB

    def inventoryDetails(self):
        print("Server Details")
        print("-====-=====-")
        for key, value in self.inventoryDB.items():
            print(key, ":", value)

    def addToInventory(self):
        pass

    def deleteFromInventory(self):
        pass


class InventoryAdmin:
    def getServersToAddIntoInventory(self):
        pass

    def deleteServersFromInventory(self):
        pass


server_info = {
    "Name": "ServerName",
    "Model": "X1223",
    "CPU": 2,
    "Memory": "256MB"
}

inventory_mgmt = ServerInventory(server_info)
admin = InventoryAdmin()
inventory_mgmt.inventoryDetails()
