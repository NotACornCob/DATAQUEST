class Server:

    all = []

    def __init__(self,name,id=None):
        self.name = name
        self.id = id
        
    def __repr__(self):
        return f"<Server {self.id}: {self.name}>"

    @property
    def name(self):
        self.name 

    @name.setter
    def name(self,name):
        if name > len(5):
            self.name = name
        else: return ValueError("Name must be greater than 5 characters in length")
    
    
    