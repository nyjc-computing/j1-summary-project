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
wooden_helmet = Armor("helm", ["Wooden helmet", 1, 1, 1])
wooden_chestplate = Armor("chest", ["Wooden chestplate", 3, 1, 2])
wooden_leggings = Armor("leg", ["Wooden leggings", 2, 1, 1])
wooden_boots = Armor("boots", ["Wooden boots", 1, 1, 1])

iron_helmet = Armor("helm", ["Wooden helmet",  2, 1, 1])
iron_chestplate = Armor("chest", ["Wooden chestplate", 6, 1, 2])
iron_leggings = Armor("leg", ["Wooden leggings", 4, 1, 1])
iron_boots = Armor("boots", ["Wooden boots", 2, 1, 1])

diamond_helmet = Armor("helm", ["Diamond helmet", 3, 1, 1])
diamond_chestplate = Armor("chest", ["Diamond chestplate", 9, 1, 2])
diamond_leggings = Armor("leg", ["Diamond leggings", 6, 1, 1])
diamond_boots = Armor("boots", ["Diamond boots", 3, 1, 1])







class Weapon:
    def __init__(self, data: list):#attack, critc, name, num, spec_weight

        self.section = 'weapon'
        self.attack = data[0]
        self.critc = data[1]
        self.name = data[2]
        self.num = data[3]
        self.weight = data[4] * self.num


    def __repr__(self):
        return f"Att:{self.attack} Crit:{self.critc}% Name:{self.name}"

    def crit(self):
        x = random.randint(1, 100)
        if x <= self.critc:
            return True
        return False

    def combat(self, enemy, Player):
        crit = 1  #if there is no crit does not change
        if self.crit():
            crit = 2  # double the damage when it crits
        damage = (self.attack + Player.attack - enemy.defense) * crit
        if damage < 0:
            damage = 1
        enemy.health -= damage
        print(f"You dealt {damage} damage to the {enemy.name}.")
        print(f"{enemy.name} current health:{enemy.health}")
        if enemy.health <= 0:
            enemy.health = 0
            print(f"{enemy} fainted.")
            


#Weapon list
#format   att, critc
wooden_sword = Weapon([3, 5, "Wooden Sword", 1, 2])
stone_sword = Weapon([5, 5, "Stone Sword", 1, 3])
iron_sword = Weapon([8, 10, "Iron Sword", 1, 4])



steel_sword = Weapon([12, 8, "Steel Sword", 1, 5])
sword_of_baguette = Weapon([8, 28, "Bagutte Sword?", 1, 1])



fire_blade = Weapon([20, 5, "Fire Blade", 1, 0])
ice_blade = Weapon([12, 50, "Ice Blade", 1, 2])

diamond_sword = Weapon([25, 12, "Diamond Sword", 1, 2])
forty_metre_long_sword = Weapon([40, 40, "40m-long-sword", 1, 40])

soul_stealer = Weapon(
    [5, 5, "Soul Stealer", 1, 0])  #steal the attack of enemy and add it to weapon's attack.

#fire blade does half of the damage dealt to the enemy, last 2 turns

#dev weapon
ulti_blade = Weapon([100000000000000, 0, "Ulti-Blade", 1, 0])

#Armors #wood 1, iron 2, diamond 3
#helm, boots 1, legs 2, chest 3

iron_helmet = Armor('helm', ['iron_helmet', 2, 1, 10])
iron_chestplate = Armor('chest', ['iron_chestplate', 6, 1, 16])
iron_leggings = Armor('leg', ['iron_leggings', 4, 1, 14])
iron_boots = Armor('boots', ['iron_boots', 2, 1, 8])

diamond_helmet = Armor('helm', ['diamond_helmet', 3, 1, 5])
diamond_chestplate = Armor('chest', ['diamond_chestplate', 9, 1, 8])
diamond_leggings = Armor('leg', ['diamond_leggings', 6, 1, 7])
diamond_boots = Armor('boots', ['diamond_boots', 3, 1, 4])

class Potions:
    def __init__(self, data):
        self.desc = data[0]
        self.buff = data[1]
        self.type = data[2]
        self.name = data[3]
        self.num = 1
        
    def __repr__(self):
        return self.desc 

    def potion_buff(self, player):
        if self.type == "healing":
            player.health += self.buff
            
        elif self.type == "attack":
            player.attack += self.buff
            
        elif self.type == "speed":
            player.speed += self.buff
            
        elif self.type == "all-in-one":
            player.health += self.buff
            player.attack += self.buff
            player.speed += self.buff
            player.defense += self.buff
            

#Potion list
lesser_healing_potion = Potions(["Heals 2 hp to the player", 2, "healing", "lesser healing potion"])
normal_healing_potion = Potions(["Heals 5 hp to the player", 5, "healing", "normal healing potion"])
greater_healing_potion = Potions(["Heals 10 hp to the player ", 10, "healing", "greater healing potion"])
supreme_healing_potion = Potions(["Heals 20 hp to the player", 20, "healing", "supreme healing potion"])


strength_potion = Potions(["Add 10 att to the player's strength stats", 10, "attack", "strength potion"])
speed_potion = Potions(["Add 5 speed to the player's speed stats", 5, "speed", "speed potion"])
almond_potion = Potions(["Add 2 to each of the player's stat", 2, "all-in-one", "almond potion"])
bleach = Potions(["Kills you instantly, toddler approved!", -9999999999999, "health", "Bleach ninety-year war", -9999999999999])


