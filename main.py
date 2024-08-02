# Import statements
from ctps import *


if __name__ == "__main__":
    game = Game()
    game.setup()
    for i in range(5):
        game.get_choice()
        game.next_room()

    print(game.isover())
