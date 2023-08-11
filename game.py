from map import Room, setup

class game:
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

    def intro(self):
        # start of the game
        print('Welcome to Hogwarts School of Witchcraft and Wizardry\n')
        name = input('Key in what do you wish to be named: ')
        print(f'\nWelcome {name}, in this game you can either move (up, down, left, right), attack or use objects\n')
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
        
        # ask for movement
        print('This room is currently connected to: \n')
        for i in available:
            print(f'{i} ')
        decision = input('\nWhich direction do you wish to move in? (up, down, left, right): ')
        while decision not in available:
            decision = input('Which direction do you wish to move in? (up, down, left, right): ')

        # if input = movement
        for direction in ('left', 'right', 'up', 'down'):
            if decision == direction:
                self.room = getattr(self.room, direction)