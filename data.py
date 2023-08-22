import random
import time

#Rooms
total_rooms = 0
def increment_total_rooms():
    global total_rooms
    return total_rooms + 1
    
class Room:
    def __init__(self, boss = None, type = 'normal', x = 2, y = 2, up = None, down = None, left = None, right = None, layer = 1, number = 0):
        #next rooms
        self.boss = boss
        self.type = type
        self.up = up
        self.down = down 
        self.right = right
        self.left = left
        self.layer = layer
        self.number = number
        connections = random.randint(2, 3)
        next_rooms = [self.up, self.down, self.left, self.right]
        ref_next_rooms = ['self.up', 'self.down', 'self.left', 'self.right']
        for i in range(len(next_rooms)):
            if next_rooms[i] != None:
                next_rooms.pop(i)
                ref_next_rooms.pop(i)
        if self.type == 'start':
            #Start Room
            self.up = Room(down = self)
        elif total_rooms < 10 and self.layer < 3:
            #Normal Room
            while connections != 0:
                next_room = random.randint(0, len(next_rooms) - 1)
                if ref_next_rooms[next_room] == 'self.up':
                    self.up = Room(down = self, layer=self.count_layer(), number = self.count_room())
                    increment_total_rooms()
                    next_rooms.pop(next_room)
                    ref_next_rooms.pop(next_room)
                elif ref_next_rooms[next_room] == 'self.down':
                    self.down = Room(up = self, layer=self.count_layer())
                    increment_total_rooms()
                    next_rooms.pop(next_room)
                    ref_next_rooms.pop(next_room)
                elif ref_next_rooms[next_room] == 'self.left':
                    self.left = Room(right = self, layer=self.count_layer())
                    increment_total_rooms()
                    next_rooms.pop(next_room)
                    ref_next_rooms.pop(next_room)
                elif ref_next_rooms[next_room] == 'self.right':
                    self.right = Room(left = self, layer=self.count_layer())
                    increment_total_rooms()
                    next_rooms.pop(next_room)
                    ref_next_rooms.pop(next_room)
                self.layer = self.countRoom()
        #Boss Room
        if self.number == 7:
            next_room = random.randint(0, len(next_rooms) - 1)
            if ref_next_rooms[next_room] == 'self.up':
                self.up = Room(down = self, type = 'boss', boss = Springtrap(), layer=self.count_layer())
                next_rooms.pop(next_room)
                ref_next_rooms.pop(next_room)
            elif ref_next_rooms[next_room] == 'self.down':
                self.down = Room(up = self, type = 'boss', boss = Springtrap(), layer=self.count_layer())
                next_rooms.pop(next_room)
                ref_next_rooms.pop(next_room)
            elif ref_next_rooms[next_room] == 'self.left':
                self.left = Room(right = self, type = 'boss', boss = Springtrap(), layer=self.count_layer())
                next_rooms.pop(next_room)
                ref_next_rooms.pop(next_room)
            elif ref_next_rooms[next_room] == 'self.right':
                self.right = Room(left = self, type = 'boss', boss = Springtrap(), layer=self.count_layer())
                next_rooms.pop(next_room)
                ref_next_rooms.pop(next_room)
                
        self.grid = Grid(type = type, x = x, y = y)
        
    def display_room(self):
        pass

    def is_next_room(self, next : str) -> bool:
        if next == 'w':
            return self.up is not None
        elif next == 'a':
            return self.left is not None
        elif next == 's':
            return self.down is not None
        elif next == 'd':
            return self.right is not None
        else:
            print('It seems that this door is locked.')

    def next_room(self, next : str) -> 'Room':
        '''
        User moves to next room. Depending on the input, move to room above, below, left or right. Also, check if next room for given input exists.
        '''
        next = next.lower()
        if next == 'w':
            return self.up
        elif next == 's':
            return self.down
        elif next == 'a':
            return self.left
        elif next == 'd':
            return self.right
    def current_room(self) -> 'Room':
        '''
        Returns the current room
        '''
        return self

    def count_layer(self):
       return self.layer + 1

    def count_room(self):
        return self.number + 1
        
    def is_boss(self):
        if self.type == 'boss':
            return True
        return False

    def get_boss(self):
        '''
        Return the boss.
        '''
        return self.boss
        
def start_room():
    """Instantiates a spawn room"""
    current_room = Room(type = 'start')
    return current_room

