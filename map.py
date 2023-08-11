class Room:
    """
    This class encapsulates data for 
    """
    def __init__(self, name):
        self.name = name
        self.enemy = None
        self.left = None
        self.right = None
        self.up = None
        self.down = None

    def __repr__(self):
        print(f"Room({self.name})")

def setup():
    map = Room("room1")
    map.left = Room("room2")
    map.up = Room("room3")
    return map