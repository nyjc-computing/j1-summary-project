import random

class Weapon:
    def __init__(self, data: list):
        self.attack = data[0]
        self.critc = data[1]
        
    def __repr__(self):
        return f"Att:{self.attack} Crit:{self.critc}%"
        
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
    
            
         #format   att, critc
Wooden_sword = Weapon([3, 5], )
Stone_sword = Weapon([5, 5])
Iron_sword = Weapon([8, 10])

Steel_sword = Weapon([12, 8])

Fire_blade = Weapon([20, 5])
Ice_blade = Weapon([12, 50])

Diamond_sword = Weapon([25, 12])

Soul_stealer = Weapon([5, 5]) #steal the attack of enemy and add it to weapon's attack.


#fire blade does half of the damage dealt to the enemy, last 2 turns


#dev weapon
Ulti_blade = Weapon([100000000000000, 0])
