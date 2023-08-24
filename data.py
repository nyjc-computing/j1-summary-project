import random
import time
import json 

#Inventory and Items
all_items = [
    {
        'name': 'Loose bolts',
        'description':
        'A pile of rusty parts found from the crushed remains of robots. Most noticeably, a pair of rusted springlocks are in the midst of the devastation.',
        'effect': 'Heals user for 10 hp.',
        'consumable': True,
        'heal': 20,
        'type': 'healing'
    },
    {
        'name': 'Functioning Limb',
        'description':
        'While the animatronic is torn beyond recognition, some part of it is still salvageable.',
        'effect': 'Heals user for 20 hp.',
        'consumable': True,
        'heal': 20,
        'type': 'healing'
    },
    {
        'name': 'Metal Pipe',
        'description': 'A ventilation pipe. It\'s stained with blood.',
        'effect': 'Increases users attack damage by 10.',
        'consumable': True,
        'damage': 10,
        'type': 'weapon'
    },
    {
        'name': 'Hatchet',
        'description': 'The hatchet brings you an unsettling feeling',
        'effect': 'Increases users attack damage by 15.',
        'consumable': True,
        'damage': 15,
        'type': 'weapon'
    },
    {
        'name': 'Battery',
        'description':
        'A battery found from a camera. It still functions with the remaining power left in it.',
        'effect': 'Heals user for 30 hp.',
        'consumable': True,
        'heal': 30,
        'type': 'healing'
    },
    {
        'name': 'Freddy Figurine',
        'description':
        'It brings you nostalgia. The microphone in the toy\'s hands is gone.',
        'effect':
        'If the selected character is Freddy, increase damage by 5. Else, it\'s a pretty cool figurine isn\'t it.',
        'consumable': False,
        'damage': 5
        
    },
    {
        'name': 'Bonnie Figurine',
        'description':
        'It brings you nostalgia. The guitar in the toy\'s hands is gone.',
        'effect':
        'If the selected character is Bonnie, increase damage by 5. Else, it\'s a pretty cool figurine isn\'t it.',
        'consumable': False,
        'damage': 5
    },
    {
        'name': 'Chica Figurine',
        'description':
        'It brings you nostalgia. You notice that the beak of the figurine is missing.',
        'effect':
        'If the selected character is Chica, increase damage by 5. Else, it\'s a pretty cool figurine isn\'t it.',
        'consumable': False,
        'damage': 5
    },
    {
        'name': 'Foxy Figurine',
        'description':
        'It brings you nostalgia. The hook in the toy\'s hands is gone.',
        'effect':
        'If the selected character is Foxy, increase damage by 5. Else, it\'s a pretty cool figurine isn\'t it.',
        'consumable': False,
        'damage': 5
    }
]

player_inventory = []

def get_inventory():
    return player_inventory

def add_item(item):
    player_inventory.append(item)
    print(f'{item} has been added to inventory!')

#Converting to json

def to_json(data):
    return json.dumps(data, indent=4)
    
#Rooms
total_rooms = 0
def increment_total_rooms():
    global total_rooms
    return total_rooms + 1

def start_room():
    """Instantiates a spawn room"""
    current_room = Room(type = 'start')
    return current_room
    
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
        x = 0
        for _ in range(len(next_rooms)):
            if next_rooms[x] != None:
                next_rooms.pop(x)
                ref_next_rooms.pop(x)
                x -= 1
            x += 1
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
                    self.down = Room(up = self, layer=self.count_layer(), number = self.count_room())
                    increment_total_rooms()
                    next_rooms.pop(next_room)
                    ref_next_rooms.pop(next_room)
                elif ref_next_rooms[next_room] == 'self.left':
                    self.left = Room(right = self, layer=self.count_layer(), number = self.count_room())
                    increment_total_rooms()
                    next_rooms.pop(next_room)
                    ref_next_rooms.pop(next_room)
                elif ref_next_rooms[next_room] == 'self.right':
                    self.right = Room(left = self, layer=self.count_layer(), number = self.count_room())
                    increment_total_rooms()
                    next_rooms.pop(next_room)
                    ref_next_rooms.pop(next_room)
                connections -= 1
        #Boss Room
        if self.number == 7:
            next_room = random.randint(0, len(next_rooms) - 1)
            if ref_next_rooms[next_room] == 'self.up':
                self.up = Room(down = self, type = 'boss', boss = Springtrap(), layer=self.count_layer())
                next_rooms.pop(next_room)
                ref_next_rooms.pop(next_room)
            elif ref_next_rooms[next_room] == 'self.down':
                self.down = Room(up = self, type = 'boss', boss = Springtrap(), layer=self.count_layer(), )
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
                    enemy_number = random.randint(1, 3)
                    enemy_list = []
                    for i in range(enemy_number):
                        enemy_list.append(random.choice(all_enemies)) 
                    self.grid[random.randint(0, 4)][random.randint(0, 4)] = {'type' : 'creature', 'creatures':enemy_list}
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
    choice = input("Type 'Start' to begin: ")
    while choice.lower() != 'start':
        print("To begin the game, enter 'start'.")
        choice = input("Type 'Start' to begin: ")

    