class Grid:
    def __init__(self, type, x, y):
        self.type = type
        self.grid = [{0 : None, 1 : None, 2 : None, 3 : None, 4 : None},
                    {0 : None, 1 : None, 2 : None, 3 : None, 4 : None},
                    {0 : None, 1 : None, 2 : None, 3 : None, 4 : None},
                    {0 : None, 1 : None, 2 : None, 3 : None, 4 : None},
                    {0 : None, 1 : None, 2 : None, 3 : None, 4 : None}]
        i = 0
        if type == 'normal':
        #Spawning creatures
            while i < 5:
                if self.grid[random.randint(0, 4)][random.randint(0, 4)] == None:                    
                    self.grid[random.randint(0, 4)][random.randint(0, 4)] = {'type' : 'creature', 'creatures':[GB(), GB()]}
                i = i + 1
            k = 0
        #Spawning items
            while k < 5:
                if self.grid[random.randint(0, 4)][random.randint(0, 4)] == None:
                    random_item = random.choice(all_items)
                    self.grid[random.randint(0, 4)][random.randint(0, 4)] = {'type' : 'item', 'item' : random_item}
                    
                    
                k = k + 1
        self.coordinates = [x, y]

        
    def get_position(self) -> list:
        '''
        Return user position
        '''
        return self.coordinates
    def prompt_movement(self) -> str:
        '''
        Prompt the user for a movement and return the direction to move. Also, to view inventory, user types open inventory
        '''
        print("Type 'wasd' to move, open the inventory by typing 'inventory'")
        action = input('Type an action:')
        return action.lower()
        
    def move(self, position : list):
        '''
        Update user position and coordinates in the room
        '''
        self.coordinates = position
    
    def is_encounter(self):
        '''
        Return true if user coordinates are currently on a creature tile.
        '''
        if self.grid[self.get_position()[0]][self.get_position()[1]] == None:
            return False
        elif self.grid[self.get_position()[0]][self.get_position()[1]]['type'] == 'creature':
            return True
        return False

    def get_enemies(self):
        '''
        Return the enemies on that tile
        '''
        return self.grid[self.get_position()[0]][self.get_position()[1]]['creatures']
    def is_item(self):
        '''
        Return true if user coordinates are currently on a item tile.
        '''
        if self.grid[self.get_position()[0]][self.get_position()[1]]['type'] == 'item':
            return True
        else:
            return False
            
    def get_item(self) -> str:
        '''
        If user is on an item tile, return the item on that tile
        '''
        return self.grid[self.get_position()[0]][self.get_position()[1]]['item']['name']
        
    def remove_item(self):
        '''
        After a defeating a creature or picking up an item, remove it from the grid
        '''
        self.grid[self.get_position()[0]][self.get_position()[1]] = None



#Start
def start_menu():
    print('Welcome to FNAF:Reckoning!')
    choice = input("Type 'Start' to begin or 'Info' for more information: ")
    if choice.lower() == 'start':
        choose_character()
    elif choice.lower() == 'info':
        info()
    else:
        print("Please type either Start or Info." )
        start_menu()

