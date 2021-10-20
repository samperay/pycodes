#!/usr/bin/python3

class Library:

    def __init__(self, availableBooks):
        self.availableBooks = availableBooks

    def displayAllAvaialbleBooks(self):
        for book in self.availableBooks:
            print(book)

    def lendBookToStudents(self, bookToBorrow):
        if bookToBorrow in self.availableBooks:
            print("Book available, you can borrow the book")
            self.availableBooks.remove(bookToBorrow)
        else:
            print("Book is not available to borrow")

    def receiveBookFromStudents(self, returnBook):
        self.availableBooks.append(returnBook)
        print("Book has been returned back to library")


class Student:
    def getYouBookFromLibrary(self):
        print("Enter the book you want from the avaialble book list")
        self.book = input()
        return self.book

    def returnYourBookToLibrarian(self):
        print("Enter your book to return to Library")
        self.book = input()
        return self.book


listOfBooks = ["Book1", "Book2", "Book3"]
library = Library(listOfBooks)
student = Student()
while True:
    print("Welcome To Lib mgmt")
    print("1. Display")
    print("2. Get book from Lib")
    print("3. Return your book to Lib")
    print("4. Quit")
    print("Enter your choice: ")
    choice = int(input())
    if choice == 1:
        library.displayAllAvaialbleBooks()
    elif choice == 2:
        student_book = student.getYouBookFromLibrary()
        library.lendBookToStudents(student_book)
    elif choice == 3:
        student_book = student.returnYourBookToLibrarian()
        library.receiveBookFromStudents(student_book)
    elif choice == 4:
        print("Quitting")
        quit()