def info(cr):
    if cr == 'freddy':
        print('HP: 100')
        print('Description: The lovable brown bear enters the dungeon, ready to face any and all challenges in his way. With his trusty microphone, Freddy faces fear head on as he ventures deeper into the spiraling depths of the abyss.')
        print('Passive: Freddy does increased damage against enemies that are asleep.')
        print('Attacks:')
        print('1. Mic Toss')
        print('2. Sing')
        print('3. The Bite')
        print('--------------------------------------------------------')
        
    elif cr == 'bonnie':
        print('HP: 100')
        print('Description: Bonnie the bunny is here and he is ready to stir up a storm. He treads through the treacherous dungeon as he sends rumbles through each room, pathing a way for him to dive deeper into the dungeons.')
        print('Passive: Bonnie increases his attacks by a random amount if enemies are resonating with him.')
        print('Attacks:')
        print('1. Rift')
        print('2. Guitar crash')
        print("3. Rock 'n' Roll")
        print('--------------------------------------------------------')
        
    elif cr == 'chica':
        print('HP: 100')
        print('Description: Chica is afraid of the darkness, hence she brought her best friend along with her - cupcake. Cupcake reassures her constantly that everything will be fine and helps her get through the dungeons, yet honestly she just wants to go back to the pizzeria and feast on pizza. ')
        print("Passive: Chica's cupcake heals her and when destroyed, explodes and deals damage to the opponent.")
        print('Attacks:')
        print('1. Pizza slice')
        print('2. Cupcake decoy')
        print("3. Devour")
        print('--------------------------------------------------------')
        
    elif cr == 'foxy':
        print('HP: 100')
        print('Description: Foxy brandishes his hook, waiting for his next unsuspecting prey to walk past him as he lurks in the shadows. His unique eyes allow him to adapt to the darkness, but is also the reason why he is largely deterred from light sources. Though Foxy may be seen as arrogant and boastful by others, his band members know that he just wants to be able to be someone to somebody, in this case a better teammate for his friends.')
        print('Passive: When Foxy has below half of his health, his hunter instincts kick in and he increases his attack.')
        print('Attacks:')
        print('1. Yar-Har')
        print('2. Harvest Moon')
        print("3. Death Grip")
        print('--------------------------------------------------------')
    
def choose_character():
    print('Characters:')
    print('1. Freddy Fazbear')
    print('2. Bonnie')
    print('3. Chica')
    print('4. Foxy')
    cr = input("Please select your character or enter 'skip' if you are ready to start the game: ")
    cr = cr.lower()
    if cr == 'skip':
        return cr
    info(cr)
    print('')
    is_select = input('Select ', cr.capitalize(), ' as your character? Y/N: ')
    is_select = is_select.lower()
    if input == 'n':
        return choose_character()
    return cr


#accuracy
def accuracy(target, accuracy):
    if target.has_status('Phantom'):
        accuracy -= 10
    if target.has_status('Nightfall'):
        accuracy += 20
    hit = [True] * accuracy + [False] * (100 - accuracy)
    if hit:
        return True
    else:
        return False
        
#Status
statuses = [{'name' : 'Sleeping', 'description' : 'Target cannot take action based on the count. At the end of the target\'s turn, reduce the count by 1.', 'count' : None}, 
            {'name' : 'Corrupted', 'description' : 'Target attacks indiscriminately, At the end of the turn, reduce the count by 1.', 'count' : None},
            {'name' : 'Infiltrated', 'description' : 'Target takes 10% more damage when attacked by Glitch Type enemies. At the end of the turn, reduce count by 1.', 'count' : None},
            {'name' : 'Phantom', 'description' : 'Target has an increased chance to dodge all attacks. At the end of the turn, reduce count by 1.' , 'count' : None},
            {'name' : 'Resonance', 'description' : 'Target gains a random damage boost between 1 and 10 extra damage. At the end of the turn, reduce count by 1.' , 'count' : None},
            {'name' : 'Nightfall', 'description' : 'Target increases their attack and accuracy of their skills, as well as gains the ability to leech of of the opponent\'s health. At the end of the turn, reduce count by 1.' , 'count' : None}]

