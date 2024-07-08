# lib/helpers.py
import click 

from models.user import User

def create_user_account():
    while True:
        print("Enter a Username")
        username = input("")
        if len(username) > 5:
            print("Enter a Password")
            password = input("")
            if len(password) > 5: 
                User.create_table()
                User.create(username,password)
                print(f"Account Created!")
                exit()
            else: 
                print("Password must be more than 5 characters")
        else: 
            print("Username must be more than 5 characters")

def edit_user_account():
        return print("edited user account!")
        exit()

def delete_user_account():
        return print("deleted user account!")

def lookup_user_account():
        return print("looked up user account")
        

def add_user_to_server():
        return print("added user to server")

def remove_user_from_server():
        return("deleted user from server")
        

def create_server():
        return("server created")
        
def edit_server():
        return("edited server")

def delete_server():
        return("server deleted")

def lookup_active_users():
        return ("found active users")

def exit_program():
    print("See you next time!")
    exit()
