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

class Player:
    def __init__(self, name, slots):
        self.name = str(name)
        self.max_health = 10
        self.current_health = 10
        self.defense = 0
        self.attack = 1
        self.speed = 1
        self.items = {}
        self.backpack_size = slots
        
    def __repr__(self):
        return f"Name: {self.name}"
    #Backpack
    def store(self, name, object):
        if self.name in self.items: #same type items stack
            self.items[name].num += object.num
            print(f'{name} * {object.num} has been stored')
            return

        if len(self.items) >= self.backpack_size: #backback full
            print("Backpack is full!")
            return

        self.items[name] = object #normal store with sufficient space
        print(f'{name} * {object.num} has been stored.')
        return

    def display(self):
        lst = [i for i in self.items.keys()]
        disp = ', '.join(lst) #all items in backpack
        return disp

    def check(self, item):
        if item in self.items.keys():
            print(f'Name: {item}')
            print(f'Amount:{self.items[item].num}')
            print(f'Description:{self.items[item].desc}')
            return
        print('Item not in Backpack')
        return
    #Gears
    def equip(self, gear):
        if gear not in self.items:
            print("You don't have that gear!")
        
class Object:
    def __init__(self, num, desc):
        self.num = num
        self.desc = desc


class Enemy:
    def __init__(self, type):
        if type == "Brute":
            self.name = "Brute"
            self.health, self.attack, self.defense = 10, 2, 1
        elif type == "Armored Gorilla":
            self.name = "Armored Gorilla"
            self.health, self.attack, self.defense = 10, 0, 1000
        else:
            self.health, self.attack, self.defense = 5, 1, 0