def info():
    print('1. Freddy Fazbear')
    print('2. Bonnie')
    print('3. Chica')
    print('4. Foxy')
    cr = input('Please select a character to read their description or Back to return to start menu: ')
    if cr.lower() == 'freddy':
        print('HP: 100')
        print('Description: The lovable brown bear enters the dungeon, ready to face any and all challenges in his way. With his trusty microphone, Freddy faces fear head on as he ventures deeper into the spiraling depths of the abyss.')
        print('Ability: Lullaby - Freddy sings a lullaby, causing all nearby monsters (except the boss) to fall asleep (for 3 turns) , allowing Freddy to walk past them without alerting them.')
        print('Passive: Freddy does increased damage against enemies that are asleep.')
        print('Attacks:')
        print('1. Mic Toss')
        print('2. Sing')
        print('3. The Bite')
        print('--------------------------------------------------------')
        info()
        
    elif 'bonnie' in cr.lower():
        print('HP: 100')
        print('Description: Bonnie the bunny is here and he is ready to stir up a storm. He treads through the treacherous dungeon as he sends rumbles through each room, pathing a way for him to dive deeper into the dungeons.')
        print('Ability: Reverb - Bonnie strums his guitar, sending shockwaves in a specific direction towards enemies, hitting each of them for 10 damage each and immediately enters combat with them. This ability stacks up to 2 times.')
        print('Passive: If there are more enemies than Bonnie in the room, Bonnie increases his attacks by 5 damage.')
        print('Attacks:')
        print('1. Rift')
        print('2. Gatecrash')
        print("3. Rock 'n' Roll")
        print('--------------------------------------------------------')
        info()
        
    elif 'chica' in cr.lower():
        print('HP: 100')
        print('Description: Chica is afraid of the darkness, hence she brought her best friend along with her - cupcake. Cupcake reassures her constantly that everything will be fine and helps her get through the dungeons, yet honestly she just wants to go back to the pizzeria and feast on pizza. ')
        print("Ability: Cupcake - Chica throws her cupcake, causing it to explode in a 3x3 area once the cupcake comes into contact with a solid object, dealing 30 damage to enemies within its area.")
        print('Passive: Chica’s cupcake acts as a light source, however her fear gauge increases quicker when she is in the dark.')
        print('Attacks:')
        print('1. Pizza Slice')
        print('2. Decoy')
        print("3. Devour")
        print('--------------------------------------------------------')
        info()
        
    elif 'foxy' in cr.lower():
        print('HP: 85')
        print('Description: Foxy brandishes his hook, waiting for his next unsuspecting prey to walk past him as he lurks in the shadows. His unique eyes allow him to adapt to the darkness, but is also the reason why he is largely deterred from light sources. Though Foxy may be seen as arrogant and boastful by others, his band members know that he just wants to be able to be someone to somebody, in this case a better teammate for his friends.')
        print('Ability: Scamper - Foxy dashes in a targeted direction, dealing 50 damage to any enemies in his way and takes 5 damage for each solid object hit.')
        print('Passive:')
        print('Foxy regenerates 5 hp each time he defeats an enemy.')
        print('Foxy does not have a fear bar but light causes him to take 5 damage when he comes into contact with it.')
        print('When Foxy’s health falls below 50%, the damage of his skills increases by 30%.')
        print('Attacks:')
        print('1. Yar-Har')
        print('2. Harvest Moon')
        print("3. Death Grip")
        print('--------------------------------------------------------')
        info()
        
    elif 'back' in cr.lower():
        start_menu()
    else:
        print('Please enter a valid animatronic.')
        info()
    
def choose_character():
    print('Characters:')
    print('1. Freddy Fazbear')
    print('2. Bonnie')
    print('3. Chica')
    print('4. Foxy')
    cr = input('Please select your character or skip if you are ready to start the game: ')
    if cr.lower() == 'freddy':
        print('You have selected Freddy Fazbear.')
        return 'freddy'
    elif 'bonnie' in cr.lower():
        print('You have selected Bonnie.')
        return 'bonnie'
    elif 'chica' in cr:
        print('You have selected Chica.')
        return 'chica'
    elif 'foxy' in cr:
        print('You have selected Foxy.')
        return 'foxy'
    elif 'skip' in cr.lower():
        print('The game will begin.')
        return 'skip'
    else:
        print('Please enter a valid animatronic.')
        return None



#accuracy
def accuracy(target, accuracy):
    if target.has_status('phantom'):
        accuracy -= 10
    hit = [True] * accuracy + [False] * (100 - accuracy)
    if hit:
        return True
    else:
        return False
#Status
statuses = [{'name' : 'Sleeping', 'description' : 'Target cannot take action based on the count. At the end of the target\'s turn, reduce the count by 1.', 'count' : None}, 
            {'name' : 'Corrupted', 'description' : 'Target attacks indiscriminately, At the end of the turn, reduce the count by 1.', 'count' : None},
            {'name' : 'Infiltrated', 'description' : 'Target takes 10% more damage when attacked by Glitch Type enemies. At the end of the turn, reduce count by 1.', 'count' : None},
           {'name' : 'Phantom', 'description' : 'Target has an increased chance to dodge all attacks. At the end of the turn, reduce count by 1.' , 'count' : None}]

def infiltrated(damage):
    return abs(damage * 110 / 100)
    
#Characters and Enemies
class GB:
    def __init__(self, status=None, health=50):
        self.name = 'Glitch Bunny'
        self.health = health
        self.status = status if status is not None else []

    def take_damage(self, damage: int):
        self.health -= damage

    def is_defeated(self):
        if self.health <= 0:
            print(f"{self.name} has died!")
            return True
        return False
        
    def display_turn(self):
        print(f"It is {self.name}'s turn.")
        
    def add_status(self, status, turns):
        for st in statuses:
            if st['name'] == status:
                temp = st.copy()
                temp['count'] = turns
                self.status.append(temp)
                
    def remove_status(self):
        for st in self.status:
            st['counter'] -= 1
            if st['counter'] == 0:
                name = st['name']
                print(f'{self.name} is no longer {name}!')
                self.status.remove(st)

    def has_status(self, status):
        for st in self.status:
            if st['name'] == status:
                return True
        return False

    def get_stats(self):
        print(f"{self.name}'s stats")
        print(f"HP: {self.health}" / 50)
        if self.status == []:
            print('Status: No statuses.')
        else:
            for st in self.status:
                name = st['name']
                description = st['description']
                turns = st['count']
                print(f'Status : {name}  /\t Description : {description}  /\t Turns Remaining : {turns}')

    def attack(self, target):
        n = random.randint(1, 100)
        if n < 50:
            if accuracy(50, target) == True:
                print(f"{self.name} used Bash on {target.name}!")
                damage = 10
                if target.has_status('Infiltrated'):
                    damage = infiltrated(damage)
                target.take_damage(damage)
                print(f'{target.name} took {damage} damage.')
            else:
                print('The attack missed!')
        else:
            if accuracy(50, target) == True:
                print(f"{self.name} used Ram on {target.name}!")
                damage = 15
                if target.has_status('Infiltrated'):
                    damage = infiltrated(damage)
                target.take_damage(damage)
                print(f'{target.name} took {damage} damage.')
            else:
                print('The attack missed!')
        print('---------------------------------------------------------')


