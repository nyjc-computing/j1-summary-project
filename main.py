# Import statements

import random
import item
import character

import time, character, intro, game
import rng



def main():
    Board = game.Game(player.name)
    Board.random_map()
    Board.printmap()
    while True:
        Board.player_input()
        Board.update_position()
        Board.printmap()
        Board.check_event()


if __name__ == "__main__":
    main()
