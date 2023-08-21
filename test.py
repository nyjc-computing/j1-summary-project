#test
# from main import game

import data
import game

# test = game.MUDGame()

    
    # try:
    #     data.start_menu()
    # except:
    #     print("Start Menu is screwed")
    # else:
    #     print("Start Menu is fine")
def test_start_room():
    try:
        test_spawn_room = data.start_room()
        if test_spawn_room.__class__.__name__ == "Room":
            print("Spawn Room is a Room Object")
        else:
            raise Exception("Spawn Room created is not a Room Object")
    except:
        raise Exception("Spawn Room function does not run.")
    else:
        print("Spawn Room instantiated with no issues.")

def test_grid():
    try:
        test_grid_obj = data.Grid(2, 2)
        print(test_grid_obj.get_position())
        
    except:
        print("Grid cannot instantiate (the function does not work).")

    
        
    
    # try:
    #     test.run()
    # except:
    #     print("The game cannot run lmao.")


test_grid()
