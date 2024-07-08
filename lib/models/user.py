from models.__init__ import CURSOR, CONN
import ipdb

class User:

    all = {}

    def __init__(self,name=None,password=None):
        self.name = name
        self.password = password 
    
    def __repr__(self):
        return f"<User {self.id}: {self.name}>"

    @property
    def name(self):
        self._name

    @name.setter
    def name(self,name): 
        if len(name) > 5:
            self._name = name
        else: return ValueError("Name must be greater than 5 characters in length")

    @property
    def password(self):
        self._password
    
    @password.setter
    def password(self,password):
        if len(password) > 5: 
            self._password = password
        else: return ValueError("Password must be greater than 5 characters in length")

    @classmethod 
    def create_table(cls):
        '''Create a table for persistant user instances'''
    sql = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    server_id INTEGER,
    FOREIGN KEY (server_id) REFERENCES servers(id))
    """ 
    CURSOR.execute(sql)
    CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS users;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def save(self,name,password):
        """Add new user to database with provided username & password."""
        sql = """
            INSERT INTO users (username,password)
            VALUES (?,?)"""
        CURSOR.execute(sql,(str(name),str(password)))
        CONN.commit()

    def update(self):
        """Update table row corresponding to current user instance"""
        sql = """
        UPDATE users
        SET name = ?, password = ?"""
        CURSOR.execute(sql,(str(self.name),str(self.password)))
        CONN.commit()

    def delete(self):
        """Delete row corresponding to current user instance"""
        sql = """
        DELETE FROM users
        WHERE id = ?
        """
        CURSOR.execute(sql,(self.id))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls,name,password):
        '''Initialize a user instance and save user instance data to database'''
        user = cls(str(name),str(password))
        user.save(name,password)
        return user
        