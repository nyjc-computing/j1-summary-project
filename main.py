from game import Game

if __name__ == "__main__":
    game = Game()
    game.start()

    while not game.game_over():
        choice = game.options()
        game.do(choice) 