# Import statements

import random
import item
import character

import time, character, intro, game
import rng

# def main():
#     yes = True
#     while True:
#         print("Intro")
#         time.sleep(1)
#         print(intro_text)
#         time.sleep(5)
#         print("You wake up, dazed, who are you again?")
#         player = classes.Player(str(input("What is your name?")))
#         while yes:
#             confirm = input(f"Are you sure your name is {player}?(y/n):")
#             if confirm == "y":
#                 yes = False
#             elif confirm == "n":
#                   player = .Player(str(input("What is your name?")))
#             else:
#                 print("Answer the question please")


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
