# lib/helpers.py
import click 

from models.user import User

def create_user():
    print("Enter a Username")
    username = input("")
    if len(username) > 5:
        print(f"User Name Set to {username}")
        print("")
        print("Enter a Password")
        password = input("")
        if len(password) > 5: 
            User.create_table()
            User.create(username,password)
            print("")
            print("***Account Created!***")
            print("")
            print("Returning to User Menu")
        else: 
            print("Password must be more than 5 characters")
    else: 
        print("Username must be more than 5 characters")

def delete_user():
        print("")
        print("***Deleted User Account***")
        print("")
        print("Returning to User Menu!")

def lookup_user():
        print("")
        print("***Looked Up User Account***")
        print("")
        print("Returning to User Menu!")

def all_users():
        print("")
        print("***List of All Users***")
        print("")
        print("Returning to User Menu!")

def exit_program():
    print("See you next time!")
    exit()