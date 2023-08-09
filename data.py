#Characters and Enemies
class Freddy:
    def __init__(self, name, attacking=0, health=100, inventory=None):
        self.name = name
        self.health = health
        self.attacking = attacking
        self.inventory = inventory if inventory is not None else []

    def heal(self, amnt):
        self.health += amnt
        print(f"Freddy healed {amnt} hp!")

    def dmg(self, damage_taken):
        self.health -= damage_taken
        print(f"Freddy took {damage_taken} damage!")
        if self.health <= 0:
            print('You died!')

    def inventory(self, item):
        print(f"{self.name}'s Inventory:")
        for item in self.inventory:
            print(item)

    def add_items(self, item):
        self.inventory.append(item)

    def attack(self, target):
        print('1. Mic Toss  90 acc  15 dmg                                                          2. Sing  40 acc - dmg                                                                3. The Bite  19 acc 87 dmg"')
        atk = input("Please select an ability to use: ")
        if atk == '1':    
            print('Freddy used Mic Toss!')
            #implement accuracy system
            self.attacking += 15
            print(f"{target.name} took {self.attacking} damage!")
            self.attacking -= 15
        if atk == '2':
            print('Freddy used Sing!')
            #implement accuracy system
            print(f"{target.name} fell asleep!")
            #enemy_tag.add(sleep)
        if atk == '3':
            print('Freddy used The Bite!')
            #implement accuracy system
            self.attacking += 87
            print(f"{target.name} took {self.attacking} damage!")
            self.attacking -= 87
        if atk < '1' or atk > '3':
            print('Please select a valid ability.')
            Freddy.attack()
    
    def passive(self):
        if Enemy.tag == sleep:
            self.attacking += 5

class Enemy:
    def __init__(self, name, tag=None, health=50, damage=10):
        self.name = name
        self.health = health
        self.damage = damage
        self.tag = tag

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has died!")
            
    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.damage)
        print(f"{target.name} took {self.damage} damage!")

    
