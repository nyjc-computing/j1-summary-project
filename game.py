from random import randint
import character, sys
class Game:
    def __init__(self, name):
        self.n = 5
        self.e = 12
        self.enemies = {}
        self.map = [['.' for i in range(self.n)] for i in range(self.n)]
        self.player = character.Player(name)
        
    def printmap(self):
        for i in range(self.n):
            output = ""
            for j in range(self.n):
                output += str(self.map[i][j])
            print(output)
        print("\n")
        print(f"Current Event:{self.player.event_queue}", type(self.player.event_queue))

    def random_map(self): #randomise events in map
        #player spawn
        self.map[0][0] = self.player
        #boss spawn
        while True:
            coords = (randint(0, self.n-1), randint(0, self.n-1))
            if self.map[coords[0]][coords[1]] == ".":
                self.map[coords[0]][coords[1]] = character.Boss(["Overlord", 1, 5, 3, 1])
                break
        #enemies spawn
        for i in range(self.e):
            while True:
                coords = (randint(0, self.n-1), randint(0, self.n-1))
                if self.map[coords[0]][coords[1]] == "." and not coords in self.enemies.keys():
                    self.enemies[coords] = True
                    break
        for i in self.enemies:
            self.map[i[0]][i[1]] = character.Enemy(["Enemy", 5, 1, 1, 1]) #enter value next time

    def player_input(self):
        while True:
            move = input("Enter move: ")
            if move=='w' and self.player.coords[0] > 0:
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
            elif not move in ["w", "a", "s", "d"]:
                print("Invalid move")
            else:
                print("You've reached the end of the dungeon")
                
    
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
            if i == 1:
                i = 0
            else:
                i += 1
        if result == -1:
            sys.exit()
        elif result == -666:
            print("The final boss has killed you...")
            sys.exit()
        elif result == -888:
            print("You have defeated the final boss")
            sys.exit()
        
            
            
        
