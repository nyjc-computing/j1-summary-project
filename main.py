# Import statements
#main game loop

import time, character, intro, game, item
import rng




def main():
    print("Wake up, WAKE UP! How much longer are you going to sleep!")
    time.sleep(1)
    print("Good, now that you finally woken up, tell me, what is your name?")
    name = input("\nWhat is your name?")
    time.sleep(1)
    print("\nwell, i dont care what your name is")
    print("now go grab this wooden sword and go beat this dungeon or whatever, i literally dont care")
    time.sleep(2)
    Board = game.Game("Jian Lin")
    Board.random_map()
    Board.printmap()
    while True:
        Board.player_input()
        Board.update_position()
        Board.printmap()
        Board.check_event()

if __name__ == "__main__":
    main()
