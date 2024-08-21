
# Import statements
#main game loop

import time, character, intro, game
import rng

def main():
    # Board = game.Game("Jian Lin")
    # Board.random_map()
    # Board.printmap()
    # while True:
    #     Board.player_input()
    #     Board.update_position()
    #     Board.printmap()
    #     Board.check_event()
    player = character.Player("Test")
    print(player.gears)
    print(player.store)
if __name__ == "__main__":
    main()
    
