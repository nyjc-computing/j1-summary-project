#File containing the code for the game
import data

class MUDGame:
    def __init__(self):
        self.gameover = False # default
        self.won = False # default
        
    
    def run(self):
        """
- initiating the game
- interaction between steve and creatures --> what kind of creature, what kind of battle do you want
- how the turns work --> when to move steve, when to move the monster
- winscreen
- losescreen + lose conditions
- 
        """
        maze = Labyrinth()
        start = maze.generate()
        