import data, interface

class Game:
    def __init__(self):
        self.interface = None
        self.player = None
        self.princess = None
        self.rooms = []
        self.now = 0
        

    def setup(self):
        self.interface = interface.Interface()
        self.player = data.createPlayer()
        self.princess = data.createPrincess()
        self.rooms = data.createRooms()
        if self.interface.start_menu() == 'exit':
            print("Exiting game...")
            exit()
        

    def isover(self):
        return self.player.isdead() or self.princess.isdead()

    def next_room(self):
        if self.now < len(self.rooms) - 1:
            self.now += 1
            
    def prev_room(self):
        if self.now > 0:
            self.now -= 1
    
    def get_now_room(self):
        return self.rooms[self.now]

    def get_now_room_name(self):
        return self.rooms[self.now].get_name()
        
    def get_next_room_name(self):
        if self.now < len(self.rooms) - 1:
            return self.rooms[self.now + 1].get_name()
        else:
            return "WALL"
    
    def get_prev_room_name(self):
        if self.now - 1 >= 0:
            return self.rooms[self.now - 1].get_name()
        else:
            return "WALL"

    def get_choice(self):
        "Dispalys and gets player choice. Display results afterwards"
        print("Now:", self.get_now_room_name())
        print("Next:", self.get_next_room_name())
        print("Prev:", self.get_prev_room_name())
        self.interface.func_map[self.get_now_room_name()]()
        choice = input("Enter choice: ")
        if choice == '2':
            self.next_room()
        elif choice == '3':
            self.prev_room()
        elif choice == '1':
            print("YOU FOUND ENEMIES!!!!")
            
        else:
            print("Invalid choice")
        print()

