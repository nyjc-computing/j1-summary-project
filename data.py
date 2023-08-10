import random

#Characters and Enemies

class Freddy:
    def __init__(self, name, attacking=0, health=100, inventory=None):
        self.name = name
        self.health = health
        self.attacking = attacking
        self.inventory = inventory if inventory is not None else []

    def heal(self, amnt):
        self.health += amnt
        print(f"Freddy healed {amnt} hp!")

    def take_damage(self, damage_taken):
        self.health -= damage_taken
        print(f"Freddy took {damage_taken} damage!")
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
            print('1. Mic Toss  90 acc  15 dmg                                                          2. Sing  40 acc - dmg                                                                3. The Bite  19 acc 87 dmg"')
            atk = input("Please select an ability to use: ")
            if atk == '1':    
                print('Freddy used Mic Toss!')
                #implement accuracy system
                self.attacking += 15
                print(f"{target.name} took {self.attacking} damage!")
                target.take_damage(self.attacking)
                self.attacking -= 15
            if atk == '2':
                print('Freddy used Sing!')
                #implement accuracy system
                print(f"{target.name} fell asleep!")
                target.add_tag('sleep')
            if atk == '3':
                print('Freddy used The Bite!')
                #implement accuracy system
                self.attacking += 87
                print(f"{target.name} took {self.attacking} damage!")
                target.take_damage(self.attacking)
                self.attacking -= 87
            if atk < '1' or atk > '3':
                print('Please select a valid ability.')
                Freddy.attack()
    
    def passive(self, target):
        if 'sleep' in target.tag:
            self.attacking += 5

class Enemy:
    def __init__(self, name, tag=None, health=50, damage=0):
        self.name = name
        self.health = health
        self.tag = tag if tag is not None else []
        self.damage = damage

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has died!")

    def add_tag(self, tag):
        self.tag.append(tag)
        #print(f"{self.name} has {self.tag}!")

    def remove_tag(self, tag):
        if tag in self.tag:
            self.tag.remove(tag)

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        n = random.randint(1, 100)
        if n < 50:
            print(f"{self.name} used Bash!")
            self.damage += 10
            target.take_damage(self.damage)
            self.damage -= 10
        else:
            print(f"{self.name} used Ram!")
            self.damage += 15
            target.take_damage(self.damage)
            self.damage -= 15


#Rooms
class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.contents = []

    def enter(self):
        self.visited = True
        print(f"You have entered room ({self.x}, {self.y}).")
    
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

#Start
def start_menu():
    print('Welcome to FNAF:Reckoning!')
    start = input("Type 'Start' to begin: ")

def character_select():
    print('Characters:')
    print('1. Freddy Fazbear')
    print('2. Bonnie')
    print('3. Chica')
    print('4. Foxy')
    cr = input('Please select your character: ')
    if cr == 'Freddy':
        print('You have selected Freddy Fazbear.')
    elif 'Bonnie' in cr:
        print('You have selected Bonnie.')
    elif 'Chica' in cr:
        print('You have selected Chica.')
    elif 'Foxy' in cr:
        print('You have selected Foxy.')
    else:
        print('Please enter a valid animatronic.')
        character_select()