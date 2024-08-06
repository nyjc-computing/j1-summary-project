import data

class Game:
    def __init__(self):
        self.player = None
        self.princess = None
        self.rooms = []
        self.now = 0

    def setup(self):
        self.player = data.createPlayer()
        self.princess = data.createPrincess()
        self.rooms = data.createRooms()

    def isover(self):
        return self.player.isdead() or self.princess.isdead()

    def next_room(self):
        if self.now < len(self.rooms):
            self.now += 1
            
    def get_next_room(self):
        return self.rooms[(self.now + 1) % 5].get_name()
        
    def prev_room(self):
        if self.now > 0:
            self.now -= 1
    
    def get_prev_room(self):
        return self.rooms[(self.now - 1) % 5].get_name()
    
    def get_now_room(self):
        return self.rooms[self.now].get_name()
    
    # def get_choice(self):
    #     now_room = self.get_now_room()
    #     choices = ["Look around"]
    #     if now_room != "Bedroom":
    #         choices.append(f"Next room: {self.get_next_room()}")
    #     if now_room != "Dungeon":
    #         choices.append(f"Previous room: {self.get_prev_room()}")

    #     print(f"You are in {self.get_now_room()}")
    #     print("-choices-")
    #     for num, choice in enumerate(choices):
    #         print(f"{num+1}. {choice}")

