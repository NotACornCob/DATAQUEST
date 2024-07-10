import click 

from Models.server import Server
import ipdb

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
            Server.create_table()
            Server.create_server(name,max)
            print("")
            print("***Server Created!***")
            print("")
            print("Returning to Server Menu")
        else: 
            print("Server max must be between 1 and 16 users")
    else: 
        print("Server name must be more than 5 characters")
        
def delete_server():
        print("Enter a Server ID")
        id_ = input()
        if server := Server.find_by_id(id_):
            server.delete_server()
            print("")
            print(f"***Server {id_} Deleted***")
            print("Returning to Server Menu!")
        else:
            print("No server attached to provided id")

def lookup_server():
        print("Enter a Server ID")
        id_ = input()
        server = Server.find_by_id(id_)
        print(server) if server else print(f"No server attached to id {id_}")

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
    print("See you next time!")
    exit()