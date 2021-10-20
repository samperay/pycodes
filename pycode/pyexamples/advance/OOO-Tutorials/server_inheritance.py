# Server Inheritance

# Parent Class - ServerHardware
# Parent Class Methods - getServerHardwareDetails
# Parent Class Attributes - Name, Model, CPU, RAM, Disks

# Child Class - Oracle, IBM, HP
# Child Class Methods - getServerHardwareDetails
# Child Class Attributes - Vendor_Name, SerialNo, ProductNo

class ServerHardware:
    contact = "www.serverhardwares.com/contact"
    startOfManufacturer = "2011"

    def contactDetails(self):
        print("Contact Details, ", self.contact)


class OracleHardwares(ServerHardware):
    def __init__(self):
        self.vendor_name = "Oracle"

    def manufacturerDetails(self):
        print("{} Hardwares can be contacted at {} for year {}".format(self.vendor_name,
                                                                       self.contact, self.startOfManufacturer))


oracle_server = OracleHardwares()
oracle_server.manufacturerDetails()
oracle_server.contactDetails()