class Springtrap:
    def __init__(self, status=None, health=300):
        self.name = 'Springtrap'
        self.health = health
        self.status = status if status is not None else []

    def take_damage(self, damage: int):
        self.health -= damage

    def is_defeated(self):
        if self.health <= 0:
            print(f"{self.name} has died!")
            return True
        return False        

    def display_turn(self):
        print(f"It is {self.name}'s turn.")
            
    def add_status(self, status, turns):
        for st in statuses:
            if st['name'] == status:
                temp = st.copy()
                temp['count'] = turns
                self.status.append(temp)
                
    def remove_status(self):
        for st in self.status:
            st['counter'] -= 1
            if st['counter'] == 0:
                name = st['name']
                print(f'{self.name} is no longer {name}!')
                self.status.remove(st)

    def has_status(self, status):
        for st in self.status:
            if st['name'] == status:
                return True
        return False

    def get_stats(self):
        print(f"{self.name}'s stats")
        print(f"HP: {self.health} / 300")
        if self.status == []:
            print('Status: No statuses.')
        else:
            for st in self.status:
                name = st['name']
                description = st['description']
                turns = st['count']
                print(f'Status : {name}  /\t Description : {description}  /\t Turns Remaining : {turns}')

    def encounter(self):
        print('You notice the pungent smell of decaying matter.')
        time.sleep(2)
        print('Then, you hear the clanking of metal wires and robotic movement.')
        time.sleep(2)
        print('Finally, you see him.')
        time.sleep(2)
        print('Springtrap.')
        
    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        n = random.randint(1, 3)
        if n == '1':
            print(f'{self.name} used Phantom Mirage!')
            self.add_status('Phantom', 1)
            damage = 7
            if target.has_status('Infiltrated'):
                damage = infiltrated(damage)            
            target.take_damage(damage)
            print(f'{target.name} took {damage} damage.')
        if n == '2':
            if accuracy(40, target) == True:
                print(f'{self.name} used Decaying Grasp on {target.name}!')
                damage = 30
                if target.has_status('Infiltrated'):
                    damage = infiltrated(damage)
                target.take_damage(damage)
                print(f'{target.name} took {damage} damage.')
            else:
                print('The attack missed!')
        if n == '3':
            if accuracy(15, target) == True:
                print(f'{self.name} used Eternal Torment on {target.name}!')
                damage = 60
                if target.has_status('Infiltrated'):
                    damage = infiltrated(damage)
                target.take_damage(damage)
                print(f'{target.name} took {damage} damage.')
            else:
                print('The attack missed!')
        print('---------------------------------------------------------')



