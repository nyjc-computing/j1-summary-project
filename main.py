# Import statements
import entities
from game import Game


LEVEL = 1

if __name__ == "__main__":
    game = Game()
    game.start()
    while not game.levelEnded:
        # TODO: Create method to initialise player

        options = game.get_options()
        choice = prompt_player(options)
        game.enter(choice)
        game.show_status()
    storyline.end()