from enemy import Enemy

class Room:
    
    def __init__(self, name: str):
        self.name = name
        self.enemy = None
        self.left = None
        self.right = None
        self.up = None
        self.down = None

    def __repr__(self):
        print(f"Room({self.name})")

    def __str__(self):
        return self.name

    def link_left(self, name: str):
        temp = Room(name)
        temp.right = self
        self.left = temp

    def link_right(self, name: str):
        temp = Room(name)
        temp.left = self
        self.right = temp

    def link_up(self, name: str):
        temp = Room(name)
        temp.down = self
        self.up = temp

    def link_down(self, name: str):
        temp = Room(name)
        temp.up = self
        self.down = temp

def setup():
    """
    Generates 3 rooms, named room1, room2, room3 and links them together
    """
    map = Room("Room1")
    map.link_left("Room2")
    map.link_right("Room3")
    map.link_up("Room4")
    boss = Enemy('Voldemort')
    big_enemy = Enemy('Death Eater')
    medium_enemy = Enemy('Basilisk')
    small_enemy = Enemy('Dementors')

    enemies = [{'room': 'Room1', 'enemy': small_enemy}, {'room': 'Room2', 'enemy': boss}, {'room': 'Room3', 'enemy': big_enemy}, {'room': 'Room4', 'enemy': medium_enemy}]

    boss = Enemy('Voldemort')
    big_enemy = Enemy('Death Eater')
    medium_enemy = Enemy('Basilisk')
    small_enemy = Enemy('Dementors')

    return [map, enemies]