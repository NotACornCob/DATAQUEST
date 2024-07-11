# lib/user_menu_helpers.py
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
            User.create_user(username,password,1)
            print("")
            print("***Account Created!***")
            print("")
            print("Returning to User Menu")
        else: 
            print("Password must be more than 5 characters")
    else: 
        print("Username must be more than 5 characters")

def delete_user():
        list = User.all_users()
        print("")
        print("Please select a user by ID#:")
        print("")
        for user in list:
            print(user.id,user)
        print("")
        id_ = input()
        if user := User.lookup_user(id_):
            print("")
            print(f"***Deleting User Account {user}***")
            user.delete_user()
            print("Returning to User Menu!")
        else:
            print("Error: No user attached to provided id")
            print("Delete User Menu Lands a critical hit!")
            print("Retreating to User Menu!")

def lookup_user():
        list = User.all_users()
        print("")
        print("Please provide a user ID:")
        print("")
        id_ = input()
        user = User.lookup_user(id_)
        if user: 
            print("")
            print(f"Your query returned the following user account: {user} password: <{user.password}> server_id: <{user.server_id}>")
            print("")
            print("Returning to User Menu!")
        else: 
            print (f"Error: No server attached to id {id_}")
            print("Lookup User Menu Lands a critical hit!")
            print("Retreating to User Menu!")
        

def all_users():
    users = User.all_users()
    print("")
    print("Listing All Users:")
    print("")
    for user in users:
        print(user.id,user)
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
    print("Thank you for playing DataQuest!")
    exit()