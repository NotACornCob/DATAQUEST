#!/usr/bin/env python3

from helpers import (
    exit_program,
    create_user_account,
    edit_user_account,
    delete_user_account,
    lookup_user_account,
    add_user_to_server,
    remove_user_from_server,
    delete_user_account,
    create_server,
    edit_server,
    delete_server,
    lookup_active_users,
)

def main_menu():
    while True:
        main_menu_prompt()
        choice = input("> ")
        if choice == "1":
            user_account_menu()
        elif choice == "2":
            server_menu()
        elif choice == "3":
            exit_program()
        else:
            print("")
            print("Invalid choice. The Main Menu returns a Critical Hit! GAME OVER")
            print("")
            exit()

def main_menu_prompt():
    print("")
    print("----------------------")
    print("Welcome to DATAQUEST!")
    print("----------------------")
    print("ADMIN access granted!")
    print("")
    print("Please select an option:")
    print("")
    print("1. User Account Menu")
    print("2. Server Menu")
    print("3. Exit DataQuest")
    print("")

def user_account_menu():
    while True:
        user_account_menu_prompt()
        choice = input("> ")
        if choice == "1": 
            create_user_account()
        elif choice == "2":
            edit_user_account()
        elif choice == "3":
            lookup_user_account()
        elif choice == "4":
            add_user_to_server()
        elif choice == "5":
            remove_user_from_server()
        elif choice == "6":
            delete_user_account()
        elif choice == "7":
            main_menu()
        else:
            print("") 
            print("Invalid choice. The User Account Menu Returns a Critical Hit!")
            print("GAME OVER")
            print("")
            exit()


def user_account_menu_prompt():
    print("")
    print("-------------------------")
    print("DataQuest User Accounts")
    print("-------------------------")
    print("")
    print("Please select an option:")
    print("")
    print("1. Create User Account")
    print("2. Edit User Account")
    print("3. Lookup Server Activity")
    print("4. Add User to Server")
    print("5. Remove User from Server")
    print("6. Delete User Account")
    print("7. Return to Main Menu")
    print("")

""" def create_user_account_menu():
    while True:
        create_user_account_prompt()
        choice = input("> ")
        if choice == "1":
            
def create_user_account_prompt():
    print("Enter A Username") """


def server_menu():
    while True:
        server_menu_prompt()
        choice = input("> ")
        if choice == "1": 
            create_server()
        elif choice == "2":
            edit_server()
        elif choice == "3":
            delete_server()
        elif choice == "4":
            lookup_active_users()
        elif choice == "5":
            main_menu()
        else:
            print("")
            print("Invalid choice. The Server Menu Returns a Critical Hit!")
            print("GAME OVER")
            print("")
            exit()

def server_menu_prompt():
    print("")
    print("--------------------")
    print("DataQuest Servers")
    print("--------------------")
    print("")
    print("Please select an option:")
    print("")
    print("1. Create Server")
    print("2. Edit Server")
    print("3. Delete server")
    print("4. Lookup Active Users")
    print("5. Return to Main Menu")
    print("")

if __name__ == "__main__":
    main_menu()


def exit_program():
    print("See you next time!")
    exit()