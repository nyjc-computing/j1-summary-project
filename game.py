

import room.py

class game:
    def __init__(self):
        raise NotImplementedError

def run():
    # start of the game
    print('Welcome to Hogwarts School of Witchcraft and Wizardry\n')
    name = input('Key in what do you wish to be named: ')
    print(f'\nWelcome {name}, in this game you can either move (up, down, left, right), attack or use objects\n')
    decision = input('Do you wish to enter the school? (y/n): ')
    while decision != 'y':
        decision = input('\nDo you wish to enter the school? (y/n): ')

def start_room():
    # ask user for input (go left right up down) (use item) (attack)
    