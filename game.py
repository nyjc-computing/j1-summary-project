from map import Room, setup
from character import Character

class Game:
    '''a class that runs when the game runs

    attributes
    ----------
    end : True when game ends, False otherwise
    room : class for monster in the room and rooms it is connected to (refer to map.py)
    character : class for the character (refer to character.py)

    methods
    -------
    intro() : runs when the game starts for the first time
    run() : runs everytime the character choose an option
    move() : method for character to traverse to different rooms
    attack() : method for character to attack enemy and vise versa
    while_fighting() : runs when character is in a fight, disabling move option
    use_item(): method for character to use item
    '''
    

    
    def __init__(self):
        self.end = False
        self.room = setup()
        self.character = Character()
        
    def intro(self):
        # start of the game
        print('Welcome to Hogwarts School of Witchcraft and Wizardry\n')
        self.character.name = input('Key in what you wish to be named: ')
        print(f'\nWelcome {self.character.name}, in this game you can either move (up, down, left, right), attack or use objects\n')
        decision = input('Do you wish to enter the school? (y/n): ')
        if decision == "n":
            self.end = True
    

    def run(self):
        # if character is not fighting
        if not self.room.get_is_fighting():
            # ask user for input (go left right up down) (use item) (attack)
            print(f'\n=========================\n        {self.room.name}\n=========================\n')

            # if charcter have not been here print description
            if not self.room.get_been_here():
                print(self.room.description)
                #print("\n")
    
            # prints which rooms are available to move to
            available = []
            for direction in ('left', 'right', 'up', 'down'):
                if getattr(self.room, direction) != None:
                    available.append(direction)
            for i in available:
                print(f'To the {i} is {getattr(self.room, i)}')
    
            # ask for input if have monster
            if self.room.enemy.get_health() != 0 or None:
                #print(f'\nROAR!!! {self.room.enemy}, {self.room.enemy.description} is in the room')
                # change available moves respectively
                available_moves = ['attack']
                decision = input('\nWhat do you wish to do? (attack): ')
                while decision not in available_moves:
                    decision = input('\nWhat do you wish to do? (attack): ')
    
            # ask for input if character have gone to this room and monster is dead
            else:
                available_moves = ['move']
                decision = input('\nWhat do you wish to do? (move): ')
                while decision not in available_moves:
                    decision = input('\nWhat do you wish to do? (move): ')
            
            # if input = movement, ask for direction
            if decision == 'move':
                self.move(available)
    
            # if input = attack, deal damage to monster for the first time
            elif decision == 'attack':
                self.attack(self.character, self.room.enemy)
                self.room.set_is_fighting(True)
                # deal damage back to character if enemy is not dead
                if not self.room.enemy.is_dead():
                    self.attack(self.room.enemy, self.character)
                    
                # if enemy is dead drop loot
                else:
                    self.character.item += self.room.enemy.loot
           
        # if character is in the middle of fighting
        else:
            self.while_fighting()

        # check if game is over
        if self.character.is_dead():
            print('\nHogwarts is not a school for the weak. Return when you are stronger')
            print('\nGAME OVER')
            self.end = True
        

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
        victim.set_health(-attacker.battle_points)

        if  not victim.is_dead(): 
            # print health of enemy
            print(f'\n{attacker} has dealt {attacker.battle_points} damage to {victim.name}. {victim} still have {victim.get_health()} health')

        else:
            # if victim is dead
            print(f'{attacker} dealt {attacker.battle_points} damage to {victim.name}. {victim} is now dead')
            self.room.is_fighting = False
            

    def while_fighting(self):
        print(f'\n{self.room.enemy} currently has {self.room.enemy.get_health()} health')
        available = ['attack']
        decision = input('What do you wish to do? (attack): ')
        # check for valid response
        while decision not in available:
            decision = input('What do you wish to do? (attack): ')
        if decision == 'attack':
            self.attack(self.character, self.room.enemy)
    
    def use_item(self):
        print('\nWhich of the following item do you wish to use? :')
        for i, item in enumerate(self.character.item):
            print(f"[{i}]: {item}")
        choice = input("Choose an item: ")
        while choice not in [str(x) for x in range(1, len(self.character.item)+1)]:
            print("Invalid Choice")
            choice = input("Choose an item: ")
        
        