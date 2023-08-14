from map import Room, setup
from character import Character

class Game:
    '''a class that runs when the game runs

    attributes
    ----------
    end : True when game ends, False otherwise
    room : 

    methods
    -------
    run() : runs when the game starts for the first time
    start_game() : runs everytime the character choose an option
    '''
    

    
    def __init__(self):
        self.end = False
        self.room = setup()
        self.character = Character()
    def intro(self):
        # start of the game
        print('Welcome to Hogwarts School of Witchcraft and Wizardry\n')
        self.character.name = input('Key in what do you wish to be named: ')
        print(f'\nWelcome {self.character.name}, in this game you can either move (up, down, left, right), attack or use objects\n')
        decision = input('Do you wish to enter the school? (y/n): ')
        if decision == "n":
            self.end = True
    

    def run(self):
        # ask user for input (go left right up down) (use item) (attack)
        print(f'\n#############   {self.room.name}   #############')

        # prints which rooms are available to move to
        available = []
        for direction in ('left', 'right', 'up', 'down'):
            if getattr(self.room, direction) != None:
                available.append(direction)
        print('This room is currently connected to: \n')
        for i in available:
            print(f'{i} ')

        # ask for input
        decision = input('\nWhat do you wish to do? (move, attack): ')

        # if input = movement, ask for direction
        if decision == 'move':
            self.move(available)

        # if input = attack, deal damage to monster
        elif decision == 'attack':
            self.attack()

    def move(self, available):
        movement = input('\nWhich direction do you wish to move in? (up, down, left, right): ')
        while movement not in available:
            movement = input('Which direction do you wish to move in? (up, down, left, right): ')

        # if input = movement, move in direction
        for direction in ('left', 'right', 'up', 'down'):
            if movement == direction:
                self.room = getattr(self.room, direction)
    
    def attack(self):
        pass