class Player:
    def __init__(self, name, slots):
        self.name = str(name)
        self.health = 10
        self.defense = 0
        self.attack = 1
        self.dodge = 0.05 #5%
        self.speed = 1
        self.crit_chance = 0.05 
        self.crit_dmg = 2 #200%
        #Backpack
        self.items = {}
        self.backpack_size = slots
        #Gears
        self.gears = {'Helmet': None, 'Chestplate': None, 'Leggings': None, 'Boots': None, 'Weapons': None, 'Accessories': None}
        
    def __repr__(self):
        return f"Name: {self.name}"
        
    #Backpack
    def store(self, item):#item is an object
        name = item.name
        if name in self.items: #same type items stack
            self.items[name].num += item.num
            print(f'{name} * {item.num} has been stored')
            return True

        if len(self.items) >= self.backpack_size: #backback full
            print("Backpack is full!")
            return False

        self.items[name] = item #normal store with sufficient space
        print(f'{name} * {item.num} has been stored.')
        return True

    def display(self):
        lst = [i for i in self.items.keys()]
        disp = ', '.join(lst) #all items in backpack
        return disp

    def check(self, item_name):
        if item_name in self.items.keys():
            print(f'Name: {item_name}')
            print(f'Amount:{self.items[item_name].num}')
            print(f'Description:{self.items[item_name].desc}')
            return True
        print('Item not in Backpack')
        return False
        
    #Gears
    def equip(self, gear: 'Item'):
        if gear.name not in self.items:
            print("You don't have that gear!")
            return False
        #if that section is full, say you have it on
        pass

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
        
class Item:
    def __init__(self, num, desc, name):
        self.name = name
        self.num = num
        self.desc = desc

class Enemy:
    def __init__(self, type):
        if type == "Brute":
            self.health, self.attack, self.defense = 10, 2, 1
        else:
            self.health, self.attack, self.defense = 5, 1, 0