# Import statements
import ctps


if __name__ == "__main__":
    game = ctps.Game()
    game.setup()
    
    for i in range(10):
        print("Now:", game.get_now_room())
        print("Next:", game.get_next_room())
        print("Prev:", game.get_prev_room())
        if input():
            game.next_room()
        else:
            game.prev_room()
        
    print(game.isover())

