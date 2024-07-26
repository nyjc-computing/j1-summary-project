
if __name__ == "__main__":
     game = Game()
    player = create_player()
    
    while not game.game_over():
        options = game.options()
        choice = choose_option(options)
        game.do(choice)
        game.display()
        