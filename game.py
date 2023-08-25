# Import statements
import data
# import os


"""call every method here """

class MUDGame:
    def __init__(self):
        """
        This class encapsulates data for MUDGame
                    
        Attributes
        -----------
        + self.end: contains the final room number
        + self.player: contains the Player class
        + self.map: contains json file with rooms and their characteristics
        + self.inventory: contins the inventory class
        + self.player_inventory: contains the player's inventory
        + self.boss: contains the Boss class
        """
        self.end = '10'
        self.player = data.Player()
        self.map = data.map
        self.inventory = data.inventory
        self.player_inventory = data.player_inventory
        self.boss = data.Boss()
        self.colour = data.Colours()

    def game_over(self) -> bool:
        """
        returns True if player's hp is less than 0
        otherwise returns False
        """
        return self.player.hp < 0

    def enemy_presence(self, enemy_list):
        """
        checks if any enemies is present in the room
        """
        return enemy_list != []

    def item_presence(self, items_list):
        """
        checks if any items are present in the room
        """
        return items_list != []

    def room_10(self):
        """
        checks if player is at room 10
        """
        return self.player.current == self.end

    def input(self, prompt: str) -> str:
        """
        strips the empty spaces and changes the input to lower case
        """
        return input(prompt).strip().lower()

    def prompt_valid_choice(self, options, question, errormsg):
        """
        Prompt the user with a question.
        If the choice is not in options, display errormsg and re-prompt the user.
        If the choice is valid, return player choice.
        """
        choice = self.input(question)
        while choice not in options:
            print(self.colour.colourised(self.colour.RED, errormsg))
            choice = self.input(self.colour.colourised(self.colour.LIGHT_WHITE, question))
        return choice

        
    def movement(self): # can change after game is working
        """
        Displays the direction that the player can travel in
        If there are more than one paths in that direction, prompts user to select a path
        Prints the name of the room
        """
    
        #change if zonemap keys of keys has been edited
        keys = ['up', 'down', 'left', 'right']
        available = []
        #extracting up, down, left, right
        
        # remove name and description from choices
        choices = list(self.map[self.player.current].values())[2:]
        
        print(self.colour.colourised(self.colour.BROWN,'\nYou can move in the following directions: \n'))
        for i, choice in enumerate(choices):
            if choice != [None]:
                print(f'- {keys[i]}')
                available.append(keys[i])
        direction_choice = self.prompt_valid_choice(
            available,
            question='\nWhich direction do you wish to go to?: ',
            errormsg='\nYou can only move in the above stated direction(s)!'
        )
        # direction_choice = self.input('Which direction do you wish to go to?: ')
        # while direction_choice not in available:
        #     print('You can only move in the above stated direction(s)!')
        #     direction_choice = self.input('Which direction do you wish to go to?: ')
        numpaths = len(choices[keys.index(direction_choice)])
        if numpaths == 1:
            path_choice = 0
        else:    
            path_choices = [str(i) for i in range(1, numpaths + 1)]
            question = f'\nYou entered a corridor, and there are {numpaths} doors...\n'
            question += '\nThe following are the paths that can be taken: '
            for i in path_choices:
                question += f'\npath {i}'
            question += '\nWhich path do you wish to take? Type the path number: '
            path_choice = self.prompt_valid_choice(path_choices, question, '\nYou can only take the above stated path(s)!')
        self.player.current = self.map[self.player.current][direction_choice][int(path_choice) - 1]
        print(self.colour.colourised(self.colour.DARK_GRAY,'\n' * 3 + 'You are now in the '+ self.map[self.player.current]["name"] + '!\n'))

    
    def intro(self):
        """
        prints the introduction to the game
        """
        with open('content/intro.txt', 'r') as f:
            for line in f:
                print(self.colour.colourised(self.colour.DARK_GRAY, line), end= '')

    def set_username(self, Player): # no colour yet
        """
        sets the player's username
        """
        self.player.set_username()

    def room_desc(self, Player):
        """
        prints the description for the room the player is in
        """
        desc = self.map[self.player.current]['description']
        print(self.colour.colourised(self.colour.GREEN, f'\n{desc}'))

    def generate_items(self):
        """
        generates a random list of items for each room
        """
        return data.generate_items()

    def generate_enemy(self):
        """
        generates a random list of enemies for each room
        """
        return data.generate_enemy()
        
    def inventory_show(self): # can seperately implement in a class
        # 62
        """
        displays the player's inventory
        """
        used = []
        print('╔═══════════════════════════════════════════════════════╗')
        print('║                   Inventory Display                   ║')
        print('╟───────────────────────────────────────────────────────╢')
        for j in self.player_inventory:
            if j.name not in used:
                used.append(j.name)
                if j.consumable == True:
                    status = 'Usable'
                else:
                    if j.status == True:
                        status = 'Equipped'
                    else:
                        status = 'carriable'
                count = self.player_inventory.count(j)
                print(f'║{j.name:<20}x{count:<4}{"["+status+"]":<15}{j.magnitude:<5}{"["+j.type+"]":<10}║')
              
        print('╚═══════════════════════════════════════════════════════╝')

    def is_equipped(self):
        """
        if player wishes to equip another weapon, 
        unquip the initial one and equip the new one 
        """
        for i in self.player_inventory:
            if i.status == True:
                i.status = False
        return 
        
 
    def inventory_consume_item(self) -> None:
        """
        Display the inventory to the player
        Prompt the player if they want to comsume any items from their inventory.
        """
        if self.player_inventory == []:
            print(self.colour.colourised(self.colour.RED, "Nothing in inventory!"))
            return
        self.inventory_show()
        consume = self.prompt_valid_choice(
            options=['y', 'n'],
            question="Would you like to consume any item?(y/n)?: ",
            errormsg='Not a valid response!'                                
        )
        
        if consume == 'n':
            return None

        else: 
            attributes = [i.name for i in self.player_inventory]
            item = self.prompt_valid_choice(
                options=attributes,
                question="Which item would you like to consume?: ",
                errormsg='Invalid item!'
            )
            
            item_index = attributes.index(item)
            used_item = self.player_inventory[item_index]
            if used_item.consumable == True:
                print(self.colour.colourised(self.colour.BLUE, (f'{used_item.name} has been consumed!')))
                if used_item.type == 'hp':
                    self.player.hp += int(used_item.magnitude)
                    print(self.colour.colourised(self.colour.BLUE, (f'{used_item.type} has been increased by {used_item.magnitude}. {used_item.type} is now {self.player.hp}')))
                elif used_item.type == 'attack':
                    self.player.attack_punch += int(used_item.magnitude)
                    print(self.colour.colourised(self.colour.BLUE, (f'punch attack has been increased by {used_item.magnitude}. punch attack is now {self.player.attack_punch}')))
                    
                self.player_inventory.pop(item_index)
                    
            else:
                print(self.colour.colourised(self.colour.BLUE, (f'{used_item.name} has been equipped!')))
                if used_item.type == 'weapon':
                    self.is_equipped()
                    prev = self.player.attack_weapon
                    self.player.attack_weapon = used_item.magnitude
                    used_item.status = True
                    print(self.colour.colourised(self.colour.BLUE, (f'weapon attack was {prev}. weapon attack is now {self.player.attack_weapon}')))
            
