import random
import data
class MUDGame:
    def __init__(self):
        # self.spawn = Room('home', up='closed')
        self.boss = data.spawn_boss()
        self.current_room = data.start_room()
        self.gameOver = False
    
    def run(self):
        data.start_menu()
        character = data.choose_character()
        if character.lower() == 'freddy':
            player = Freddy()
        while not self.gameOver:
            self.current_room.display()
            while not self.current_room.encounter():
                self.current_room.prompt_movement()
                if self.current_room.grid.position == []:
                    
                
                
            # display current status
            # prompt player for action
            # validate action
            # update game attributes
            # check game over
            #if self.boss.isDead():
                #self.gameOver = True
                #print('Congratulations!')
            


# class Room:
#     def __init__(self, type, row = 2, column = 2, up = None, down = None, left = None, right = None, number = 0):
#         #current room attributes
#         self.current = type
#         #next rooms
#         self.up = up
#         self.down = down 
#         self.right = right
#         self.left = left
#         self.count = number
        
#         connections = random.randint(1, 3)
#         next_rooms = [self.up, self.down, self.left, self.right]
#         for room in next_rooms:
#             if room != None:
#                 next_rooms.remove(room)
#         while connections != 0:
#             next_room = random.randint(0, 2)
#             next_rooms[next_room] = 'closed'
#             next_rooms.remove(next_room)
#             connections = connections - 1
#     def nextRoom(self, next : str):
#         if next.lower() == 'w':
#             if self.up == None:
#                 print('It seems that this door is locked.')
#             else:
#                 prev = self
#                 self.up = Room('creature', up = prev, number=countRoom())
#                 self = self.up
#         if next.lower() == 's':
#             if self.down == None:
#                 print('It seems that this door is locked.')
#             else:
#                 prev = self
#                 self.down = Room('creature', down = prev, number=countRoom())
#                 self = self.down
#         if next.lower() == 'a':
#             if self.left == None:
#                 print('It seems that this door is locked.')
#             else:
#                 prev = self
#                 self.left = Room('creature', right = prev, number=countRoom())
#                 self = self.left
#         if next.lower() == 'd':
#             if self.right == None:
#                 print('It seems that this door is locked.')
#             else:
#                 prev = self
#                 self.right = Room('creature', left = prev, number=countRoom())
#                 self = self.right

#    def countRoom(self):
#        return self.count + 1
#    
#    def has_door(self):
#
#class Grid:
#    def __init__(self):
#        self.grid = [{0:None, 1:None, 2:'creature'}]
#        self.encounter = False
#
#    def encounter(self):
#        self.encounter = True