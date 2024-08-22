import random

class Item:
    def __init__(self, data: list):# name, num, desc, spec_weight
        self.name = data[0]
        self.num = data[1]
        self.desc = data[2]
        self.weight = data[3] * self.num


class Armor:
    def __init__(self, section, data: list):#name, defense, num, spec_weight
        self.section = section #helm, chest, leg, boots
        self.name = data[0]
        self.defense = data[1]
        self.num = data[2]
        self.weight = data[3] * self.num


    def __repr__(self):
        return f"{self.name}"
    
    def get_stats(self):
        return f"Item Description\n-----\nName: {self.name}\nDefense: {self.defense}\nItem Stack: {self.num}\nTotal Weight: {self.weight}\n-----"


class Weapon:
    def __init__(self, data: list):#attack, critc, name, num, spec_weight
        self.section = 'weapon'
        self.attack = data[0]
        self.critc = data[1]
        self.name = data[2]
        self.num = data[3]
        self.weight = data[4] * self.num

    def __repr__(self):
        return f"{self.name}"

    def get_stats(self):
        return f"Item Description\n-----\nName: {self.name}\nAttack: {self.attack}\nCrit Chance: {self.critc}\nItem Stack: {self.num}\nTotal Weight: {self.weight}\n-----"

    def crit(self):
        x = random.randint(1, 100)
        if x <= self.critc:
            return True
        return False

    

#Weapon list
#format   att, critc
wooden_sword = Weapon([5, 5, "Wooden Sword", 1, 2])
stone_sword = Weapon([8, 5, "Stone Sword", 1, 3])
iron_sword = Weapon([10, 10, "Iron Sword", 1, 4])

steel_sword = Weapon([12, 12, "Steel Sword", 1, 5])

fire_blade = Weapon([15, 10, "Fire Blade", 1, 0])
ice_blade = Weapon([10, 50, "Ice Blade", 1, 2])

diamond_sword = Weapon([20, 20, "Diamond Sword", 1, 2])
forty_metre_long_sword = Weapon([40, 40, "40m-long-sword", 1, 40])

soul_stealer = Weapon(
    [5, 5, "Soul Stealer", 1, 0])  #steal the attack of enemy and add it to weapon's attack.

#fire blade does half of the damage dealt to the enemy, last 2 turns

#dev weapon
ulti_blade = Weapon([100000000000000, 0, "Ulti-Blade", 1, 0])

#Armors #wood 1, iron 2, diamond 3
#helm, boots 1, legs 2, chest 3
wooden_helmet = Armor("helm", ["Wooden Helmet", 1, 1, 1])
wooden_chestplate = Armor("chest", ["Wooden Chestplate", 2, 1, 2])
wooden_leggings = Armor("leg", ["Wooden Leggings", 2, 1, 1])
wooden_boots = Armor("boots", ["Wooden Boots", 1, 1, 1])

iron_helmet = Armor('helm', ['Iron Helmet', 2, 1, 10])
iron_chestplate = Armor('chest', ['Iron Chestplate', 3, 1, 16])
iron_leggings = Armor('leg', ['Iron Leggings', 3, 1, 14])
iron_boots = Armor('boots', ['Iron Boots', 2, 1, 8])

diamond_helmet = Armor('helm', ['Diamond Helmet', 3, 1, 5])
diamond_chestplate = Armor('chest', ['Diamond Chestplate', 4, 1, 8])
diamond_leggings = Armor('leg', ['Diamond Leggings', 4, 1, 7])
diamond_boots = Armor('boots', ['Diamond Boots', 3, 1, 4])

class Boost:
    def __init__(self, data):
        self.name = data[0]
        self.buff = data[1]
        self.weight = data[2]
        self.num = data[3]

    def __repr__(self):
        return self.name

#Potion list
life_crystal = Boost(["Life Crystal", 10, 1, 1])



loot_table = [wooden_boots, wooden_chestplate, wooden_helmet, wooden_leggings, stone_sword, iron_helmet, iron_chestplate, iron_leggings, iron_boots, iron_sword, steel_sword,life_crystal, diamond_helmet, diamond_chestplate, diamond_leggings, diamond_boots, fire_blade, ice_blade, diamond_sword, forty_metre_long_sword]