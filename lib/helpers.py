# lib/helpers.py
import click 

from models.user import User

def create_user_account():
    print("Enter a Username")
    username = input("")
    if len(username) > 5:
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

def edit_user_account():
        print("")
        print("***Edited User Account***")
        print("")
        print("Returning to User Menu!")

def delete_user_account():
        print("")
        print("***Deleted User Account***")
        print("")
        print("Returning to User Menu!")


def lookup_user_account():
        print("")
        print("***Looked Up User Account***")
        print("")
        print("Returning to User Menu!")

def add_user_to_server():
        print("")
        print("***Added User to Server***")
        print("")
        print("Returning to User Menu!")

def remove_user_from_server():
        print("")
        print("***Deleted User From Server***")
        print("")
        print("Returning to User Menu!")

def create_server():
        print("")
        print("***Server Created***")
        print("")
        print("Returning to User Menu!")
        
def edit_server():
        print("")
        print("***Edited Server***")
        print("")
        print("Returning to User Menu")

def delete_server():
        print("")
        print("***Server Deleted***")
        print("")
        print("Returning to User Menu")

def lookup_active_users():
        print("")
        print("***Found Active Users***")
        print("")
        print("Returning to User Menu")

def exit_program():
    print("")
    print("See you next time!")
    exit()
