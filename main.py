if __name__ == "__main__":
    game = Game()
    game.start() # Welcomes the player, creates the map
    player = create_player()
    
    while not game.game_over():
        game.print_map()
        options = game.options() # can put into game.do()
        choice = choose_option(options)
        game.do(choice) # executes the option chosen
