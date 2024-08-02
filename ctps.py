from character import *
from room import *

class Game:
    def __init__(self):
        self.player = None
        self.princess = None
        self.rooms = []
        self.now = 0

    def setup(self):
        self.player = Player(1, 1, [])
        self.princess = Princess(1, 1)
        self.rooms.append(Room("Bedroom", 3))

    def isover(self):
        return self.player.isdead() or self.princess.isdead()

    def next_room(self):
        self.now += 1
    

