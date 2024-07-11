# lib/server_menu_helpers.py
from models.server import Server

def create_server():
    print("Enter a Server Name")
    name = input("")
    if len(name) > 5:
        print(f"Server Name Set to {name}")
        print("")
        print("Enter Max Player Count")
        max = input()
        if 1 <= int(max) <= 16: 
            print(f"Max Player Count Set to {max}")
            Server.create_server(name,int(max))
            print("")
            print("***Server Created!***")
            print("")
            print("Returning to Server Menu")
        else: 
            print("Error: Server max must be between 1 and 16 users")
            print("Create Server Menu Lands a critical hit!")
            print("Retreating to Server Menu!")

    else: 
        print("Error: Server name must be more than 5 characters")
        print("Create Server Menu Lands a critical hit!")
        print("Retreating to Server Menu!")
        
def delete_server():
        servers = Server.all_servers()
        print("")
        print("Please select a server by ID#")
        print("")
        for server in servers:
            print(server)
        id_ = input()
        if server := Server.find_by_id(id_):
            server.delete_server()
            print("")
            print(f"***Server {id_} Deleted***")
            print("Returning to Server Menu!")
        else:
            print("Error: No Server Attached to Provided id")
            print("Delete Server Menu Lands a critical hit!")
            print("Retreating to Server Menu!")

def lookup_server():
        print("")
        print("Please enter a server ID")
        print("")
        id_ = input()
        server = Server.find_by_id(id_)
        if server:
            print(server) 
        else: 
             print(f"No server attached to id {id_}")
             print("Lookup Server Menu Lands a critical hit!")
             print("Retreating to Server Menu!")

def all_servers():
      servers = Server.all_servers()
      print("")
      print("Listing All Servers:")
      print("")
      for server in servers:
        print(server)
      print("")
      print("Returning to Server Menu!")

def users():
    list = Server.all_servers()
    print("")
    print("Please select a server by ID#:")
    print("")
    for server in list:
         print(server)
    print("")
    id_ = input()
    server = Server.find_by_id(id_)
    print("")
    print(f"{server.name} server population: {len(server.users())}")
    print("")
    print(server.users())
    print("")
    print("Returning to Server Menu!")


def exit_program():
    print("Thank you for playing DataQuest!")
    exit()