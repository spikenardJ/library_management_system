# Library User Operations

# library_users = users()

from termcolor import colored
import library_book_operations
import re

class User:
    def __init__(self, user_name, user_phone_number, user_email, user_library_id):
        self.user_name = user_name
        self.__user_phone_number = user_phone_number
        self.__user_email = user_email
        self.__user_library_id = user_library_id
        self.books_borrowed = []

    def get_user_name(self):
        return self.user_name
    
    def get_user_phone_number(self):
        return self.__user_phone_number
    
    def get_user_email(self):
        return self.__user_email
    
    def get_user_library_id(self):
        return self.__user_library_id
    
    def get_books_borrowed(self):
        return self.books_borrowed
    
    def set_books_borrowed(self):
        return self.books_borrowed
    
    def view_user_details(self):
        print(colored(f"\nName: {self.user_name}", "cyan", attrs=["bold"]))
        print(colored(f"Phone: {self.__user_phone_number} \nEmail: {self.__user_email} \nLibraray ID: {self.__user_library_id}", "grey"))
        print(colored("Books Borrowed:", "cyan"))
        print(colored(f"{self.__books_borrowed}", "grey"))
        print(colored("-------------", "grey"))

class UserOperations:
    def __init__(self, users):
        self.users = users

    def add_new_user(self):
        user_name = input("\nEnter the name of the new user: ").title()
        user_phone_number = input("\nEnter the user's phone number 1-###-###-####: ")
        user_email = input("\nEnter the user email: ")
        user_library_id = input("\nEnter the library ID of the new user: ")
        if re.match(r"^(1-)?\d{3}-\d{3}-\d{4}$", user_phone_number) and re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
            user = User(user_name, user_phone_number, user_email, user_library_id)
            self.users[user_library_id] = user
            return self.users
        else:
            print("Invalid entry of phone number or email address. Please try again.")

    def display_all_users(self):
        if len(self.users) == 0:
            print("\nThere are no users in the Library.")
        else:
            print(colored("\nLibrary Users:", "white", attrs=["bold"]))
            for user in self.users.values():
                user.view_user_details()