#File containing the code for the game
import data
import random



class MUDGame:
    def __init__(self):
        self.gameover = False # default
        self.won = False # default
        maze = Labyrinth()
        maze.generate()
        steve = Steve()

    
    def introduce(self): 
        """
        Starting interface of the game
        """
        username = input('Enter your username:')
        print(f'{username}, OH NO YOU ARE TRAPPED! \nYou will go through a series of rooms that may give you items or have ANGRY creatures wanting you DEAD :P \nKill them all, especially the boss to escape! \nGOOD LUCK ;D')




    
    def encounter(creature):
        """
        Options when encountering creatures
        """
        option = None
        while option == None:
            # loop to prompt valid input
            print(f'You have encountered {creature}! \nDo you want to attack or escape?')
            print('1. Attack \n2. Escape')
            option = input('Your choice:')
            if option == 1:
                # player choose to attack creature
                pass
            elif option == 2:
                # player choose to escape
                chance = random.randint(1, 2)
                if chance == 1:
                    # player escapes
                    pass
                else:
                    # player failed to escape
                    # player receive damage
                    pass
            else:
                option = None

    
                    
                
            
    
    def run(self):
        """
- initiating the game
- interaction between steve and creatures --> what kind of creature, what kind of battle do you want
- how the turns work --> when to move steve, when to move the monster
- winscreen
- losescreen + lose conditions
- 
        """
        self.introduce()
        while not self.gameover():
            self.show_status()
            # show status
            self.show_options()
            # show player action options
            choice = self.prompt_player()
            # prompt player to take actions
            self.validate(choice)
            # validate choice
            self.do_action()
            self.update()
            # update
            
            


