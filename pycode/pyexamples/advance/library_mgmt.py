# class library
# layers of abstraction => display book, lend book, add book

# class cutomer
# layers of abstraction => request book, return book

class Library:

    def __init__(self,listOfBooks):
        self.availablebooks = listOfBooks

    def displayAvailableBooks(self):
        for books in self.availablebooks:
            print(books)

    def lendBook(self,requestedBook):
        if requestedBook in self.availablebooks:
            print("borrowed book...")
            self.availablebooks.remove(requestedBook)
        else:
            print("Book not available")

    def addBook(self,returnedBook):
        self.availablebooks.append(returnedBook)
        print("Book added to library")

class Customer:
    def requestBook(self):
        print("Enter book you want to borrow: ")
        self.book = str(input())
        return self.book

    def returnBook(self):
        print("Add book to library: ")
        self.book = input()
        return self.book

library=Library(['book1','book2','book3'])
customer=Customer()
while True:
    print("1. Display Available Book")
    print("2. Request Book ")
    print("3. Return Book " )
    print("4. Quit")
    choice = int(input())
    if choice is 1:
        library.displayAvailableBooks()
    elif choice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif choice is 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    else:
        quit()
