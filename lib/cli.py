#!/usr/bin/env python3

from user_menu_helpers import (
    exit_program,
    create_user,
    delete_user,
    lookup_user,
    all_users,
)

from server_menu_helpers import (
    exit_program,
    create_server,
    delete_server,
    lookup_server,
    all_servers,
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
            create_user()
        elif choice == "2":
            delete_user()
        elif choice == "3":
            lookup_user()
        elif choice == "4":
            all_users()
        elif choice == "5":
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
    print("2. Delete User Account")
    print("3. Lookup User by ID")
    print("4. List All Users")
    print("5. Return to Main Menu")
    print("")

def server_menu():
    while True:
        server_menu_prompt()
        choice = input("> ")
        if choice == "1": 
            create_server()
        elif choice == "2":
            delete_server()
        elif choice == "3":
            lookup_server()
        elif choice == "4":
            all_servers()
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
    print("2. Delete Server")
    print("3. Lookup Server by ID")
    print("4. List All Servers")
    print("5. Return to Main Menu")
    print("")

if __name__ == "__main__":
    main_menu()