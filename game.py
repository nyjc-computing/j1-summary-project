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

    def prompt_player(self) -> int:
        opt = None
        while not self.isvalid(opt):
            opt = input('Please choose option 1 or 2:')
        return opt

    def isvalid(choice) -> bool:
        if choice in ('12'):
            if len(choice) == 1:
                return True
        return False

    def attack(self):
        x, y =self.maze.steve_pos()
        room = self.maze.get_current_pos()
        while not self.steve_isdead() or self.creature.hitpoints <= 0:
            print(self.steve)
            creature = self.room.get_creature()
            print(f"{creature.info['name']} has {self.creature.get_health()} HP")
            damage = self.steve....
            self.creature.hitpoints -= damage
            print(f'You attacked {creature.info['name']}')
            self.steve.health -= creature.get_attack()

    def creature_encountered():
        if self.room.creature is None:
            return False
        return True

    def item_found():
        if self.room.item is None:
            return False
        return True

    def show_winscreen():
        print('Congratulations! \nYou have escaped!')

    def show_losescreen():
        print("YOU DIED...\nDo you want to try again?")

    def movesteve():
        dir = input('Where are you going next? \n1. North \n2. East \n3.South \n4.West')
        if try_move_steve(..., dir):
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
            # show status: direction, hp, lvl, inventory
            if self.creature_encountered():
                self.show_options(creature)
                # show player action options
                option = self.prompt_player()
                # prompt player to take actions
                if option == 1:
                    self.attack()
                    if self.game_is_over():
                        continue
                else:
                    odds = random.randint(0, 100)
                    if odds <= 80:
                        self.maze.try_move_steve(...)
                    else:
                        print()
                        self.attack()
                        if self.game_is_over():
                            continue
            if self.item_found():
                item = ...
                self.show_options(item)
                item_choice = self.prompt_player()
                self.isvalid(item_choice)
                if item_choice == 1:
                    self.steve._add_item_to_inv(item)
                self.movesteve()
                # update
        if self.steve.isdead():
            self.show_losescreen()
            self.show_options('restart')
            restart_choice = self.prompt_player()
            self.isvalid(restart_choice)
            if restart_choice == 1:
                self.run()
            else:
                print('Hope to see you again !')
        else:
            self.show_winscreen()

            
            
            


