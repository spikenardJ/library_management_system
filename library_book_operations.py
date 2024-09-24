# Library Book Operations

from termcolor import colored

users = {}

class Book:
    def __init__(self, title, author, genre, isbn, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.publication_date = publication_date
        self.is_available = True

    def get_title(self):
        return self.title.title()
    
    def get_availability(self):
        return self.is_available
    
    def change_book_status(self):
        if self.is_available:
            self.is_available = False
        elif not self.is_available:
            self.is_available = True

    def display_book_information(self):
        print(colored(f"\nTitle: {self.title}", "cyan", attrs=["bold"]))
        print(colored(f"Author: {self.author} \nGenre: {self.genre} \nISBN: {self.isbn} \nPublication Date: {self.publication_date}", "grey"))
        if self.get_availability() == True:
            print(colored("Availability: Available", "grey"))
        else:
            print(colored("Availability: Borrowed", "grey"))
        print(colored("-------------", "grey"))

class BookOperations:
    def __init__(self, library, current_loans):
        self.library = library
        self.current_loans = current_loans

    def add_book(self):
        title = input("\nEnter the book's title: ").title()
        author = input("Enter the author: ").title()
        genre = input("Enter the genre: ").title()
        isbn = input("Enter the isbn: ")
        publication_date = input("Enter the publication date: ")
        book = Book(title, author, genre, isbn, publication_date)
        self.library[isbn] = book
        print("Book added successfully.")
        return self.library
    
    def search_book(self):
        title = input("\nEnter the book title to search: ").title()
        found = False
        for book in self.library.values():
            if book.get_title() == title.title():
                print("\nBook:")
                book.display_book_information()
                found = True
                break
        if not found:
            print("\nBook not found.")

    def display_books(self):
        if len(self.library) == 0:
            print("\nThere are no books in the Library.")
        else:
            print(colored("\nLibrary Books:", "white", attrs=["bold"]))
            for book in self.library.values():
                book.display_book_information()

    def checkout_book(self):
        print(colored("\nLibrary Books:", "white", attrs=["bold"]))
        for book in self.library.values():
            book.display_book_information()
        title = input("\nEnter the title of the book to borrow: ").title()
        user = input("\nEnter name of user: ").title()
        found = False
        for book in self.library.values():
            print(book)
            if title == book.get_title() and book.get_availability():
                self.current_loans[title] = user
                book.change_book_status()
                print(user)
                print(colored(f"\nBook {book.get_title()} borrowed successfully by {user}.", "grey"))
                found = True
                break
        if not found:
            print("\nBook not available or not found.")
        return self.library

    def checkin_book(self):
        title = input("\nEnter the title of the book to return: ").title()
        user = input("\nEnter name of user: ").title()
        found = False
        for book in self.library.values():
            if title == book.get_title() and not book.get_availability():
                del self.current_loans[title]
                book.change_book_status()
                print(colored(f"\nBook {book.get_title()} returned successfully from {user}.", "grey"))
                found = True
                break
        if not found:
            print("\nBook not available or not found.")
        return self.library