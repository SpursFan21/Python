"""
Problem:
You are tasked with creating a program to manage a library system. The program should be able to handle books, patrons (library users), and transactions (books borrowed/returned by patrons). Each book has a title, author, and availability status. Each patron has a name and a list of books they currently have borrowed. Transactions involve a patron borrowing or returning a book.

Your task is to create a Python program that models this library system using classes and objects. Implement the following functionalities:

Create classes for Book, Patron, and Transaction.
Implement an __init__ method for each class to initialize their attributes.
Implement methods to borrow and return books for patrons.
Implement methods to display the details of books, patrons, and transactions.
Your program should demonstrate the use of classes, objects, and the __init__ method to organize and manage the library system effectively.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.availability = True

class Inventory:
    @staticmethod
    def get_books():
        """
        Get a list of the libraries inventory.
        """
        return [
            ("Black Knight", "Author A"),
            ("My ABC's", "Author B"),
            ("The Lord of The Rings", "Author C"),
            ("Star Wars", "Author D")
        ]

class LibrarySystem:
    def __init__(self):
        self.books = []  # Initialize an empty list to store books in the library
        self.preload_books()

    def preload_books(self):
        """
        Preload books into the library system from the PreloadedBooks class.
        """
        inventory = Inventory.get_books()
        for book_info in inventory:
            title, author = book_info
            book = Book(title, author)
            self.books.append(book)

    def display_books(self):
        """
        Display the details of all books in the library.
        """
        if not self.books:
            print("The library is currently empty.")
        else:
            print("Books available in the library:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. Title: {book.title}, Author: {book.author}, Availability: {'Available' if book.availability else 'Not Available'}")
                
class Patron:
    def __init__(self, name):
        self.name = name
        self.books_borrowed = []
        
class Transaction:
    def __init__(self, book, patron, transaction_date):
        self.book = book
        self.patron = patron
        self.transaction_date = transaction_date
        


# Initialize the library system
library = LibrarySystem()

# Display the books in the library
library.display_books()
