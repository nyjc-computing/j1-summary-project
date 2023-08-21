import game
import data
class Test:
    def __init__(self):
        pass

<<<<<<< HEAD
    
=======
    def valid_move(self, path, location):
        '''According to the UI this test is useless'''
        if path not in roompaths[location]:
            print('Invalid move')
            return False
        else:
            return True

    def player_presence(self, location):
        '''According to the fact that spawn is fixed and the UI doesnt allow you to move anywhere but map locations this test is also useless'''
        if location not in map:
            return False
        else:
            return True

    def end_state(self, player_hp):
        '''The game has its own test for the end so this is also useless'''
        if player_hp < 300:
            return True
        else:
            return False

'in summary my game programmer made this thing so idiot proof that i dont actually know how or what to write test cases for'
>>>>>>> main
def valid_move(self, path, location):
        '''According to the UI this test is useless'''
        if path not in roompaths[location]:
            print('Invalid move')
            return False
        else:
            return True

    def player_presence(self, location):
        '''According to the fact that spawn is fixed and the UI doesnt allow you to move anywhere but map locations this test is also useless'''
        if location not in map:
            return False
        else:
            return True

    def end_state(self, player_hp):
        '''The game has its own test for the end so this is also useless'''
        if player_hp < 300:
            return True
        else:
            return False

'in summary my game programmer made this thing so idiot proof that i dont actually know how or what to write test cases for'    def valid_move(self, path, location):'''According to the UI this test is useless'''
        if path not in roompaths[location]:
            print('Invalid move')
            return False
        else:
            return True

    def player_presence(self, location):
        '''According to the fact that spawn is fixed and the UI doesnt allow you to move anywhere but map locations this test is also useless'''
        if location not in map:
            return False
        else:
            return True

    def end_state(self, player_hp):
        '''The game has its own test for the end so this is also useless'''
        if player_hp < 300:
            return True
        else:
            return False

'in summary my game programmer made this thing so idiot proof that i dont actually know how or what to write test cases for    
'how write test without data structure'
'what do i even test'