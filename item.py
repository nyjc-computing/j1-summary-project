import random

class Item:
    def __init__(self, data: list):# name, desc, num, spec_weight
        self.name = data[0]
        self.desc = data[1]
        self.num = data[2]
        self.weight = data[3] * self.num
wooden_helmet = ["Wooden helmet", "nil", 1, 1]
wooden_chestplate = ["Wooden chestplate", "nil", 1, 2]
wooden_leggings = ["Wooden leggings", "nil", 1, 1]
wooden_boots = ["Wooden boots", "nil", 1, 1]

class Gear(Item):
    def __init__(self, section, data: list):
        super().__init__(data)
        self.section = section





class Weapon(Gear):
    def __init__(self, data: list):

        self.attack = data[0] 
        self.section = 'weapon'
        self.attack = data[0]
        self.critc = data[1]
        self.name = data[2]
        self.num = 1
        
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
Wooden_sword = Weapon([3, 5, "Wooden Sword"])
Stone_sword = Weapon([5, 5, "Stone Sword"])
Iron_sword = Weapon([8, 10, "Iron Sword"])


Steel_sword = Weapon([12, 8, "Steel Sword"])
Sword_of_baguette = Weapon([8, 28, "Bagutte Sword?"])

Fire_blade = Weapon([20, 5, "Fire Blade"])
Ice_blade = Weapon([12, 50, "Ice Blade"])

Diamond_sword = Weapon([25, 12, "Diamond Sword"])
Forty_metre_long_sword = Weapon([40, 40, "40m-long-sword"])

Soul_stealer = Weapon(
    [5, 5, "Soul Stealer"])  #steal the attack of enemy and add it to weapon's attack.

#fire blade does half of the damage dealt to the enemy, last 2 turns

#dev weapon
Ulti_blade = Weapon([100000000000000, 0, "Ulti-Blade"])



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
normal_healing_potion = ["Heals 5 hp to the player", 5, "healing", "normal healing potion"]
greater_healing_potion = ["Heals 10 hp to the player ", 10, "healing", "greater healing potion"]
supreme_healing_potion = ["Heals 20 hp to the player", 20, "healing", "supreme healing potion"]


strength_potion = Potions(["Add 10 att to the player's strength stats", 10, "attack", "strength potion"])
speed_potion = Potions(["Add 5 speed to the player's speed stats", 5, "speed", "speed potion"])
almond_potion = Potions(["Add 2 to each of the player's stat", 2, "all-in-one", "almond potion"])
bleach = Potions(["Kills you instantly, toddler approved!", -9999999999999, "health", "Bleach ninety-year war", -9999999999999])


