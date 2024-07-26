import random
class Weapon:
    def __init__(self, data: list):
        self.attack = data[0]
        self.critc = data[1]
        self.rarity = data[2]
        self.passive = data[3]
    def __repr__(self):
        return f"Att:{self.attack} Crit:{self.critc}% Rarity:{self.rarity}"
        
    def crit(self):
        x = random.randint(1, 100)
        if x <= self.critc:
            return True
        return False
        
    def combat(self):
        crit = 1 #if there is no crit does not change
        if self.crit():
            crit = 2 # double the damage when it crits
        print(f"You dealt {self.attack * crit} damage to the enemy.")
    
            
        
Wooden_sword = Weapon([3,5, "Common", False], )
Stone_sword = Weapon([5, 5, "Common", False])
Iron_sword = Weapon([8, 10, "Uncommon", False])
Steel_sword = Weapon([12, 8, "Uncommon", False])
Fire_blade = Weapon([10, 5, "Rare", True])
#fire blade does half of the damage dealt to the enemy, last 2 turns
