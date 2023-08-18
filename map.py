from enemy import Enemy

class Room:
    
    def __init__(self, name: str, enemy):
        self.name = name
        self.enemy = enemy
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.is_fighting = False

    def __repr__(self):
        print(f"Room({self.name})")

    def __str__(self):
        return self.name

    def link_left(self, name: str, enemy):
        temp = Room(name, enemy)
        temp.right = self
        self.left = temp

    def link_right(self, name: str, enemy):
        temp = Room(name, enemy)
        temp.left = self
        self.right = temp

    def link_up(self, name: str, enemy):
        temp = Room(name, enemy)
        temp.down = self
        self.up = temp

    def link_down(self, name: str, enemy):
        temp = Room(name, enemy)
        temp.up = self
        self.down = temp

    def set_is_fighting(self, boolean: bool):
        self.is_fighting = bool

def setup():
    """
    Generates 3 rooms, named room1, room2, room3 and links them together
    """
    map = Room("Room1", Enemy('Dementors', 100))
    map.link_left("Room2", Enemy('Basilisk', 500))
    map.link_right("Room3", Enemy('Death Eater', 1000))
    map.link_up("Room4", Enemy('Voldemort', 5000))

    return map