class Glitchtrap:
    def __init__(self, status=None, health=250):
            self.name = 'Glitchtrap'
            self.health = health
            self.status = status if status is not None else []
    
    def take_damage(self, damage: int):
        self.health -= damage

    def is_defeated(self):
        if self.health <= 0:
            print(f"{self.name} has died!")

    def display_turn(self):
        print(f"It is {self.name}'s turn.")
        
    def add_status(self, status, turns):
        for st in statuses:
            if st['name'] == status:
                temp = st.copy()
                temp['count'] = turns
                self.status.append(temp)
                
    def remove_status(self):
        for st in self.status:
            st['counter'] -= 1
            if st['counter'] == 0:
                name = st['name']
                print(f'{self.name} is no longer {name}!')
                self.status.remove(st)

    def has_status(self, status):
        for st in self.status:
            if st['name'] == status:
                return True
        return False

    def get_stats(self):
        print(f"{self.name}'s stats")
        print(f"HP: {self.health} / 250")
        if self.status == []:
            print('Status: No statuses.')
        else:
            for st in self.status:
                name = st['name']
                description = st['description']
                turns = st['count']
                print(f'Status : {name}  /\t Description : {description}  /\t Turns Remaining : {turns}')

    def spawn():
        if Springtrap.health <= 0:
            print("Springtrap has died!")
            time.sleep(2)
            print('Or has he?')
            time.sleep(2)
            print('Springtrap: Did you really think this would be enough to finish me?')
            time.sleep(2)
            print('Springtrap: Death has never been my concern.')
            time.sleep(3)
            print('Springtrap: You forget,')
            time.sleep(3)
            print('Springtrap: I always come back.')
            time.sleep(4)
            print('You watch as the decaying bunny is encapsulated in digital code, turning him into another bunny with stitches running down his sides as he chuckles.')
            time.sleep(5)
            print('Glitchtrap: This is only the beginning.')
    
    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        n = random.randint(1, 100)
        if n > 30 and n < 60: #28% chance to use this attack
            print(f'{self.name} used Corrupt on {target.name}!')
            if accuracy(50, target) == True:   
                damage = 20
                if target.has_status('Infiltrated'):
                    damage = infiltrated(damage)
                target.take_damage(damage)
                print(f"{target.name} took {damage} damage!")
                target.add_status('Corrupted', 1)
                print(f"{target.name} is corrupted!")
            else:
                print('The attack missed!')
        if n > 15 and n < 31: #17% chance to use this attack
            print(f'{self.name} used Digital Infiltration on {target.name}!')
            if accuracy(30, target) == True:
                target.add_status('infiltrated', 1)
                print(f"{self.name} infiltrated {target.name}'s system!")
            else:
                print('The attack missed!')
        if n >= 2 and n < 16: #14% chance to use this attack
            print(f'{self.name} used System Overload on {target.name}!')
            if accuracy(40, target) == True:
                damage = 40
                if target.has_status('Infiltrated'):
                    damage = infiltrated(damage)
                target.take_damage(self.damage) 
                print(f"{target.name} took {damage} damage!")
            else:
                print('The attack missed!')
        if n >= 60: #40% chance to use this attack
            print(f'{self.name} used Pixel Blast on {target.name}!')
            if accuracy(70, target) == True:
                damage = 15
                if target.has_status('Infiltrated'):
                    damage = infiltrated(damage)
                target.take_damage(self.damage)
                print(f"{target.name} took {damage} damage!")
            else:
                print('The attack missed!')
        if n == 1:  #1% chance to use this attack
            print(f'{self.name} hit the Griddy!') 
            print('You were fascinated and stared in awe.')
#Inventory
all_items = []
player_inventory = []
def get_inventory():
    return player_inventory
    
