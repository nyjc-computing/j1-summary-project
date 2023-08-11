import random

#Rooms
class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.contents = []

    def enter(self):
        self.visited = True
        print(f"You have entered ({self.x}, {self.y}).")
    
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rooms = [[Room(x, y) for y in range(height)] for x in range(width)]

    def get_room(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.rooms[x][y]
        else:
            return None
            
def start_room() -> 'Room':
    pass
    

#Start
def start_menu():
    print('Welcome to FNAF:Reckoning!')
    choice = input("Type 'Start' to begin or 'Info' for more information: ")
    if choice.lower() == 'start':
        character_select()
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
    
def character_select():
    print('Characters:')
    print('1. Freddy Fazbear')
    print('2. Bonnie')
    print('3. Chica')
    print('4. Foxy')
    cr = input('Please select your character: ')
    if cr.lower() == 'freddy':
        print('You have selected Freddy Fazbear.')
    elif 'bonnie' in cr.lower():
        print('You have selected Bonnie.')
    elif 'chica' in cr:
        print('You have selected Chica.')
    elif 'foxy' in cr:
        print('You have selected Foxy.')
    else:
        print('Please enter a valid animatronic.')
        character_select()



#accuracy
def accuracy(hit_chance):
    miss_chance = random.randint(1, 100)
    if miss_chance > hit_chance:
        return False
    else:
        return True

#Characters and Enemies
class GB:
    def __init__(self, name, tag=None, counter=0, health=50, damage=0):
        self.name = name
        self.health = health
        self.counter = counter
        self.tag = tag if tag is not None else []
        self.damage = damage

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has died!")

    def add_tag(self, tag):
        self.tag.append(tag)

    def remove_tag(self, tag):
        if tag in self.tag:
            self.tag.remove(tag)

    def has_tag(self, tag):
        return tag in self.tag

    def attack(self, target):
        if 'sleep' in self.tag:
            print(f'{self.name} is asleep!')
            sleep(self)
            return
        else:
            print(f"{self.name} attacks {target.name}!")
            n = random.randint(1, 100)
            if n < 50:
                if accuracy(80) == True:
                    print(f"{self.name} used Bash!")
                    self.damage += 10
                    target.take_damage(self.damage)
                    self.damage -= 10
                else:
                    print('The attack missed!')
            else:
                if accuracy(80) == True:
                    print(f"{self.name} used Ram!")
                    self.damage += 15
                    target.take_damage(self.damage)
                    self.damage -= 15
                else:
                    print('The attack missed!')



class Freddy:
    def __init__(self, name, tag=None, counter=0, attacking=0, health=100, inventory=None):
        self.name = name
        self.health = health
        self.counter = counter
        self.tag = tag if tag is not None else []
        self.attacking = attacking
        self.inventory = inventory if inventory is not None else []

    def heal(self, amnt):
        self.health += amnt
        print(f"Freddy healed {amnt} hp!")

    def take_damage(self, damage_taken):
        self.health -= damage_taken
        print(f"Freddy took {damage_taken} damage!")
        print(f'HP left:{self.health}')
        if self.health <= 0:
            print('You died!')

    def inventory(self, item):
        print(f"{self.name}'s Inventory:")
        for item in self.inventory:
            print(item)

    def add_items(self, item):
        self.inventory.append(item)

    def attack(self, target):
            print(f"Freddy attacks {target.name}!")
            print('1. Mic Toss  90 acc  15 dmg')
            print('2. Sing  40 acc - dmg')
            print('3. The Bite  19 acc 87 dmg')
            atk = input("Please select an ability to use: ")
            if atk == '1':    
                print('Freddy used Mic Toss!')
                if accuracy(90) == True:
                    self.attacking += 15
                    print(f"{target.name} took {self.attacking} damage!")
                    target.take_damage(self.attacking)
                    self.attacking -= 15
                else:
                    print('The attack missed!')
            if atk == '2':
                print('Freddy used Sing!')
                if target.has_tag('sleep'):
                    print(f'{target.name} is already asleep!')
                    return
                else:
                    if accuracy(40) == True:
                        print(f"{target.name} fell asleep!")
                        target.add_tag('sleep')
                        sleep(target)
                    else:
                        print('The attack missed!')
            if atk == '3':
                print('Freddy used The Bite!')
                if accuracy(19) == True:
                    self.attacking += 87
                    print(f"{target.name} took {self.attacking} damage!")
                    target.take_damage(self.attacking)
                    self.attacking -= 87
                else:
                    print('The attack missed!')
            if atk < '1' or atk > '3':
                print('Please select a valid ability.')
                self.attack(target)
    
    def passive(self, target):
        if 'sleep' in target.tag:
            self.attacking += 5

    def add_tag(self, tag):
        self.tag.append(tag)

    def remove_tag(self, tag):
        if tag in self.tag:
            self.tag.remove(tag)

    def has_tag(self, tag):
        return tag in self.tag


#Turns
class Turn:
    def __init__(self, turn):
        self.turn = 1
        
    def turn_start(self):
        print(f'Turn {self.turn}')
    
    def turn_end(self):
        self.turn += 1


#Status
def sleep(target):
    if target.has_tag('sleep'):
        target.counter -= 1
    else:
        target.counter += 3
    while target.counter != 0:
        target.turn_end()
    target.remove_tag('sleep')