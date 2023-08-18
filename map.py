from enemy import Enemy

class Room:
    """
    creates the room

    Attribute
    ---------
    + name: str
    + enemy: str
    + right: str
    + left: str
    + up: str
    + down: str
    + been_here: bool
    - is_fighting: bool

    Method
    ------
    + link_left(): updates the room to the left of the home room(self.name)
    + link_right(): updates the room to the right of the home room(self.name)
    + link_up(): updates the room to the up of the home room(self.name)
    + link_down(): updates the room to the down of the home room(self.name)
    + set_is_fighting: updates the status of the character in the room
    + get_is_fighting: gets the status of the character in the room
    + set_been_here(): updates the status of wether the character has been to this room
    + get_been_here(): gets the status of wether the character has been to this room
    """
    
    def __init__(self, name: str, enemy, description):
        self.name = name
        self.enemy = enemy
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.been_here = False
        self.is_fighting = False
        self.description = description

    def __repr__(self):
        print(f"Room({self.name})")

    def set_been_here(self, status: bool) -> None:
        self.been_here = status
        
    def get_been_here(self) -> bool:
        return self.been_here

    def set_is_fighting(self, status: bool) -> None:
        self.is_fighting = status

    def get_is_fighting(self) -> bool:
        return self.is_fighting
    
    def __str__(self):
        return self.name

    def link_left(self, name: str, enemy, description):
        temp = Room(name, enemy, description)
        temp.right = self
        self.left = temp

    def link_right(self, name: str, enemy, description):
        temp = Room(name, enemy, description)
        temp.left = self
        self.right = temp

    def link_up(self, name: str, enemy, description):
        temp = Room(name, enemy, description)
        temp.down = self
        self.up = temp

    def link_down(self, name: str, enemy, description):
        temp = Room(name, enemy, description)
        temp.up = self
        self.down = temp

    def set_is_fighting(self, boolean: bool):
        self.is_fighting = bool

def setup():
    """
    Generates 3 rooms, named room1, room2, room3 and links them together
    """
    map = Room("Room1", Enemy('Dementors', 100, "a scary monster"), "meow\n")
    map.link_left("Room2", Enemy('Basilisk', 500, "a thingy"), "meow meow")
    map.link_right("Room3", Enemy('Death Eater', 1000, "a demon"), "meow meow")
    map.link_up("Room4", Enemy('Voldemort', 5000, "a very bad guy"), "meow meow")

    return map