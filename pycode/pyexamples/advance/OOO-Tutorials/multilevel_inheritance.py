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


class OracleHardwares(ServerHardware):
    vendor_name = "Oracle"
    contact = "www.oracle.com/contact"


class OracleSoftwares(OracleHardwares):
    os = "Oracle Linux"
    kernel = "uek"

    def displayInstallationNotes(self):
        if self.multithreading is True:
            print("Since {} vendor supports {}, we can installed {} with {} as softwares".format(
                self.vendor_name, self.multithreading, self.os, self.kernel))
        else:
            print("Oracle Software Not supported")


os = OracleSoftwares()
os.displayInstallationNotes()
