from models.__init__ import CURSOR, CONN
from lib.models.server import Server 
from lib.models.user import User

def seed_database():
    User.create_table()
    User.create_user()