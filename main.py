
# Import statements
import ctps


if __name__ == "__main__":
    player = create_player()
    game = Game()
    game.setup()
    while not game.over():
        # get list of choices
        choices = game.get_choices()
        choice = get_player_choice(choices)
        game.execute(choice)
