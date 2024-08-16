# Import statements
import entities
from game import Game


LEVEL = 1

if __name__ == "__main__":
    game = Game()
    game.start()
    while not game.levelEnded:
        storyline.doIntro()
        name = input("Brave adventurer! What is your name?")
        # TODO: Create method to initialise player
        game.player = entities.Player(name, 100, 100, game.currentTilePos)
        options = game.get_options()
        choice = prompt_player(options)
        game.enter(choice)
        game.show_status()
    storyline.end()