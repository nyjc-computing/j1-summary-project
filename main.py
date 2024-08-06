# Import statements
from ctps import *


if __name__ == "__main__":
    game = Game()
    game.setup()
    for i in range(5):
        print(game.get_now_room())
        game.next_room()

    print(game.isover())