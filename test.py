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

'''
===============================================
Test the Normal Room and Grid class for errors.
===============================================
'''
# test_grid = data.Grid("normal", 2, 2)
# test_room = data.Room()
        
# try:
    
#     if test_room.grid.get_position() != [2, 2]:
#         print("Grid positioning does not work properly.")
#     else:
#         print("Grid position is ok.")
    
# except:
#     print("Grid cannot instantiate (the function does not work).")
# test_room.grid.move([0,0])

# for x in range(0, 5):
#     for y in range(0, 5):
#         pos = [x, y]
#         print(pos)
#         try:
#             if test_room.grid.is_encounter():
#                 print(test_room.grid.get_enemies())
#         except:
#             print("is_encounter() does not work")
#         test_room.grid.move(pos)

# test_room.next_room('w')

# print("Room and Grid instantiated with no issues.")





'''
========================================
Test the start_room function for errors.
========================================
'''

# try:
#     test_spawn_room = data.start_room()
#     if test_spawn_room.__class__.__name__ == "Room":
#         print("Spawn Room is a Room Object")
#     else:
#         raise Exception("Spawn Room created is not a Room Object")
# except:
#     raise Exception("Spawn Room function does not run.")
# else:
#     print("Spawn Room instantiated with no issues.")



'''
==================================================
Test the Grid class for errors.
==================================================
'''

# try:
#     test_grid_obj = data.Grid(2, 2)
    
#     if test_grid_obj.get_position() != [2, 2]:
#         print("Grid positioning does not work properly.")
#     else:
#         print("Grid position is ok.")
    
# except:
#     print("Grid cannot instantiate (the function does not work).")
# test_grid_obj.move([0,0])

# for x in range(0, 5):
#     for y in range(0, 5):
#         pos = [x, y]
#         print(pos)
#         try:
#             if test_grid_obj.is_encounter():
#                 print(test_grid_obj.get_enemies())
#         except:
#             print("is_encounter() does not work")
#         test_grid_obj.move(pos)

# print("Grid instantiated with no issues.")


        
        
test_freddy = data.Freddy()
test_enemy = data.GB()
while test_enemy.is_defeated() == False:
    test_freddy.attack(test_enemy, 1)
    test_freddy.attack(test_enemy, 2)
    test_freddy.attack(test_enemy, 3)
        
    
    # try:
    #     test.run()
    # except:
    #     print("The game cannot run lmao.")

