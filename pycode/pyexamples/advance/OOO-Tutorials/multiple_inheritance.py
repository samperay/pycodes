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
    multithreading = True

    def contactDetails(self):
        print("Contact Details, ", self.contact)


class OracleHardwares:
    vendor_name = "Oracle"
    contact = "www.oracle.com/contact"

# Multiple Inheritance


class OracleSoftwares(OracleHardwares, ServerHardware):
    def __init__(self):
        if self.multithreading is True:
            print("{} vendor supports, please contact {}".format(self.vendor_name, self.contact))


application = OracleSoftwares()