def infiltrated(damage):
    return abs(damage * 110 / 100)

def instinct(damage):
    return abs(damage * 130 / 100)
    
#Enemies
all_enemies = ['GB', 'BB']

class GB:
    def __init__(self, status=None, health=50):
        self.name = 'Glitch Bunny'
        self.health = health
        self.status = status if status is not None else []

    def take_damage(self, damage: int):
        self.health -= damage

    def is_defeated(self):
        if self.health <= 0:
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

class BB:
    def __init__(self, status=None, health=75):
        self.name = 'Balloon Boy'
        self.health = health
        self.status = status if status is not None else []

    def take_damage(self, damage: int):
        self.health -= damage

    def is_defeated(self):
        if self.health <= 0:
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
        print(f"HP: {self.health}" / 75)
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
                print(f"{self.name} used Twirl on {target.name}!")
                damage = 10
                if target.has_status('Infiltrated'):
                    damage = infiltrated(damage)
                target.take_damage(damage)
                print(f'{target.name} took {damage} damage.')
            else:
                print('The attack missed!')
        else:
            if accuracy(50, target) == True:
                print(f"{self.name} used Balloon Entanglement on {target.name}!")
                damage = 20
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
        print('Finally, you see a haunted amalgamation of wires and memories emerge from the shadows.')
        time.sleep(3)
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
            print('Or has he?')
            time.sleep(2)
            print('Springtrap: Did you really think this would be enough to finish me?')
            time.sleep(2)
            print('Springtrap: I am the embodiment of your fears and uncertainties, now merged and given form.')
            time.sleep(3)
            print('Springtrap: You forget,')
            time.sleep(3)
            print('Springtrap: I always come back.')
            time.sleep(4)
            print('You watch as the decaying bunny is encapsulated in digital code, turning him into another bunny with stitches running down his sides as he chuckles.')
            time.sleep(5)
            print('Glitchtrap: The time of reckoning, has begun.')
    
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
            print(f'{target.name} was traumatised and stared in disgust.')
    
