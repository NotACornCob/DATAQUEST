from models.__init__ import CURSOR, CONN
from models.server import Server 
from models.user import User

def seed_database():
    User.drop_table()
    Server.drop_table()
    User.create_table()
    Server.create_table()

    #Seed Data
    atlantic = Server.create_server("Atlantic",12)
    pacific = Server.create_server("Pacific",8)
    chesapeake = Server.create_server("Chesapeake",4)
    User.create_user("Quirm","12345")
    User.create_user("Lord Scottish","boing")
    User.create_user("Onion Knight","onion")
    User.create_user("Rogier","sleep")
    User.create_user("Himbo Jones","1337")
    User.create_user("NotACornCob","qwerty")
    User.create_user("fortnite","fortnite")
    User.create_user("Turtle Wizard","mana345")
    User.create_user("Malenia","Miquella")

seed_database()
print("Seeded Database")
