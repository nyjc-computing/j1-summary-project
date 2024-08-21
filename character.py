

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
from item import Gear

from typing import Any, Dict

import item
import time


class Player:
    def __init__(self, name):
        self.name = str(name)
        self.max_health = 10
        self.current_health = 10
        self.defense = 0
        self.attack = 1
        self.speed = 1
        self.coords = (0, 0)
        self.last_move = (0, 0)
        self.event_queue = ""
        self.items = {}
        self.mload = 10

        self.gears: Dict[str, Any]= {
            'helm': None, 
            'chest': None, 
            'leg': None, 
            'boots': None, 
            'weapon': item.wooden_sword
        }

        
    def __repr__(self):
        return f"Name: {self.name}"
        



    def backpack_isFull(self):
        total = 0
        for item in self.items.values():
            total += item.num
        return total >= self.backpack_size



    def store(self, object):
        if self.backpack_isFull():
            print("Unable to store. Backpack is full.")
        else:
            if object.name in self.items: #item present
                self.items[object.name].num += object.num
                
                weight = 0
                for item in self.items.values():
                    weight += item.weight
                if weight > self.mload:
                    print("That's too much for your bag to handle!")
                    
                    self.items[object.name].num -= object.num #Take back item
                    return False
                    
                print(f'{object.num} {object.name} has been stored')
                return True
            
            else: #new item
                self.items[object.name] = object
                
                total = 0
                for item in self.items.values():
                    total += item.weight
                if total > self.mload:
                    print("That's too much for your bag to handle!")
                    del self.items[object.name]
                    return False
                    
                print(f'{object.num} {object.name} has been stored.')

        

                return True
            return False




    def display(self):
        lst = [i for i in self.items.keys()]
        disp = ', '.join(lst) #all items in backpack
        return disp


    def check(self, item):
        if item in self.items.keys():
            print(f'Name: {item}')
            print(f'Amount:{self.items[item].num}')
            print(f'Description:{self.items[item].desc}')
            return True
        print('Item not in Backpack')
        return False

    #Gears
    def equip(self, gear: 'Armor'):
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
        return True


class Object:
    def __init__(self, name, num, description):
        self.name = name
        self.num = num
        self.description = description


    def unequip(self, section):
        if self.gears[section] is None:
            print('Nothing is equipped there.')
            return False
            
        if self.store(self.gears[section]) is False:
            print(f'Backpack Full! {section} cannot be unequipped!')
            return False 
            
        self.store(self.gears[section])
        self.gears[section] = None
        print(f'{self.gears[section].name} unequipped')
        return True

    def combat(self, enemy: "Enemy"):
        print("\n")
        time.sleep(0.5)
        crit = 1  #if there is no crit does not change
        
        if self.gears["weapon"].crit():
            crit = 2  # double the damage when it crits
            
        damage = (self.gears['weapon'].attack + self.attack - enemy.defense) * crit
        
        if damage < 0:
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


class Enemy:
    def __init__(self, type):
        if type == "Brute":
            self.name = "Brute"
            self.health, self.attack, self.defense = 10, 2, 1
        elif type == "Armored Gorilla":
            self.name = "Armored Gorilla"
            self.health, self.attack, self.defense = 10, 1, 1000
        elif type == "Slime":
            self.health, self.attack, self.defense = 5, 1, 0






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


        if damage < 0:
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


        if damage < 0:
            damage = 1

        player.health -= damage #lose health

        print(f"You received {damage} damage from the {self.name}.")#print damage to player


        print(f"{player.name} current health:{player.health}") #print hp left

        if player.health <= 0:
            player.health = 0
            print("You fainted. Skill Issue.")
            return -666
        else:
            return False
        