#Characters
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
        is_use = input("Use an item? Y/N: ")
        return is_use.lower()
                    
    def use_item(self, item):
        global player_inventory
        for it in player_inventory:
            if it['name'] == item:
                if not it['consumable']: #If item can't be consumed
                    print("You can't consume this item.")
                    return False
                if it['type'] == 'healing': #If item is healing
                    self.heal(it['heal'])
                    player_inventory.remove(it)
                    return True 
                elif it['type'] == 'weapon': #If item is weapon
                    if self.items_equipped != None:
                        print('You already have a weapon equipped.')
                        return False
                    else:
                        self.items_equipped.append(it)
                        name = it['name']
                        print(f'{self.name} has equipped {name}.')
                        player_inventory.remove(it)
                        return True 
        print("You don't have this item.")
        return False

    def heal(self, amnt):
        self.health += amnt
        print(f"{self.name} healed {amnt} hp!")

    def take_damage(self, damage_taken):
        self.health -= damage_taken

    def is_defeated(self):
        if self.health <= 0:
            return True
        return False
            
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
        print("Type 'back' to cancel the attack. Use the numbers corresponding to each ability to attack.")
        atk = input("Select an attack to use: ")
        return atk.lower()

    def attack(self, target, atk):
        damage = 0
        damage += self.passive(target)
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

            
    def passive(self, target):
        if target.has_status('Sleeping'):
            return 5
        else:
            return 0
            
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
    def __init__(self, status=None, health=100, inventory=None):
        self.name = 'Bonnie'
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
        is_use = input("Use an item? Y/N: ")
        is_use = is_use.lower()
        while is_use != 'y' and is_use != 'n':
            print("Type 'Y' or 'N'.")
            is_use = input("Use an item? Y/N: ")
        if is_use == 'n':
            return False
        elif is_use == 'y':
            return True
                    
    def use_item(self, item):
        global player_inventory
        for it in player_inventory:
            if it['name'] == item:
                if not it['consumable']: #If item can't be consumed
                    print("You can't consume this item.")
                    return False
                if it['type'] == 'healing': #If item is healing
                    self.heal(it['heal'])
                    player_inventory.remove(it)
                    return True 
                elif it['type'] == 'weapon': #If item is weapon
                    if self.items_equipped != None:
                        print('You already have a weapon equipped.')
                        return False
                    else:
                        self.items_equipped.append(it)
                        name = it['name']
                        print(f'{self.name} has equipped {name}.')
                        player_inventory.remove(it)
                        return True 
        print("You don't have this item.")
        return False

    def heal(self, amnt):
        self.health += amnt
        print(f"{self.name} healed {amnt} hp!")

    def take_damage(self, damage_taken):
        self.health -= damage_taken

    def is_defeated(self):
        if self.health <= 0:
            return True
        return False
            
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
        print(f"{self.name}'s attacks:'")
        print('1. Rift  90 acc  15 dmg')
        print('2. Guitar crash  40 acc - dmg')
        print("3. Rock 'n' Roll  19 acc 87 dmg")
        print("Type 'back' to cancel the attack. Use the numbers corresponding to each ability to attack.")
        atk = input("Select an attack to use: ")
        return atk.lower()

    def attack(self, target, atk):
        damage = 0
        damage += self.passive(target)
        damage += self.item_equipped['damage']
        if atk == '1':
            print(f'{self.name} used Rift on {target.name}!')
            if accuracy(90, target) == True:
                damage += 15
                print(f"{target.name} took {damage} damage!")
                target.take_damage(damage)
            else:
                print('The attack missed!')
        if atk == '2':
            print(f'{self.name} used Guitar Crash on {target.name}!')
            if accuracy(40, target) == True:
                damage += 10
                self.heal(10)
                print(f"{target.name} took {damage} damage!")
                target.add_status('Resonance', 3)
                target.take_damage(damage)
                print(f"{self.name}'s attack leaves a resonating aura around {target.name}!")
            else:
                print('The attack missed!')
        if atk == '3':
            print(f"{self.name} used Rock 'n' Roll on {target.name}!")
            if accuracy(40, target) == True:
                hits = random.randint(1, 5)
                damage += 25*hits
                print(f'{target.name} was hit {hits} times!')
                print(f"{target.name} took {damage} damage!")
                target.take_damage(damage)
            else:
                print('The attack missed!')

            
    def passive(self, target):
        if target.has_status('Resonance'):
            multiplier = random.randint(1, 10)
            return multiplier
        else:
            return 0
            
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




class Foxy:
    def __init__(self, status=None, health=100, inventory=None):
        self.name = 'Foxy'
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
        is_use = input("Use an item? Y/N: ")
        is_use = is_use.lower()
        while is_use != 'y' and is_use != 'n':
            print("Type 'Y' or 'N'.")
            is_use = input("Use an item? Y/N: ")
        if is_use == 'n':
            return False
        elif is_use == 'y':
            return True
                    
    def use_item(self, item):
        global player_inventory
        for it in player_inventory:
            if it['name'] == item:
                if not it['consumable']: #If item can't be consumed
                    print("You can't consume this item.")
                    return False
                if it['type'] == 'healing': #If item is healing
                    self.heal(it['heal'])
                    player_inventory.remove(it)
                    return True 
                elif it['type'] == 'weapon': #If item is weapon
                    if self.items_equipped != None:
                        print('You already have a weapon equipped.')
                        return False
                    else:
                        self.items_equipped.append(it)
                        name = it['name']
                        print(f'{self.name} has equipped {name}.')
                        player_inventory.remove(it)
                        return True 
        print("You don't have this item.")
        return False

    def heal(self, amnt):
        self.health += amnt
        print(f"{self.name} healed {amnt} hp!")

    def take_damage(self, damage_taken):
        self.health -= damage_taken
    
    def is_defeated(self):
        if self.health <= 0:
            return True
        return False
            
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
        print(f"{self.name}'s attacks:'")
        print('1. Yar-Har  90 acc  15 dmg')
        print('2. Harvest Moon  - acc - dmg')
        print("3. Death Grip  25 acc 125 dmg")
        print("Type 'back' to cancel the attack. Use the numbers corresponding to each ability to attack.")
        atk = input("Select an attack to use: ")
        return atk.lower()

    def attack(self, target, atk):
        damage = 0
        damage += self.item_equipped['damage']
        if atk == '1':
            print(f'{self.name} used Yar-Har on {target.name}!')
            if accuracy(90, target) == True:
                damage += 15
                self.passive(damage)
                if self.has_status('Nightfall'):
                    damage += 15
                    self.heal(20)
                    print(f"{self.name} leeched {target.name}'s health!")
                print(f"{target.name} took {damage} damage!")
                target.take_damage(damage)
                
            else:
                print('The attack missed!')
        if atk == '2':
            print(f'{self.name} used Harvest Moon!')
            print(f"{self.name}'s attack and accuracy rose!")
            self.add_status('Nightfall', 5)
        if atk == '3':
            print(f"{self.name} used Death Grip on {target.name}!")
            if accuracy(25, target) == True:
                damage += 125
                self.passive(damage)
                if self.has_status('Nightfall'):
                    damage += 15
                    self.heal(20)    
                    print(f"{self.name} leeched {target.name}'s health!")
                print(f"{target.name} took {damage} damage!")
                target.take_damage(damage)
            else:
                print('The attack missed!')

            
    def passive(self, damage):
        if self.health < 50:
            damage = instinct(damage)
            return damage
        else:
            return 0
            
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



