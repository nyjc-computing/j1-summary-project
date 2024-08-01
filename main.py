from game import Game # IMPORT GAME

if __name__ == "__main__":
    game = Game()
    game.start()

    while not game.game_over():
        choice = game.options()
        game.do(choice) 
