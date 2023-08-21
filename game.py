#File containing the code for the game
from data import *
import random



class MUDGame:
    """This class encapsulates data for the main game implementation."""
    def __init__(self):
        self.gameover = False # default
        self.won = False # default
        self.maze = Labyrinth()
        self.maze.generate()
        self.steve = Steve(0)
        self.creature = Creature()
        self.steve_path = []

    
    def introduce(self): 
        """
        Starting interface of the game
        """
        username = input('Enter your username:')
        print(f'{username}, OH NO YOU ARE TRAPPED! \nYou will go through a series of rooms that may give you items or have ANGRY creatures wanting you DEAD :P \nKill them all, especially the boss to escape! \nGOOD LUCK ;D')

    def game_is_over(self) -> bool:
        if self.steve.isdead() or self.boss.isdead(): # other conditions
            return True

    def show_status(self) -> 'str':
        print(self.steve)

    def show_options(self, situation) -> str:
        sit = str(situation)
        if sit == 'creature':
            menu = "1. Attack \n2. Retreat"
        elif sit == 'item':
            menu = '1. Pick Up \n2. Do not pick up'
        elif sit == 'restart':
            menu = '1. Yes \n2. No'
        print(menu)

    def prompt_player_2opt(self) -> int:
        opt = None
        while not self.isvalid_2opt(opt):
            opt = input('Please choose option 1 or 2:')
        return opt

    def isvalid_2opt(choice) -> bool:
        if choice in ('12'):
            if len(choice) == 1:
                return True
        return False

    def isvalid_4opt(choice) -> bool:
        if choice in ('1234'):
            if len(choice) == 1:
                return True
        return False

    def attack(self):
        x, y =self.maze.steve_pos()
        room = self.maze.get_current_pos()
        creature = self.room.get_creature()
        while not self.steve_isdead() or self.creature.hitpoints <= 0:
            print(self.steve)
            print(f"{creature.info['name']} has {self.creature.get_health()} HP")
            # damage = self.steve....
            self.creature.hitpoints -= damage
            print(f'You attacked {creature.info["name"]}')
            self.steve.health -= creature.get_attack()
        pass

    def creature_encountered(self):
        if self.room.creature is None:
            return False
        return True

    def item_found(self):
        if self.room.item is None:
            return False
        return True

    def show_winscreen():
        print('Congratulations! \nYou have escaped!')

    def show_losescreen():
        print("YOU DIED...\nDo you want to try again?")

    def movesteve(self):
        current_location = self.maze.get_current_pos
        opt_dir = {'1':'North', '2':'East', '3':'South', '4':'West'}
        available_dir = []
        dir_provided = ''
        for dir in opt_dir.values:
            if self.maze.can_move_here(current_location, dir):
                available_dir.append(dir)
        for i in range(len(available_dir)):
            dir_provided = dir_provided + str(i+1) + '. ' + available_dir[i] + ' '
        validity = False
        while validity == False:
            print('Where are you going next? ' + dir_provided )
            choice = input('Next location:')
            no_of_choice = len(available_dir)
            valid_choice = ''
            for i in range(no_of_choice):
                valid_choice += str(i + 1)
            if choice in valid_choice:
                if len(choice) == 1:
                    validity = True
        self.maze.move_steve(current_location, available_dir[choice - 1])

    def moveboss(self):
        self.maze.move_boss()
        
    
    def restore_steve_hp(self):
        
    
    
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
            self.steve_path.append(self.maze.get_current_pos)
            self.show_status()
            # show status: direction, hp, lvl, inventory
            if self.creature_encountered():
                self.show_options('creature')
                # show player action options
                option = self.prompt_player_2opt()
                # prompt player to take actions
                if option == 1:
                    self.attack()
                    if self.game_is_over():
                        continue
                else:
                    odds = random.randint(0, 100)
                    if odds <= 40:
                        self.maze.try_move_steve(...)
                        continue
                    else:
                        print("Too late to escape!")
                        self.attack()
                        if self.game_is_over():
                            continue
            if self.item_found():
                item = self.room.get_item()
                self.show_options(item)
                item_choice = self.prompt_player_2opt()
                if item_choice == 1:
                    self.steve._add_item_to_inv(item)
                    
            self.restore_steve_hp()
            self.movesteve()
            self.moveboss()
                # update
        if self.steve.isdead():
            self.show_losescreen()
            self.show_options('restart')
            restart_choice = self.prompt_player_2opt()
            if restart_choice == 1:
                self.run()
            else:
                print('Hope to see you again !')
        else:
            self.show_winscreen()

            
            
            


