#lib/models/user.py
from models.__init__ import CONN, CURSOR
from models.server import Server

class User:

    all = {}

    def __init__(self,name,password,server_id=1,id=None):
        self.id= id
        self.server_id = server_id
        self.name = name
        self.password = password
    
    def __repr__(self):
        return f"<{self.name}>"
    
    @property
    def name(self):
       return self._name

    @name.setter
    def name(self,name): 
        if isinstance(name, str) and len(str(name)) > 5:
            self._name = name
        else: raise ValueError("Name must be greater than 5 characters in length")

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,password):
        if isinstance(password,str) and len(password) > 5: 
            self._password = password
        else: raise ValueError("Password must be greater than 5 characters in length")

    @classmethod
    def create_user(cls,name,password,server_id):
        '''Initialize a user instance and save user instance data to database'''
        user = cls(name,password,server_id)
        user.save()
        return user

    def save(self):
        """Add new user to database with provided username & password."""
        sql = """
            INSERT INTO users (username,password,server_id)
            VALUES (?,?,?)"""
        CURSOR.execute(sql,(self.name,self.password,self.server_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        self.all[self.id] = self

    @classmethod 
    def create_table(cls):
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

    def delete_user(self):
        sql = """
        DELETE FROM users
        where id = ?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls,row):
        """Return a user object having the attribute values from the table row"""
        user = cls.all.get(row[0])
        if user:
            user.name = row[1]
            user.password = row[2]
        else: 
            user = cls(row[1],row[2])
            user.id = row[0]
            cls.all[user.id] = user
        return user
    
    def update(self):
        """Update table row corresponding to current user instance"""
        sql = """
        UPDATE users
        SET name = ?, password = ?"""
        CURSOR.execute(sql,(str(self.name),str(self.password)))
        CONN.commit()

    def delete_user(self):
        """Delete row corresponding to current user instance"""
        sql = """
        DELETE FROM users
        WHERE id = ?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def lookup_user(cls, id):
        sql = """
        SELECT *
        FROM users
        WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row)
    
    @classmethod
    def all_users(cls):
        sql = """SELECT *
        FROM users
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def add_to_server(self,server_id):
        self.server_id = server_id
        self.update_user_server()
    
    def update_user_server(self):
        sql = """
        UPDATE users
        SET server_id = ?
        WHERE id = ?"""
        CURSOR.execute(sql,(str(self.server_id),self.id))
        CONN.commit()
    
    def server(self):
        from models.server import Server
        sql = """
        SELECT * FROM servers
        WHERE id = ?"""
        rows = CURSOR.execute(sql, (self.server_id,),).fetchall()
        return [Server.instance_from_db(row) for row in rows]