#Playable Characters
class Freddy:
    def __init__(self, status=None, health=100, inventory=None):
        self.name = 'Freddy Fazbear'
        self.health = health
        self.status = status if status is not None else []
        self.item_equipped = None

    def display_inventory(self):
        print("Inventory:")
        if len(player_inventory) == 0:
            print("You don't have any items currently.")
        else:
            for item in player_inventory:
                name = item['name']
                description = item['description']
                effect = item['effect']
                consumable = item['consumable']
                print(f'Item : {name}  /\t Description : {description}  /\t Effect : {effect}  /\t Consumable : {consumable}')

    def add_item(self, item):
        global player_inventory
        global all_items
        for it in all_items:
            if it['name'] == item:
                player_inventory.append(it)

    def is_use_item(self):
        is_use = input("Use an item? Y/N :")
        is_use = is_use.lower()
        while is_use != 'y' and is_use != 'n':
            print("Type 'Y' or 'N'.")
            is_use = input("Use an item? Y/N :")
        if is_use == 'n':
            return False
        elif is_use == 'y':
            return True
                    
    def use_item(self):
        global player_inventory
        item = input('Choose an item to use: ')
        for it in player_inventory:
            if it['name'] == item:
                if not it['consumable']: #If item can't be consumed
                    print("You can't consume this item.")
                    return
                is_use = input("Use this item? Y/N :")
                is_use = is_use.lower()
                while is_use != 'y' and is_use != 'n':
                    print("Type 'Y' or 'N'.")
                    is_use = input("Use this item? Y/N :")
                if is_use == 'n':
                    return 
                if it['type'] == 'healing': #If item is healing
                    self.heal(it['heal'])
                    player_inventory.remove(it)
                    return
                elif it['type'] == 'weapon': #If item is weapon
                    if self.items_equipped != None:
                        print('You already have a weapon equipped.')
                    else:
                        self.items_equipped.append(it)
                        name = it['name']
                        print(f'{self.name} has equipped {name}')
                        player_inventory.remove(it)
                        return
        print("You don't have this item.")

    def heal(self, amnt):
        self.health += amnt
        print(f"{self.name} healed {amnt} hp!")

    def take_damage(self, damage_taken):
        self.health -= damage_taken

    def is_defeated(self):
        if self.health <= 0:
            print('You died!')
            
    def display_turn(self):
        print(f"It is {self.name}'s turn.")

    def prompt_action(self, target):
        print('Select one of the following actions:')
        print('1. Attack')
        print('2. Target')
        print('3. Stats')
        print('4. Item')
        dec = input('Please choose an action: ')
        dec = dec.lower()
        if dec in ['attack', 'target', 'stats', 'item']:
            return dec
        else:
            return None
    
    def target(self):
        print('To target enemies, input a number, with the leftmost enemy being 1.')
        target = input('Choose an enemy to target: ')
        return target
        
    def prompt_check(self):
        print("Type 'enemy' to see enemy stats, 'party' to see party stats, 'back' to cancel this action.")
        check = input("Choose to check enemy or party stats: ")
        return check.lower()
        
    def prompt_attack(self):
        print(f"{self.name}'s Attacks:'")
        print('1. Mic Toss  90 acc  15 dmg')
        print('2. Sing  40 acc - dmg')
        print('3. The Bite  19 acc 87 dmg')
        print("Type 'back' to return cancel the attack. Use the numbers corresponding to each ability to attack.")
        atk = input("Select an ability to use: ")
        return atk.lower()

    def attack(self, target, atk):
        damage = 0
        damage += self.passive(damage, target)
        damage += self.item_equipped['damage']
        if atk == '1':
            print(f'Freddy used Mic Toss on {target.name}!')
            if accuracy(90, target) == True:
                damage += 15
                print(f"{target.name} took {damage} damage!")
                target.take_damage(damage)
            else:
                print('The attack missed!')
        if atk == '2':
            print(f'Freddy used Sing on {target.name}!')
            if accuracy(40, target) == True:
                target.add_status('Sleeping')
            else:
                print('The attack missed!')
        if atk == '3':
            print(f'Freddy used The Bite on {target.name}!')
            if accuracy(19, target) == True:
                damage += 87
                print(f"{target.name} took {damage} damage!")
                target.take_damage(damage)
            else:
                print('The attack missed!')

            
    def passive(self, damage, target):
        if target.has_status(damage):
            return damage + 5
            
    def add_status(self, status, turns):
        for st in statuses:
            if st['name'] == status:
                temp = st.copy()
                temp['count'] = turns
                self.status.append(temp)
                
    def remove_status(self):
        for st in self.status:
            st['counter'] -= 1
            if st['counter'] == 0:
                name = st['name']
                print(f'{self.name} is no longer {name}!')
                self.status.remove(st)

    def has_status(self, status):
        for st in self.status:
            if st['name'] == status:
                return True
        return False

    def get_stats(self):
        print(f"{self.name}'s stats")
        print(f"HP: {self.health}")
        if self.status == []:
            print('Status: No statuses.')
        else:
            for st in self.status:
                name = st['name']
                description = st['description']
                turns = st['count']
                print(f'Status : {name} , Description : {description} , Turns Remaining : {turns}')






