class Apple:
    manufacturer = "Apple Inc"
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("Contact Details, ", self.contactWebsite)


class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacturer = 2021

    def manufacturerDetails(self):
        print("Macbook manufactured in {} by {}".format(self.yearOfManufacturer, self.manufacturer))


macbook = MacBook()
macbook.manufacturerDetails()
macbook.contactDetails()
