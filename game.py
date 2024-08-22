import random
import character, sys, item
import time

class Game:
    def __init__(self, name):
        self.n = 5 #length of sides of grid
        self.e = 12 #num of enemies
        self.map = [['.' for i in range(self.n)] for i in range(self.n)]
        self.player = character.Player(name)

    def printmap(self):
        print("\n-----\nMap\n\n")
        for i in range(self.n):
            output = ""
            for j in range(self.n):
                output += str(self.map[i][j])+" "
            print(output)
        print(f"Current Event:{self.player.event_queue}")#type(self.player.event_queue))
        print("-----\n")
        

    def random_map(self): #randomise events in map
        #player spawn
        self.map[0][0] = self.player
        #boss spawn
        while True:
            coords = (random.randint(0, self.n-1), random.randint(0, self.n-1))
            if self.map[coords[0]][coords[1]] == ".":
                self.map[coords[0]][coords[1]] = character.Boss(["Overlord", 125, 5, 10, 0.5]) #change values as needed
                break
        #enemies spawn
        for i in range(self.e):
            while True:
                coords = (random.randint(0, self.n-1), random.randint(0, self.n-1))
                if self.map[coords[0]][coords[1]] == ".":
                    self.map[coords[0]][coords[1]] = character.Enemy(["Enemy", random.randint(20, 50), random.randint(0, 5), random.randint(3, 8), 1])
                    break

    def help_cmds(self):
        return "-----\nMovement\n\n'w'\n'a'\n's'\n'd'\n-----\nActions\n\n'trash' (remove item from inventory)\n'equip'\n'unequip'\n'use'\n'stats'\n''map''\n'-----\nInfo\n\n'inventory'\n'gears''\n'It is highly recommended that you get good gears before challenging the boss, otherwise you will lose."
        
    def player_input(self):
        while True:
            move = input("Enter move or 'help' to view all commands: ")
            if move=="help":
                print(self.help_cmds())
            elif move=="inventory":
                self.player.display_inv()
            elif move=="gears":
                self.player.display_gears()
            elif move=="stats":
                self.player.stats()
            elif move=="map":
                self.printmap()
            elif move=="use":
                if item.life_crystal.name not in self.player.items:
                    print("Nothing to use")
                else:
                    self.player.display_inv()
                    thing = input("you can only use the life crystal lmao (Type):")
                    if thing == item.life_crystal.name:
                        self.player.use(item.life_crystal)
                        
            elif move=="equip":
                if len(self.player.items.keys()) > 0:
                    self.player.display_inv()
                    move2=input("Enter what to equip: ")
                    while not move2 in self.player.items.keys():
                        move2=input("Enter valid item: ")
                    self.player.equip(self.player.items[move2])
                else:
                    print("got nothing to equip lah")
            elif move=="unequip":
                self.player.display_gears()
                move2=input("Enter what section to unequip (e.g. helm, chest etc AND NOT THE NAME OF THE ITEM): ")
                while not move2 in ["helm", "chest", "leg", "boots", "weapon"]:
                    move2=input("Enter valid section: ")
                self.player.unequip(move2)
            elif move=="trash":
                if len(self.player.items.keys()) > 0:
                    self.player.display_inv()
                    move2=input("Enter what to trash: ")
                    while not move2 in self.player.items.keys():
                        move2=input("Enter valid item: ")
                    self.player.trash(self.player.items[move2])
                else:
                    print("got nothing to trash lah")
            elif move=='w' and self.player.coords[0] > 0:
                self.player.event_queue = self.map[self.player.coords[0] - 1][self.player.coords[1]]
                self.player.last_move = self.player.coords
                self.player.coords =(self.player.coords[0] - 1, self.player.coords[1])
                break
            elif move=='a' and self.player.coords[1] > 0:
                self.player.event_queue = self.map[self.player.coords[0]][self.player.coords[1] - 1]
                self.player.last_move = self.player.coords
                self.player.coords =(self.player.coords[0], self.player.coords[1] - 1)
                break
            elif move=='s' and self.player.coords[0] < self.n - 1:
                self.player.event_queue = self.map[self.player.coords[0] + 1][self.player.coords[1]]
                self.player.last_move = self.player.coords
                self.player.coords =(self.player.coords[0] + 1, self.player.coords[1])
                break
            elif move=='d' and self.player.coords[1] < self.n - 1:
                self.player.event_queue = self.map[self.player.coords[0]][self.player.coords[1] + 1]
                self.player.last_move = self.player.coords
                self.player.coords =(self.player.coords[0], self.player.coords[1] + 1)
                break
            else:
                print("Invalid move")


    def update_position(self):
        self.map[self.player.coords[0]][self.player.coords[1]] = self.player
        self.map[self.player.last_move[0]][self.player.last_move[1]] = "X"

    def check_event(self):
        if isinstance(self.player.event_queue, character.Enemy):
            print("You have encountered an enemy.")
            self.event_fight(self.player, self.player.event_queue)
        else:
            print("nothing")

    def event_fight(self, player, enemy):
        result = False
        turn_order = [player, enemy]
        if player.speed >= enemy.speed:
            i = 0
        else:
            i = 1
        while not result:
            result = turn_order[i].combat(turn_order[i - 1]) #if i = 0 i.e. player, i - 1 will become -1 which points to enemy as intended
            time.sleep(0.5)
            if i == 1:
                i = 0
            else:
                i += 1
        if result == -1: #defeat against normal enemy
            sys.exit()
        elif result == -666: #defeat against boss
            print("The final boss has killed you...")
            sys.exit()
        elif result == -888: #win against boss
            print("The player exited the dungeon triumphantly, although that came at a cost, he has sustained fatal injuries, 1 bruise to his knee when he fell down and 3 scratch marks left by the final boss. Nevertheless, the player was happy to leave the dungeon at long last.")
            print("You WIN!!!")
            while True:
                answer = input("Enjoyed the game?? Please rate the game out of 10")
                if answer != "10":
                    print("Wrong answer, pls try again!")
                    continue
                else:
                    "Glad to hear you enjoyed the game"
                break
            print("Thanks for playing!")
            sys.exit()
        elif result == True: #win against normal enemy
            print("\n")
            self.player.health = self.player.max_health
            x = random.randint(1,10)
            if x <= 5:
                reward = random.choice(item.loot_table[0:5])
            elif 5 < x <= 9:
                reward = random.choice(item.loot_table[5:12])
            else:
                reward = random.choice(item.loot_table[12:])
            print(f"You have obtained {reward}")
            self.player.store(reward)
