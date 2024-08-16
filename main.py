# Import statements
import ctps


if __name__ == "__main__":
    game = ctps.Game()
    game.setup()

    for i in range(10):
        game.get_choice()
        
    print(game.isover())
