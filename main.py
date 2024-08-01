# Import statements
import mud

import data

if __name__ == "__main__":
    game = mud.Game()
    mud.welcome()
    players = mud.init_players()
    # Game loop
    while not game.is_gameover():
        ...
    game.epilogue()