from character import *

class Game:
    def __init__(self):
        self.player = None
        self.princess = None
        self.rooms = []
        self.now = 0

    def setup(self):
        self.player = Player(1, 1, [])
        self.rooms.append(Bedroom())

    def isdead(self):
        return self.player.isdead()

    def isover(self):
        return self.isdead()



    def next_room(self):
        self.now += 1
    

