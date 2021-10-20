#!/usr/bin/python3

# Lib Mgmt Systems

# Class - Library ( Abstraction )
# Methods - displayAvailbleBooks, lendAvailableBook, returnBook (Encapsulation)

# Class - Customer (Abstraction)
# Methods - requestBook, returnBook

class Library:

    def __init__(self, availbleBooks):
        self.availbleBooks = availbleBooks
        print(self.availbleBooks)

    def displayAvailbleBooks(self):
        for books in self.availbleBooks:
            print(books)

    def lendAvailableBook(self, requestedBook):
        if requestedBook in self.availbleBooks:
            print("Your book is available to lend")
            self.availbleBooks.remove(requestedBook)
        else:
            print("You book is not available")

    def addBook(self, returnbook):
        self.availbleBooks.append(returnbook)
        print("adding book back to the libary")


class Customer:
    def requestBook(self):
        print("Enter the book you like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the book you want to return: ")
        self.book = input()
        return self.book


library = Library(["book1", "book2", "book3"])
customer = Customer()
while True:
    print("1. Display Available Book")
    print("2. Request Book ")
    print("3. Return Book ")
    print("4. Quit")
    choice = int(input())
    if choice == 1:
        library.displayAvailbleBooks()
    elif choice == 2:
        requestedBook = customer.requestBook()
        library.lendAvailableBook(requestedBook)
    elif choice == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    else:
        quit()
