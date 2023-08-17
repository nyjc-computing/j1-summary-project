import game
import data

class Test:
    def __init__(self):
        pass

    def valid_move(self, path, location):
        if path not in roompaths[location]:
            print('Invalid move')
            return False
        else:
            return True

    def player_presence(self, location):
        if location not in map:
            return False
        else:
            return True

    def end_state(self, player_hp):
        if player_hp < 300:
            return True
        else:
            return False
    
'how write test without data structure'
'what do i even test'