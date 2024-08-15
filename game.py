from random import randint
import character
class Game:
    def __init__(self, name):
        self.n = 6
        self.e = 5
        self.x, self.y = 0, 0
        self.past_x, self.past_y = 0, 0
        self.enemies = {}
        self.map = [['.' for i in range(self.n)] for i in range(self.n)]
        player = character.Player(name, 10)
        
    def printmap(self):
        print(self.map)
        for i in range(self.n):
            output = ""
            for j in range(self.n):
                # output += self.map[i][j]
                print(self.map[i][j])
            #doesnt work, need to join str and class tgt another way WIP
            pass

    def random_map(self):
        #enemies
        for i in range(6):
            enemy = character.Enemy()
            co = (randint(0, self.n-1), randint(0, self.n-1))
            if not co in self.enemies.keys():
                self.enemies[co] = True
        for i in self.enemies:
            self.map[i[0]][i[1]] = enemy

    def play(self):
        self.random_map()
        while (self.x!=self.n-1 and self.y!=self.n-1):
            move = input()
            if move=='w' and self.x > 0:
                self.past_x, self.past_y = self.x, self.y
                self.x-=1
            elif move=='a' and self.y > 0:
                self.past_x, self.past_y = self.x, self.y
                self.y+=1
            elif move=='s' and self.x < self.n:
                self.past_x, self.past_y = self.x, self.y
                self.x-=1
            elif move=='d' and self.y < self.n:
                self.past_x, self.past_y = self.x, self.y
                self.y-=1
            else:
                print("Invalid Move!")
                continue
            self.printmap()
            if ((self.x, self.y) in self.enemies):
                print("The ememy has been summoned!")
                if self.fight(self.enemies[(self.x, self.y)]):
                    self.lose()
                    return
        self.win()
        return
    def update_position(self):
        self.map[self.y][self.x], self.map[self.past_y][self.past_x] = "P", "X"

    def fight(self, enemy):
        return False

    def win(self):
        print("You have arrived safely. Well done!")
        
    def lose(self):
        print("Game over")
