from random import randint
import character, colorama
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

    def random_map(self): #randomise events in map
        #enemies
        self.map[0][0] = self.player
        for i in range(self.e):
            while True:
                coords = (randint(0, self.n-1), randint(0, self.n-1))
                if self.map[coords[0]][coords[1]] == "." and not coords in self.enemies.keys():
                    self.enemies[coords] = True
                    break
        for i in self.enemies:
            self.map[i[0]][i[1]] = character.Enemy()

    def play(self):
        while True: #check doesnt work fix this shit
            move = input("Enter move: ")
            if move=='w' and self.player.coords[0] > 0:
                self.player.last_move = self.player.coords
                self.player.coords =(self.player.coords[0] - 1, self.player.coords[1])
                break
            elif move=='a' and self.player.coords[1] > 0:
                self.player.last_move = self.player.coords
                self.player.coords =(self.player.coords[0], self.player.coords[1] - 1)
                break
            elif move=='s' and self.player.coords[0] < self.n:
                self.player.last_move = self.player.coords
                self.player.coords =(self.player.coords[0] + 1, self.player.coords[1])
                break
            elif move=='d' and self.player.coords[1] < self.n:
                self.player.last_move = self.player.coords
                self.player.coords =(self.player.coords[0], self.player.coords[1] + 1)
                break
            else:
                print("Invalid Move!")
                
    
    def update_position(self):
        self.map[self.player.coords[0]][self.player.coords[1]] = self.player
        self.map[self.player.last_move[0]][self.player.last_move[1]] = "X"

    def fight(self, enemy):
        return False

    def win(self):
        print("You have arrived safely. Well done!")
        
    def lose(self):
        print("Game over")
