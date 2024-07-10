from Models.__init__ import CURSOR, CONN
from Models.server import Server 
from Models.user import User
import ipdb

def seed_database():
    User.drop_table()
    Server.drop_table()
    User.create_table()
    Server.create_table()

    #Seed Data
    atlantic = Server.create_server("Atlantic","12")
    pacific = Server.create_server("Pacific","8")
    chesapeake = Server.create_server("Chesapeake","4")
    quirmish = User.create_user("Quirmish","12345")
    User.create_user("Lord Scottish","boing")
    User.create_user("Onion Knight","onion")
    User.create_user("Rogier","sleep")
    User.create_user("Himbo Jones","1337")
    User.create_user("NotACornCob","qwerty")
    User.create_user("fortnite","fortnite")
    User.create_user("Turtle Wizard","mana345")
    User.create_user("Malenia","Miquella")
    quirmish.add_to_server(atlantic.id)

seed_database()

print("Seeded Database")
