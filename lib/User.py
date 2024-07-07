class User:

    all = []

    def __init__(self,name=None,password=None):
        self.name = name
        self.password = password 
    
    def __repr__(self):
        return f"<User {self.id}: {self.name}>"

    @property
    def name(self):
        self.name

    @name.setter
    def name(self,name): 
        if name > len(5):
            self.name = name
        else: return ValueError("Name must be greater than 5 characters in length")

    @property
    def password(self):
        self.password
    
    @password.setter
    def password(self,password):
        if password > len(5): 
            self.password = password
        else: return ValueError("Password must be greater than 5 characters in length")