class Bonnie:
    def __init__(self, name, status=None, counter=0, attacking=0, health=100, inventory=None):
        self.name = name
        self.health = health
        self.counter = counter
        self.status = status if status is not None else []
        self.attacking = attacking
        self.inventory = inventory if inventory is not None else []

    def heal(self, amnt):
        self.health += amnt
        print(f"{self.name} healed {amnt} hp!")

    def take_damage(self, damage_taken):
        self.health -= damage_taken
        print(f"{self.name} took {damage_taken} damage!")
        print(f'HP left:{self.health}')
        if self.health <= 0:
            print('You died!')

    def inventory(self, item):
        print(f"{self.name}'s Inventory:")
        for item in self.inventory:
            print(item)

    def add_status(self, status):
        self.status.append(status)
        
    def add_items(self, item):
        self.inventory.append(item)

    def prompt_attack(self):
        print(f"{self.name} is about to attack!")
        print('1. Rift  90 acc  15 dmg')
        print('2. Gatecrash  40 acc 5 dmg')
        print("3. Rock 'n' Roll  50 acc 25 dmg")
        atk = input("Please select an ability to use: ")
        return atk

    def attack(self, target, atk):
        if 'sleep' in self.status:
            print(f'{self.name} is asleep!')
            self.turn_end()
        elif 'corrupt' in self.status:
            print(f'{self.name} is corrupted and cannot move!')
            self.turn_end()
        elif 'infiltrated' in self.status:
            infiltrated(self)
        else:
            if atk == '1':
                print(f'{self.name} used Rift!')
                if accuracy(90) == True:
                    self.attacking += 15
                    print(f"{target.name} took {self.attacking} damage!")
                    target.take_damage(self.attacking)
                    self.attacking -= 15
                else:
                    print('The attack missed!')
            if atk == '2':
                print(f'{self.name} used Gatecrash!')
                if accuracy(40) == True:
                    self.attacking += 5
                    print(f"{target.name} took {self.attacking} damage!")
                    target.take_damage(self.attacking)
                    self.attacking -= 5
                    #stuns the opponent or can change 
                else:
                    print('The attack missed!')
            if atk == '3':
                print(f"{self.name} used Rock 'n' Roll!")
                if accuracy(50) == True:
                    self.attacking += 25
                    print(f"{target.name} took {self.attacking} damage!")
                    target.take_damage(self.attacking)
                    self.attacking -= 25
                    #implement chance indicator on number of times the attack hits
                    #max: 5 hits
                else:
                    print('The attack missed!')
            if atk < '1' or atk > '3':
                print('Please select a valid ability.')
            
    def passive(self, target):
        pass

    def depassive(self, target):
        pass

    def remove_status(self, status):
        if status in self.status:
            self.status.remove(status)

    def has_status(self, status):
        return status in self.status

    def display_turn(self):
        print(f"It is {self.name}'s turn.")

    def get_stats(self):
        print(f"{self.name}'s stats")
        print(f"HP: {self.health}")
        #print(f"Light level: {self.light}")
        if self.status == []:
            print('Status: No statuses.')
        else:
            for status in self.status:
                print(f'Status: {status}')
            
    def prompt_action(self, target):
        print('1. Attack')
        print('2. Stats')
        print('3. Light Level')
        print('4. Item')
        dec = input('Please choose an action: ')
        if dec in ['attack', 'stats', 'light', 'item']:
            return dec
        else:
            return None

    def prompt_light():
        L = input('Do you want to increase or decrease your light level: ')
        if 'increase' in L.lower():
            return L
        elif 'decrease' in L.lower():
            return L
        elif 'back' in L.lower():
            return L
        else:
            print('Please choose either increase, decrease or back.')


class Chica:
    def __init__(self, name, status=None, counter=0, attacking=0, health=100, inventory=None):
        self.name = name
        self.health = health
        self.counter = counter
        self.status = status if status is not None else []
        self.attacking = attacking
        self.inventory = inventory if inventory is not None else []

    def heal(self, amnt):
        self.health += amnt
        print(f"{self.name} healed {amnt} hp!")

    def take_damage(self, damage_taken):
        self.health -= damage_taken
        print(f"{self.name} took {damage_taken} damage!")
        print(f'HP left:{self.health}')
        if self.health <= 0:
            print('You died!')

    def inventory(self, item):
        print(f"{self.name}'s Inventory:")
        for item in self.inventory:
            print(item)

    def add_status(self, status):
        self.status.append(status)
        
    def add_items(self, item):
        self.inventory.append(item)

    def prompt_attack(self):
        print(f"{self.name} is about to attack!")
        print('1. Pizza slice  90 acc  15 dmg')
        print('2. Cupcake Decoy  - acc - dmg')
        print('3. Devour  19 acc 87 dmg')
        atk = input("Please select an ability to use: ")
        return atk

    def attack(self, target, atk):
        if 'sleep' in self.status:
            print(f'{self.name} is asleep!')
            self.turn_end()
        elif 'corrupt' in self.status:
            print(f'{self.name} is corrupted and cannot move!')
            self.turn_end()
        elif 'infiltrated' in self.status:
            infiltrated(self)
        else:
            if atk == '1':
                print(f'{self.name} used Pizza slice!')
                if accuracy(90) == True:
                    self.attacking += 15
                    print(f"{target.name} took {self.attacking} damage!")
                    target.take_damage(self.attacking)
                    self.attacking -= 15
                else:
                    print('The attack missed!')
            if atk == '2':
                print(f'{self.name} used Cupcake Decoy!')
                #deploys a clone to take damage instead of Chica
                #fails if cupcake already in play
                #cupcake's hp?
            if atk == '3':
                print(f"{self.name} used Devour!")
                if accuracy(69) == True:
                    self.attacking += 20
                    #if item has been used, increase dmg to 125
                    print(f"{target.name} took {self.attacking} damage!")
                    target.take_damage(self.attacking)
                    self.attacking -= 20
                else:
                    print('The attack missed!')
            if atk < '1' or atk > '3':
                print('Please select a valid ability.')
            
    def passive(self, target):
        pass

    def depassive(self, target):
        pass

    def remove_status(self, status):
        if status in self.status:
            self.status.remove(status)

    def has_status(self, status):
        return status in self.status

    def display_turn(self):
        print(f"It is {self.name}'s turn.")

    def get_stats(self):
        print(f"{self.name}'s stats")
        print(f"HP: {self.health}")
        #print(f"Light level: {self.light}")
        if self.status == []:
            print('Status: No statuses.')
        else:
            for status in self.status:
                print(f'Status: {status}')
            
    def prompt_action(self, target):
        print('1. Attack')
        print('2. Stats')
        print('3. Light Level')
        print('4. Item')
        dec = input('Please choose an action: ')
        if dec in ['attack', 'stats', 'light', 'item']:
            return dec
        else:
            return None

    def prompt_light():
        L = input('Do you want to increase or decrease your light level: ')
        if 'increase' in L.lower():
            return L
        elif 'decrease' in L.lower():
            return L
        elif 'back' in L.lower():
            return L
        else:
            print('Please choose either increase, decrease or back.')



