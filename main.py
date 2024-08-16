# Import statements
import ctps


if __name__ == "__main__":
    game = ctps.Game()
    game.setup()

    for i in range(10):
        print("Now:", game.get_now_room().enemies)
        print("Next:", game.get_next_room())
        print("Prev:", game.get_prev_room())
        game.get_choice()
        
    print(game.isover())
