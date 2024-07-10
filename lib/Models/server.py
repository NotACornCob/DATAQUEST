#lib/models/server.py
from Models.__init__ import CURSOR, CONN
import ipdb

class Server:

    all = {}

    def __init__(self,name,player_max,id=None):
        self.id = id
        self.name = name
        self.player_max = player_max
        
    def __repr__(self):
        return f"<Server {self.id}: {self.name}, players:{self.player_max}>"
    
    @property
    def name(self):
       return self._name 

    @name.setter
    def name(self,name):
        if len(name) > 5:
            self._name = name
        else: 
            return ValueError("Name must be greater than 5 characters in length")
    
    @property
    def player_max(self):
        self._player_max
    
    @player_max.setter
    def player_max(self,player_max):
        """ if (1 <= player_max <= 16): """
        self._player_max = player_max
        """ else: return ValueError("Server max must be between 1 and 16 users") """
    
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS servers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        player_max INTEGER)
        """ 
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS servers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def save(self,name,player_max):
        """Add new server to database with provided name & player_max."""
        sql = """
            INSERT INTO servers (name,player_max)
            VALUES (?,?)"""
        CURSOR.execute(sql,(name,player_max))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def delete_server(self):
        sql = """
        DELETE FROM servers
        WHERE id = ?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def instance_from_db(cls,row):
        """Return a Department object having the attribute values from the table row."""
        server = cls.all.get(row[0])
        if server:
            server.name = row[1]
            server.player_max = row[2]
        else: 
            server = cls(row[1],row[2])
            server.id = row[0]
            cls.all[server.id] = server
        return server
    
    @classmethod
    def create_server(cls,name,player_max):
        '''Initialize a server instance and save server instance data to database'''
        server = cls(name,player_max)
        server.save(name,player_max)
        return server
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
        SELECT *
        FROM servers
        WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def all_servers(cls):
        """Return a list containing a Department object per row in the table"""
        sql = """
            SELECT *
            FROM servers
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def users(self):
        from user import User
        sql = """
            SELECT * FROM users
            WHERE server_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            User.instance_from_db(row) for row in rows
        ]
server = Server("server",12)
Server.find_by_id(1)
Server.create_server("Atlantic","12")