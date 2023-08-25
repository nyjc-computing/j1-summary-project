#File containing the code for the game
from data import *
import random

NORTH = "NORTH"
SOUTH = "SOUTH"
EAST = "EAST"
WEST = "WEST"


class MUDGame:
    """This class encapsulates data for the main game implementation."""
    def __init__(self):
        self.gameover = False # default
        self.won = False # default
        self.maze = Labyrinth()
        self.maze.generate()
        self.steve = Steve()
        self.steve_path = []
        self.boss = Boss()


    
    def introduce(self): 
        """
        Starting interface of the game
        """
        username = input('Enter your username: ')
        while username is None:
            username = input('Enter your username: ')
        print(f'{username}, OH NO YOU ARE TRAPPED! \nYou will go through a series of rooms that may give you items or have ANGRY creatures wanting you DEAD :P \nKill them all, especially the boss to escape! \nGOOD LUCK ;D')

    def game_is_over(self) -> bool:
        if self.steve.isdead() or self.boss.isdead(): # other conditions
            return True

    def show_status(self) -> None:
        print(self.steve)

    def show_options(self, sit: str) -> None:
        if sit == 'creature':
            menu = "1. Attack \n2. Retreat"
        elif sit == 'item':
            menu = '1. Pick Up \n2. Do not pick up'
        elif sit == 'restart':
            menu = '1. Yes \n2. No'
        elif sit == 'battle':
            menu = '1. Attack \n2. Heal'
        print(menu)

    def prompt_player_2opt(self) -> int:
        opt = input('Please choose option 1 or 2: ')
        while not self.isvalid_2opt(opt):
            print('Please a valid number(1/2).')
            opt = input('Please choose option 1 or 2: ')
        return opt


    def isvalid_2opt(self, opt) -> bool:
        if opt in '12':
            if len(opt) == 1:
                return True
        return False

    def isvalid_4opt(self, opt) -> bool:
        if opt in '1234':
            if len(opt) == 1:
                return True
        return False

    def battle(self):
        x, y = self.maze.get_current_pos()
        room = self.maze.lab[x][y]
        creature = room.get_creature()
        print(f"You have encountered the {creature.get_name()}!")
        while not self.steve.isdead() or self.creature.isdead():
            print(self.steve) # show HP
            if len(self.steve.inventory) == 0:
                print(f'You have no heal items! \nAttack the {creature.get_name()}.')
                damage = self.steve.get_attack()
                self.creature.take_damage(damage)
                print(f"{creature.get_name()} now has {self.creature.get_health()} HP")
            else:
                self.show_options('battle')
                battle_option = self.prompt_player_2opt()
                if battle_option == 1:
                    #attack
                    damage = self.steve.get_attack()
                    self.creature.take_damage(damage)
                    print(f"{creature.get_name()} now has {self.creature.get_health()} HP")
                elif battle_option == 2:
                    #heal
                    heal_option = None
                    while not self.isvalid_heal(heal_option): 
                        self.steve.display_inventory()
                        heal_option = input('Please choose a food item: ')
                        self.isvalid_heal(heal_option)
                    heal_option = int(heal_option) - 1
                    self.steve.eat(heal_option)
                    print('Healed!')
            #Steve endturn 
            damage = creature.random_move()
            self.steve.take_damage(damage)
            if damage == 0:
                print(f"The {creature.name} has healed itself.")
            else:
                print(f"The {creature.name} has dealt {damage} damage on you.")
        

    def isvalid_heal(self, heal_option):
        range_of_option = len(self.steve.inventory) + 1
        valid_opt = []
        for i in range(1, range_of_option):
            valid_opt.append(str(i))
        if heal_option in valid_opt:
            return True
        return False
        

    def creature_encountered(self):
        x, y = self.maze.get_current_pos()
        room = self.maze.lab[x][y]
        if room.get_creature() is None:
            return False
        return True

    def item_found(self):
        x, y = self.maze.get_current_pos()
        room = self.maze.lab[x][y]
        if room.get_item() is None:
            return False
        return True

    def show_winscreen(self):
        print('Congratulations! \nYou have won!')

    def show_losescreen(self):
        print("YOU DIED!")
        print(f"Score: {random.randint(0, 100000)}")

    def movesteve(self):
        current_location = self.maze.get_current_pos()
        opt_dir = {'1':NORTH, '2':SOUTH, '3':EAST, '4':WEST}
        available_dir = []
        dir_provided = ''
        for dir in opt_dir.values():
            if self.maze.can_move_here(current_location, dir):
                available_dir.append(dir)
        for i in range(len(available_dir)):
            dir_provided = dir_provided + str(i+1) + '. ' + available_dir[i] + ' '
        validity = False
        while validity == False:
            print('Where are you going next? ' + dir_provided )
            choice = input('Next location: ')
            no_of_choice = len(available_dir)
            valid_choice = ''
            for i in range(no_of_choice):
                valid_choice += str(i + 1)
            if choice in valid_choice:
                if len(choice) == 1:
                    validity = True
        choice = int(choice)
        self.maze.move_steve(available_dir[choice - 1])

    def moveboss(self):
        self.maze.move_boss()
        
    
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
                if option == '1':
                    self.battle()
                    if self.game_is_over():
                        continue
                else:
                    odds = random.randint(1, 100)
                    if odds <= 40:
                        self.maze.try_move_steve(self.steve_path[-2])
                        continue
                    else:
                        print("Too late to escape!")
                        self.battle()
                        if self.game_is_over():
                            continue
            if self.item_found():
                x, y = self.maze.get_current_pos()
                room = self.maze.lab[x][y]
                item = room.get_item()
                self.show_options('item')
                item_choice = self.prompt_player_2opt()
                if item_choice == 1:
                    self.steve._add_item_to_inv(item)
            self.movesteve()
            if random.randint(1, 100) <= 30:
                self.moveboss() 
                # update
        if self.steve.isdead():
            self.show_losescreen()
        else:
            self.show_winscreen()

            
            