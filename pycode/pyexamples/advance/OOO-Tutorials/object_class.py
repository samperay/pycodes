class Servers:
    # class attributes
    vendor = "Oracle"
    countOfHardDiskSlots = 4

    # class methods
    # since the object implicits to the class, hence self is passed by default.
    def displayServerDetails(self):
        self.countOfHardDiskSlots = 1
        print("Vendor: ", self.vendor)
        print("HDD Slots: ", self.countOfHardDiskSlots)


server1 = Servers()
server2 = Servers()

# instance attributes, first woudl be checked if any attributes exists, then it would
# assign those values, if it couldn't find, it would then check from class attributes to get
# the values and would be assigned.

# Override the class values and print the object values.
server1.countOfHardDiskSlots = 1
server1.vendor = "IBM"

print("Server2 gets values from the class attributes: ", server2.displayServerDetails())
print("")
# Explict and implict calls for object instance
print("First Method: Object calling to print...")
server1.displayServerDetails()
print("")
print("Second Method: Object calling to print...")
Servers.displayServerDetails(server1)
