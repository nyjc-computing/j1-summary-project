from game import Game

if __name__ == "__main__":
    game = Game()
    game.start()

    while not game.game_over():
        options = game.options()
        choice = game.choose_option(options) 
        if choice is not None:
            game.do(choice) 
        else:
            print("Invalid choice. Please try again.")