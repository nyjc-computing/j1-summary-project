
class Gears:
    def __init__(self):
        self.helmet = (None)
        self.chestplate = (None)
        self.leggings = (None)
        self.boots = (None)
        self.accessories = (None)
        
        
class Backpack: #store, display, check, destroy
    def __init__(self, slots):
        self.items = {}
        self.backpack_size = slots

    def store(self, name, object):
        if name in self.items:
            self.items[name].num += object.num
            print(f'{name} * {object.num} has been stored')
            return
            
        if len(self.items) >= self.backpack_size:
            print("Backpack is full!")
            return
        self.items[name] = object
        print(f'{name} * {object.num} has been stored.')
        return
        
    def display(self):
        lst = [i for i in self.items.keys()]
        disp = ', '.join(lst)
        return disp

    def check(self, item):
        pass


from item import Item
from item import Armor



from typing import Any, Dict
import item
import time

class Player:
    def __init__(self, name):
        self.name = str(name)
        self.health = 30
        self.max_health = self.health
        self.defense = 0
        self.attack = 10
        self.speed = 1
        self.coords = (0, 0)
        self.last_move = (0, 0) #tracks the player's position last turn
        self.event_queue = None #stores the event that the player is moving to (e.g. enemy fight)
        self.items = {}
        self.mload = 10000000000000000000000 #fuck it who cares
        #hell yeah Matthew
        self.gears = {
            'helm': None, 
            'chest': None, 
            'leg': None, 
            'boots': None, 
            'weapon': item.wooden_sword
        }
    #item.wooden_sword
    def __repr__(self):
        return "P"
    def stats(self):
        print(f"Att:{self.attack}")
        print(f"Hp:{self.health}")
        print(f"Def:{self.defense}")
        print(f"Crit:{self.gears["weapon"].critc}%")
        
    def backpack_isFull(self):
        total = 0
        for itm in self.items.values():
            total += itm.weight
        return total >= self.mload

    def store(self, object):
        if not self.backpack_isFull():
            if object.name in self.items: #item present
                self.items[object.name].num += 1


                print(f'1 {object.name} has been stored')
                return True

            else: #new item
                self.items[object.name] = object
                self.items[object.name].num = 1

            

                print(f'1 {object.name} has been stored.')
                return True

        else:
            print("Unable to store. Backpack is full.")



    def display_inv(self):
        print("-----\nInventory\n")
        for i in self.items.keys():
            print(i, self.items[i].num)
        print("-----\n")

    def display_gears(self):
        print("-----\nGears\n")
        for i in self.gears.keys():
            print(f"{i}: {self.gears[i]}")
        print("-----\n")
        
    def check(self, object):
        if item in self.items.keys():
            print(f'Name: {item}')
            print(f'Amount:{self.items[item].num}')
            print(f'Description:{self.items[item].desc}')
            return True
        print('Item not in Backpack')
        return False

    def trash(self, object):
        if object.name not in self.items:
            print("Invalid object entered")
        else:
            self.items[object.name].num -= 1
            if self.items[object.name].num <= 0:
                del self.items[object.name]
    #Gears
    def equip(self, gear): #accepts object class
        if gear.name not in self.items:
            print("You don't have that gear!")
            return False
        #if that section is full, say you have it on

        if self.gears[gear.section] is not None:
            print(f'You already have a {gear.section} equipped.')
            return False

        #else, equip that gear
        self.gears[gear.section] = gear
        print(f'{gear.name} is equipped')
        if gear.section == "weapon":
            self.attack += gear.attack
        else:
            self.defense += gear.defense
        self.items[gear.name].num -= 1
        if self.items[gear.name].num == 0:
            del self.items[gear.name]
        return True

    def unequip(self, section): #accepts string of equipment type
        if self.gears[section] is None:
            print('Nothing is equipped there.')
            return False

        if self.backpack_isFull():
            print(f'Backpack Full! {section} cannot be unequipped!')
            return False 
        else:
            if section == "weapon":
                self.attack -= self.gears[section].attack
            else:
                self.defense -= self.gears[section].defense
            self.store(self.gears[section])
            print(f'{self.gears[section].name} unequipped')
            self.gears[section] = None
            return True
    
    def combat(self, enemy: "Enemy"):
        print("\n")
        time.sleep(0.5)
        crit = 1  #if there is no crit does not change

        if self.gears["weapon"].crit():
            crit = 2  # double the damage when it crits

        damage = (self.attack - enemy.defense) * crit

        if damage <= 0:
            damage = 1

        enemy.health -= damage

        print(f"You dealt {damage} damage to the {enemy.name}.")

        print(f"{enemy.name} current health:{enemy.health}")

        if enemy.health <= 0:
            enemy.health = 0
            print(f"{enemy} fainted.")
            if isinstance(enemy, Boss):
                return -888
            return True
        else:
            return False
    def use(self, life_crystal):
        print("You gained 10 hp!")
        self.health += life_crystal.buff
        del self.items[life_crystal.name]



class Enemy:
    def __init__(self, data: list): #name, health, defense, attack, speed
        self.name = data[0]
        self.health = data[1]
        self.defense = data[2]
        self.attack = data[3]
        self.speed = data[4]

    def __repr__(self):
        return "E"

    def combat(self, player: "Player"):

        print("\n")
        time.sleep(0.5)
        damage = (self.attack - player.defense) #enemy doesn't crit


        if damage <= 0:
            damage = 1

        player.health -= damage #lose health

        print(f"You received {damage} damage from the {self.name}.")#print damage to player


        print(f"{player.name} current health:{player.health}") #print hp left

        if player.health <= 0:
            player.health = 0
            print("You fainted. Skill Issue.")
            return -1
        else:
            return False

class Boss(Enemy):
    def __init__(self, data):
        super().__init__(data)

    def __repr__(self):
        return "B"

    def combat(self, player: "Player"):
        print("\n")
        time.sleep(0.5)
        damage = (self.attack - player.defense) #enemy doesn't crit


        if damage <= 0:
            damage = 1

        player.health -= damage #lose health

        print(f"You received {damage} damage from the {self.name}.")#print damage to player


        print(f"{player.name}'s current health:{player.health}") #print hp left

        if player.health <= 0:
            player.health = 0
            print("You fainted. Skill Issue.")
            return -666
        else:
            return False
