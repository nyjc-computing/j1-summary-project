# Import statements
import Game

if __name__ == "__main__":
    game = Game()
    game.setup()
    game.welcome()
    player = create_player()
    
    while not game.over():
        # Get list of choices
        choices = game.get_choices()
        choice = get_player_choice(choices)
        game.execute(choice)


