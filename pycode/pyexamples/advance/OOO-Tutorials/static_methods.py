class Servers:
    def getVendorDetails(self, vendor):
        self.vendor = vendor

    # there is no usage of self being used in this function and hence we could remove it
    # however, since the object is passed, it would be expecting 1 argument.
    # To overcome this problem we would make a decorator with "@staticmethod" by removing "self"
    # python understand that binding to the object has to be ignored
    # def displayVendorDetails(self):
    #     print("Thank you for your purchase")

    @staticmethod
    def displayVendorDetails():
        print("Thank you for your purchase")


server1 = Servers()
server1.getVendorDetails("Oracle")
server1.displayVendorDetails()
