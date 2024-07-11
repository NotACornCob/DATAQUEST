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
    quirmish = User.create_user("Quirmish","123456",1)
    lordscottish = User.create_user("Lord Scottish","boingbong",atlantic.id)
    onionknight = User.create_user("Onion Knight","onionish",atlantic.id)
    rogier = User.create_user("Rogier","sleepy",atlantic.id)
    himbojones = User.create_user("Himbo Jones","1337H3x",pacific.id)
    notacorncob = User.create_user("NotACornCob","qwertyaf",pacific.id)
    fortnite = User.create_user("fortnite","fortnite",pacific.id)
    turtlewizard = User.create_user("Turtle Wizard","mana34557",chesapeake.id)
    malenia = User.create_user("Malenia","Miquella",chesapeake.id)

seed_database()
print("Seeded Database")
