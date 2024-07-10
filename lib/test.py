import ipdb

class Server:

    all = {}

    def __init__(self,name,player_max,id=None):
        self.id = id
        self.name = name
        self.player_max = player_max
        ipdb.set_trace()

    def __repr__(self):
        return f"<Server {self.id}: {self.name}, players:{self.player_max}>"
    
    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self,name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
    
server = Server("thing","8")