# Import statements
import entities
from game import Game
from time import sleep
if __name__ == "__main__":

    game = Game()
    game.start()
    while not game.win() and not game.lose():
        
        x = 'invalid'
        while x == 'invalid':
            game.show_status()
            options = game.get_options()
            choice = game.prompt_player(''.join(options))
            x = game.enter(choice)
            if x == 'invalid':
                sleep(1)
                print("\033c", end="", flush=True)
            
        
        print("\033c", end="", flush=True)
        
    if game.win():
        print("You win")
    else:
        print("You Lose")
        
            
