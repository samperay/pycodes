class Servers:
    # initialization happens when object is being created. hence we would assign the values
    # using the init method
    def __init__(self, vendor):
        # self.vendor is the instance attribute name
        # vendor is the name of the attribute which you have passed
        self.vendor = vendor

    def displayServerDetails(self):
        print("Vendor: ", self.vendor)


# object created along with the values using init function
server1 = Servers("Oracle")
server2 = Servers("IBM")
server1.displayServerDetails()
server2.displayServerDetails()
