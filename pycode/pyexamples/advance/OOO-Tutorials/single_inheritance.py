class Apple:
    manufacturer = "Apple Inc"
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("Contact Details, ", self.contactWebsite)


class MacBook(Apple):

    # protected attribute, you would just say that use this attribute only in this class and no where else

    _color = "Grey"

    # private attribute
    __password = "private"  # NameDangling i.e _Apple__companyManufactureYear

    def __init__(self):
        self.yearOfManufacturer = 2021

    def manufacturerDetails(self):
        print("Macbook manufactured in {} by {}".format(
            self.yearOfManufacturer, self.manufacturer))


macbook = MacBook()
macbook.manufacturerDetails()
macbook.contactDetails()
print("Protected Attribute: ", macbook._color)
print("Private Attribute: ", macbook._MacBook__password)
