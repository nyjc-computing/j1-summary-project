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
        print(f'\n=========================\n        {self.room.name}\n=========================\n')

        # prints which rooms are available to move to
        available = []
        for direction in ('left', 'right', 'up', 'down'):
            if getattr(self.room, direction) != None:
                available.append(direction)
        for i in available:
            print(f'To the {i} is: {getattr(self.room, i)}')

        # ask for input if have monster
        if not self.room.been_here:
            print(f'\nROAR!!! {self.room.enemy} is in the room')
            decision = input('\nWhat do you wish to do? (move, attack): ')

        # ask for input if character have gone to this room and monster is dead
        else:
            decision = input('\nWhat do you wish to do? (move): ')

        # if input = movement, ask for direction
        if decision == 'move':
            self.move(available)

        # if input = attack, deal damage to monster
        elif decision == 'attack':
            self.attack(self.character, self.room.enemy)

    def move(self, available):
        movement = input('\nWhich direction do you wish to move in? (up, down, left, right): ')
        while movement not in available:
            movement = input('Which direction do you wish to move in? (up, down, left, right): ')

        # if input = movement, move in direction
        for direction in ('left', 'right', 'up', 'down'):
            if movement == direction:
                self.room = getattr(self.room, direction)
    
    def attack(self, attacker, victim):
        # reduce enemy health base on battle point of character
        victim.set_health(attacker.battle_points)

        if  not victim.is_dead(): 
            # print health of enemy
            print(f'You dealt {attacker.battle_points} damage to {victim.name}. Enemy still have {victim.get_health()} health')

        else:
            # if victim is dead
            print(f'You dealt {attacker.battle_points} damage to {victim.name}. Enemy is now dead')

    def use_item(self):
        pass