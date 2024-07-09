import click 

from models.server import Server
import ipdb

def create_server():
    print("Enter a Server Name")
    name = input("")
    if len(name) > 5:
        print(f"Server Name Set to {name}")
        print("")
        print("Enter Max Player Count")
        player_max = input()
        if 1 <= int(player_max) <= 16: 
            print(f"Max Player Count Set to {player_max}")
            Server.create_table()
            Server.create_server(name,player_max)
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
        print("")
        print("***Looked Up Server***")
        print("")
        print("Returning to Server Menu!")

def all_servers():
      print("")
      print("***List of All Servers***")
      print("")
      print("Returning to Server Menu!")

def exit_program():
    print("See you next time!")
    exit()