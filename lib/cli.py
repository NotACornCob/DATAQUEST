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
        if choice == "2":
            server_menu()
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice! GAME OVER")

def main_menu_prompt():
    print("Welcome to DATAQUEST!")
    print("ADMIN access granted!")
    print("Please select an option:")
    print("1. User Account Menu")
    print("2. Server Menu")
    print("3. Exit DataQuest")

def user_account_menu():
    while True: 
        user_account_menu_prompt()
        choice = input("> ")
        if choice == "1": 
            create_user_account()
        if choice == "2":
            edit_user_account()
        if choice == "3":
            lookup_user_account()
        if choice == "4":
            add_user_to_server()
        if choice == "5":
            remove_user_from_server()
        if choice == "6":
            delete_user_account()
        if choice == "7":
            main_menu()
        else: 
            print("Invalid choice! GAME OVER")


def user_account_menu_prompt():
    print("DataQuest User Accounts")
    print("Please select an option:")
    print("1. Create User Account")
    print("2. Edit User Account")
    print("3. Lookup Server Activity")
    print("4. Add User to Server")
    print("5. Remove User from Server")
    print("6. Delete User Account")
    print("7. Return to Main Menu")

def server_menu():
    while True: 
        server_menu_prompt()
        choice = input("> ")
        if choice == "1": 
            create_server()
        if choice == "2":
            edit_server()
        if choice == "3":
            delete_server()
        if choice == "4":
            lookup_active_users()
        if choice == "5":
            main_menu()
        else: 
            print("Invalid choice! GAME OVER")

def server_menu_prompt():
    print("DataQuest Servers")
    print("Please select an option:")
    print("1. Create Server")
    print("2. Edit Server")
    print("3. Lookup Active Users")
    print("4. Delete server")
    print("5. Return to Main Menu")

if __name__ == "__main__":
    main_menu()


def exit_program():
    print("See you next time!")
    exit()
