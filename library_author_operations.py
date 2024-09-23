# Library Author Operations

from termcolor import colored

class Author:
    def __init__(self, author_name, year_born, country_of_birth, books_written):
        self.author_name = author_name
        self.year_born = year_born
        self.country_of_birth = country_of_birth
        self.books_written = books_written

    def get_author_name(self):
        return self.author_name
    
    def get_books_written(self):
        return self.books_written
    
    def view_author_details(self):
        print(colored(f"\nAuthor: {self.author_name}", "cyan", attrs=["bold"]))
        print(colored(f"Year Born: {self.year_born} \nCountry of Birth: {self.country_of_birth}", "grey"))
        print(colored("Books Written:", "cyan"))
        print(colored(f"{self.books_written}", "grey"))
        print(colored("-------------", "grey"))

class AuthorOperations:
    def __init__(self, authors):
        self.authors = authors

    def add_new_author(self):
        author_name = input("\nEnter the author name: ").title()
        year_born = int(input(f"\nEnter the year {author_name} was born: "))
        country_of_birth = input(f"\nEnter the country {author_name} was born: ").title()
        books_written = input(f"\nEnter the books {author_name} has written: ").title()
        author = Author(author_name, year_born, country_of_birth, books_written)
        self.authors[author_name] = author
        return self.authors
    
    def display_all_authors(self):
        if len(self.authors) == 0:
            print("\nThere are no authors in the Library.")
        else:
            print(colored("\nAuthors:", "white", attrs=["bold"]))
            for author in self.authors.values():
                author.view_author_details()