
# Import statements
#main game loop

import time, character, intro, game
import rng

def main():
    Board = game.Game("Jian Lin")
    Board.random_map()
    Board.printmap()
if __name__ == "__main__":
    main()
    
