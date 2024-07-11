# lib/helpers.py
import click 

from Models.user import User

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
            User.create_user(username,password)
            print("")
            print("***Account Created!***")
            print("")
            print("Returning to User Menu")
        else: 
            print("Password must be more than 5 characters")
    else: 
        print("Username must be more than 5 characters")

def delete_user():
        print("Enter a User ID")
        id_ = input()
        if user := User.lookup_user(id_):
            user.delete_user()
            print("")
            print(f"***Deleted User Account {id_}***")
            print("Returning to User Menu!")
        else:
             print("No user attached to provided id")

def lookup_user():
        print("Enter a User ID")
        id_ = input()
        user = User.lookup_user(id_)
        print(user) if user else print (f"No server attached to id {id_}")
        print("Returning to User Menu!")

def all_users():
    users = User.all_users()
    print("")
    print("Listing All Users:")
    print("")
    for user in users:
        print(user)
    print("")
    print("Returning to User Menu!")

def lookup_user_server():
    list = User.all_users()
    print("")
    print("Please select a user by ID#:")
    print("")
    for user in list:
         print(user.id,user)
    print("")
    id_ = input()
    user = User.lookup_user(id_)
    print("")
    print(f"{user} is currently active on: {user.server()}")
    print("")
    print("Returning to User Menu!")

def exit_program():
    print("See you next time!")
    exit()