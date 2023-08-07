

import map.py

class game:
    def __init__(self):
        self.end = False
        self.room = map.py.setup()

    def run(self):
        # start of the game
        print('Welcome to Hogwarts School of Witchcraft and Wizardry\n')
        name = input('Key in what do you wish to be named: ')
        print(f'\nWelcome {name}, in this game you can either move (up, down, left, right), attack or use objects\n')
        decision = input('Do you wish to enter the school? (y/n): ')
        if decision == "n":
            self.end = True
    

    def start_game(self):
        # ask user for input (go left right up down) (use item) (attack)
        print(f'#############   {self.room.name}   #############')

        # prints which rooms are available to move to
        available = []
        for direction in ('left', 'right', 'up', 'down'):
            if getattr(self.room, direction) != None:
                available.append(direction)
        
        # ask for movement
        print('This room is currently connected to ')
        for i in available:
            print(f'{i} ')
        movement = input('Which direction do you wish to move in? (up, down, left, right): ')
        while movement not in available:
            input('Which direction do you wish to move in? (up, down, left, right): ')