class Chica:
    def __init__(self, status=None, health=100, inventory=None, cupcake=None):
        self.name = 'Chica'
        self.health = health
        self.status = status if status is not None else []
        self.item_equipped = None
        self.cupcake = cupcake

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
        is_use = input("Use an item? Y/N: ")
        is_use = is_use.lower()
        while is_use != 'y' and is_use != 'n':
            print("Type 'Y' or 'N'.")
            is_use = input("Use an item? Y/N: ")
        if is_use == 'n':
            return False
        elif is_use == 'y':
            return True
                    
    def use_item(self, item):
        global player_inventory
        for it in player_inventory:
            if it['name'] == item:
                if not it['consumable']: #If item can't be consumed
                    print("You can't consume this item.")
                    return False
                if it['type'] == 'healing': #If item is healing
                    self.heal(it['heal'])
                    player_inventory.remove(it)
                    return True 
                elif it['type'] == 'weapon': #If item is weapon
                    if self.items_equipped != None:
                        print('You already have a weapon equipped.')
                        return False
                    else:
                        self.items_equipped.append(it)
                        name = it['name']
                        print(f'{self.name} has equipped {name}.')
                        player_inventory.remove(it)
                        return True 
        print("You don't have this item.")
        return False

    def heal(self, amnt):
        self.health += amnt
        print(f"{self.name} healed {amnt} hp!")

    def take_damage(self, damage_taken):
        if self.cupcake <= 0:
            self.health -= damage_taken
            self.cupcake = None
        else:
            self.cupcake -= damage_taken
        
    def is_defeated(self):
        if self.health <= 0:
            return True
        return False
            
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
        print(f"{self.name}'s attacks:'")
        print('1. Pizza slice  90 acc  15 dmg')
        print('2. Cupcake decoy  - acc - dmg')
        print("3. Devour  69 acc 30 dmg")
        print("Type 'back' to cancel the attack. Use the numbers corresponding to each ability to attack.")
        atk = input("Select an attack to use: ")
        return atk.lower()

    def attack(self, target, atk):
        damage = 0
        damage += self.passive(target)
        damage += self.item_equipped['damage']
        if atk == '1':
            print(f'{self.name} used Pizza slice on {target.name}!')
            if accuracy(90, target) == True:
                damage += 15
                print(f"{target.name} took {damage} damage!")
                target.take_damage(damage)
            else:
                print('The attack missed!')
        if atk == '2':
            if self.cupcake != 0:
                print(f'{self.name} used Cupcake decoy!')
                print(f'{self.name} placed a cupcake in place of her.')
                self.cupcake = 0
                self.cupcake += 50
            else:
                print('There is already a cupcake in place!')
        if atk == '3':
            print(f"{self.name} used Devour on {target.name}!")
            if accuracy(40, target) == True:
                if self.use_item() == True:
                    damage += 125
                    print(f"{target.name} took {damage} damage!")
                else:
                    damage += 30
                    print(f"{target.name} took {damage} damage!")
                target.take_damage(damage)
            else:
                print('The attack missed!')

            
    def passive(self, target):
        if self.cupcake <= 0:
            target.take_damage(20)
            print(f'The cupcake exploded and dealt 20 damage to {target.name}!')
        else:
            self.heal(10)
            print(f"The cupcake healed {self.name}'s HP!")
            
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