#     def generate_health_bar(health, max_health):
#         bar_length = 20
#         filled_blocks = int((health / max_health) * bar_length)
#         empty_blocks = bar_length - filled_blocks
    
#         health_bar = f"[{'█' * filled_blocks}{'░' * empty_blocks}] {int((health / max_health) * 100)}%"
#         return health_bar
    
# player_health = 75
# player_max_health = 100

# enemy_health = 85
# enemy_max_health = 100

# player_health_bar = generate_health_bar(player_health, player_max_health)
# enemy_health_bar = generate_health_bar(enemy_health, enemy_max_health)

# print("Player HP:", player_health_bar)
# print("Enemy HP:", enemy_health_bar)

    def fight(self, enemy_list):
        #if enemy_presence --> choose whether to consume an item --> player attack enemy first then enemy attack player --> if player hp reaches 0 before enemy, player looses --> else continue
        """
        The player and enemy take turns to attack each other until one of their hp is less than 0
        """
        for i in range(len(enemy_list)):
            while self.player.hp > 0 and enemy_list[i].hp > 0:
                print(self.colour.colourised(self.colour.PURPLE, (f'{self.player.name} hp: {self.player.hp}')))
                print(self.colour.colourised(self.colour.CYAN, (f'enemy hp: {enemy_list[i].hp}')))
                choice = self.prompt_valid_choice(
                    options=['1', '2'],
                    question='The enemy is now in front of you! You can choose to \n1. punch \n2. attack with existing weapons: ',
                    errormsg='Invalid option!'
                )
            
    
                if choice == '1':
                    self.player.attack_p(enemy_list[i])
                elif choice == '2':
                    self.player.attack_w(enemy_list[i])
                
                enemy_list[i].atk(self.player)
    
                if enemy_list[i].hp <= 0:
                    print(self.colour.colourised(self.colour.LIGHT_WHITE, ('You have defeated the enemy!')))
                    
        # if self.player.hp < 0:
        #     self.game_over = True
        
    def pick_item(self, items): # need change
        """
        Displays the item available in the room
        """
        for i in items:
            item = self.colour.colourised(self.colour.YELLOW, i.name)
        #print(self.colour...item)
            choice = self.prompt_valid_choice(
                options=['y', 'n'],
                question=f'{item}found! Collect it to help increase your chances of defeating the monsters!(y/n): ',
                errormsg='\ninvalid option!\n'
                
                
            )

            if choice.lower() == "y":
                data.player_inventory_temp.add_item(i)
                
                
    
    def final_room(self):
        """
        Display the story text for the final room.
        Prompt the player if they would like to consume any items.
        Make the player fight the enemy
        """
        with open('content/finaldesc.txt', 'r') as f:
            for line in f:
                print(self.colour.colourised(self.colour.LIGHT_GREEN, (line.strip())))

    def final_boss_fight(self):
        """
        player and final boss take turns to attack each other
        """ 
        print(self.colour.colourised(self.colour.PURPLE, (f'{self.player.name} hp: {self.player.hp}')))           
        print(self.colour.colourised(self.colour.CYAN, (f'boss hp: {self.boss.hp}')))
        while self.player.hp > 0 and self.boss.hp > 0:
            choice = self.prompt_valid_choice(
                options=['1','2'],
                question = 'The enemy is now in front of you! You can choose to \n1. punch \n2. attack with existing weapons: ',
                errormsg='Invalid option!')
            
            if choice == '1':
                self.player.attack_p(self.boss)
            else:
                self.player.attack_w(self.boss)

            self.boss.atk(self.player)
                
            print(self.colour.colourised(self.colour.PURPLE, (f'{self.player.name} hp: {self.player.hp}')))
            print(self.colour.colourised(self.colour.CYAN, (f'boss hp: {self.boss.hp}')))

    def win(self) -> bool:
        """
        Prints winning plot when boss hp is less than 0, returns True
        Otherwise returns False
        """
        if not self.game_over():
            if self.boss.hp <= 0:
                with open('content/win_desc.txt', 'r') as f:
                    for line in f:
                        print(self.colour.colourised(self.colour.DARK_GRAY, (line.strip())))
                    return True
            else:
                return False
        return False
    
    def run(self) -> str:
        """ 
        1. method to call story intro
        2. set username
        3. movement
        4. if room has enemy then fight (method to check if enemy is inside) , if not pick item
        5. finish fighting -> pick item if any
        6. repeat 3-5 but before 4. ask if want to consume item (need method to call inventory)
        7. when reach room 10, fight the final boss. If the player is defeated before the enemy is over, prompt game over.
        """
        self.intro()
        print('\n')
        self.set_username(data.Player())
        #if os.environ.get('DEBUG'):
         #   self.player.current = "10"
        while not self.game_over()  and not self.room_10():
            self.movement()
            self.room_desc(data.Player())
            enemy_list = self.generate_enemy()
            if self.enemy_presence(enemy_list):                    
                print(self.colour.colourised(self.colour.LIGHT_GRAY, ('There is a monster in the room. Defeat them to rescue your family from the grasp of dark magic!')))
                self.inventory_consume_item()
                self.fight(enemy_list)
            else:
                print(self.colour.colourised(self.colour.LIGHT_GRAY, ("Great save! There are no enemies in this room.")))
            if not self.game_over():
                items_list = self.generate_items()
                if self.item_presence(items_list):
                    self.pick_item(items_list)
                    self.inventory_show()
                else:
                    print(self.colour.colourised(self.colour.LIGHT_GRAY, ("Aww too bad, there are no items in this room :(")))
                    
        self.final_room()
        self.inventory_consume_item()
        self.final_boss_fight()
        
                
        if not self.win():
            print(self.colour.colourised(self.colour.DARK_GRAY, ("You have been defeated >_<")))
            return
    
                    
               
        
        
                

   