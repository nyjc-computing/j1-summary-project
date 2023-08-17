#File containing the code for the game
import data
import random



class MUDGame:
    """This class encapsulates data for the main game implementation."""
    def __init__(self):
        self.gameover = False # default
        self.won = False # default
        self.maze = Labyrinth()
        self.maze.generate()
        self.steve = Steve()
        self.creature = Creature()

    
    def introduce(self): 
        """
        Starting interface of the game
        """
        username = input('Enter your username:')
        print(f'{username}, OH NO YOU ARE TRAPPED! \nYou will go through a series of rooms that may give you items or have ANGRY creatures wanting you DEAD :P \nKill them all, especially the boss to escape! \nGOOD LUCK ;D')

    def game_is_over(self) -> bool:
        if self.steve.isdead(): # other conditions
            return True

    def show_status(self) -> 'str':
        print(self.steve)

    def show_options(self) -> str:
        menu = "1. Attack\n 2. Retreat"
        print(menu)

    def prompt_player(self) -> int:
        opt = None
        while not self.isvalid(opt):
            opt = input('Please choose option 1 or 2:')
        return opt

    def validate(choice) -> bool:
        if choice in ('12'):
            if len(choice) == 1:
                return True
        return False

    def do_action(self):
        print(self.items)
        total = len(self.items)
        choice = input('Please choose your weapon.')
        # requires weapon list to be in number options
        if len(choice) == 1:
            if choice in range(len(self.items)):
                self.steve._equip_armour(choice)

    def show_losescreen(self):
        print('Game Over !')
                
    def restart():
        print('Try Again?')
        print('1. Yes\n2. No')
        choice = input()

    def attack(self):
        x, y = maze.steve_pos()
        room = Room(x, y)
        while not self.steve_isdead() or self.creature.hitpoints == 0:
            pass


    
    
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
        while not self.game_is_over():
            self.show_status()
            # show status
            if self.creature_encountered():
                self.show_options()
                # show player action options
                option = self.prompt_player()
                # prompt player to take actions
                if option == 1:
                    self.attack()
                    if self.game_is_over():
                        continue
                else:
                    odds = random.randint(0, 100)
                    if odds <= 80%
                        self.maze.try_move_steve(...)
                    else:
                        print()
                        self.attack()
                        if self.game_is_over():
                            continue
                        
                self.do_action()
                self.update()
                # update
            
        self.show_losescreen()
        restart_choice = self.restart()
        if self.validate():
            
            
            


