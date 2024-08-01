class Player:
    def __init__(self, name):
        self.name = str(name)
        self.health = 10
        self.defense = 0
        self.attack = 1
        self.dodge = 0.05 #5%
        self.speed = 1
        self.crit_chance = 0.05 
        self.crit_dmg = 2 #200%

    def __repr__(self):
        return f"Name: {self.name}"

class Backpack:
    pass
        

class Object:
    def __init__(self, num, desc):
        self.num = num
        self.desc = desc


class Enemy:
    def __init__(self, type):
        if type == "Brute":
            self.health, self.attack, self.defense = 10, 2, 1
        else:
            self.health, self.attack, self.defense = 5, 1, 0
    def attack(self, player_obj):
        pass
