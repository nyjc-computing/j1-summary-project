class Player:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.defense = 0
        self.attack = 1
        self.dodge = 0.05 #5%
        self.speed = 1
        self.crit_chance = 0.05 
        self.crit_dmg = 2 #200%
    
        
class Object:
    def __init__(self, amount, desc):
        self.amount = amount
        self.desc = desc
