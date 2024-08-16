import data, interface, battle, time

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
        choice = self.interface.func_map[self.get_now_room_name()]()
        print(choice)
        if choice == 'Move to next room':
            self.next_room()
        elif choice == 'Move to previous room':
            self.prev_room()
        elif choice == 'Look around':
            print("YOU FOUND ENEMIES!!!!")
            combat = battle.Battle(self.player, self.get_now_room())
            i = 0
            while combat.battle_over() is False:
                if i % 2 == 0:
                    combat.player_attack()
                elif i % 2 == 1:
                    combat.enemy_attack()
                    self.interface.combat_menu(self.player.get_health(), self.get_now_room().get_enemies()[0].get_health())
                i += 1
            print(self.get_now_room().get_enemies())
        else:
            print("Invalid choice")
        print()