class Foxy:
    def __init__(self, name, status=None, counter=0, attacking=0, health=100, inventory=None):
        self.name = name
        self.health = health
        self.counter = counter
        self.status = status if status is not None else []
        self.attacking = attacking
        self.inventory = inventory if inventory is not None else []

    def heal(self, amnt):
        self.health += amnt
        print(f"{self.name} healed {amnt} hp!")

    def take_damage(self, damage_taken):
        self.health -= damage_taken
        print(f"{self.name} took {damage_taken} damage!")
        print(f'HP left:{self.health}')
        if self.health <= 0:
            print('You died!')

    def inventory(self, item):
        print(f"{self.name}'s Inventory:")
        for item in self.inventory:
            print(item)

    def add_status(self, status):
        self.status.append(status)
        
    def add_items(self, item):
        self.inventory.append(item)

    def prompt_attack(self):
        print(f"{self.name} is about to attack!")
        print('1. Yar-Har!  90 acc  15 dmg')
        print('2. Harvest Moon  - acc - dmg')
        print('3. Death Grip  20 acc 125 dmg')
        atk = input("Please select an ability to use: ")
        return atk

    def attack(self, target, atk):
        if 'sleep' in self.status:
            print(f'{self.name} is asleep!')
            self.turn_end()
        elif 'corrupt' in self.status:
            print(f'{self.name} is corrupted and cannot move!')
            self.turn_end()
        elif 'infiltrated' in self.status:
            infiltrated(self)
        else:
            if atk == '1':
                print(f'{self.name} used Yar-Har!')
                if accuracy(90) == True:
                    self.attacking += 15
                    print(f"{target.name} took {self.attacking} damage!")
                    target.take_damage(self.attacking)
                    self.attacking -= 15
                    self.heal(5)
                else:
                    print('The attack missed!')
            if atk == '2':
                print(f'{self.name} used Harvest Moon!')
                #raise attack and accuracy
            if atk == '3':
                print(f"{self.name} used Death Grip!")
                if accuracy(30) == True:
                    self.attacking += 125
                    print(f"{target.name} took {self.attacking} damage!")
                    target.take_damage(self.attacking)
                    self.attacking -= 125
                    self.heal(5)
                else:
                    print('The attack missed!')
            if atk < '1' or atk > '3':
                print('Please select a valid ability.')
            
    def passive(self, target):
        pass

    def depassive(self, target):
        pass

    def remove_status(self, status):
        if status in self.status:
            self.status.remove(status)

    def has_status(self, status):
        return status in self.status

    def display_turn(self):
        print(f"It is {self.name}'s turn.")

    def get_stats(self):
        print(f"{self.name}'s stats")
        print(f"HP: {self.health}")
        #print(f"Light level: {self.light}")
        if self.status == []:
            print('Status: No statuses.')
        else:
            for status in self.status:
                print(f'Status: {status}')
            
    def prompt_action(self, target):
        print('1. Attack')
        print('2. Stats')
        print('3. Light Level')
        print('4. Item')
        dec = input('Please choose an action: ')
        if dec in ['attack', 'stats', 'light', 'item']:
            return dec
        else:
            return None

    def prompt_light():
        L = input('Do you want to increase or decrease your light level: ')
        if 'increase' in L.lower():
            return L
        elif 'decrease' in L.lower():
            return L
        elif 'back' in L.lower():
            return L
        else:
            print('Please choose either increase, decrease or back.')

