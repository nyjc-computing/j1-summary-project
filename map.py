class Room:
    """This class stores the rooms and the rooms connected to it

    Attributes
    ----------
    + name: str
    + enemy: str
    + left: str
    + right: str
    + up: str
    + down: str

    Methods
    -------
    nil?
    """
    
    def __init__(self, name: str):
        self.name = name
        self.enemy = None
        self.left = None
        self.right = None
        self.up = None
        self.down = None

    def __repr__(self):
        print(f"Room({self.name})")

    def link_left(self, name: str):
        self.left = name

    def link_right(self, name: str):
        self.right = name

    def link_up(self, name: str):
        self.up = name

    def link_down(self, name: str):
        self.down = name

def setup():
    """
    Generates 3 rooms, named room1, room2, room3 and links them together
    """
    map = Room("room1")
    map.left = Room("room2")
    map.up = Room("room3")
    return map