from weapon import *

class Character:
    """
    creates the character

    Attribute
    ---------
    + name: str
    + health: int
    + spell: str
    + battle_points: int
    + potion: list
    + equip: class
    + item: list

    Method
    ------
    + set_health(): updates the character's health
    + get_health(): gets the health of the character
    - is_dead(): checks if the enemy is dead
    
    """
    def __init__(self) -> None:
        self.name = ""
        self.health = 0
        self.spells = []
        self.attack = 0
        self.mana = 0
        self.armour = None
        self.armours = []
        self.weapon = None
        self.weapons = []
        self.accessory = None
        self.accessories = []

    def set_name(self, name) -> None:
        """
        sets the name of the character
        """
        self.name = name

    def get_name(self) -> str:
        """
        gets the name of the character
        """
        return self.name
        
    def set_health(self, health) -> None:
        """Sets the character's health"""
        self.health = health

    def get_health(self) -> int:
        """Returns the character's health"""
        return self.health
        
    def set_spells(self, spell):
        self.spells.append(spell)

    def get_spells(self):
        return self.spells

    def set_attack(self, attack):
        self.attack = attack

    def get_attack(self):
        return self.attack

    def set_mana(self, mana):
        self.mana = mana

    def get_mana(self):
        return self.mana

    def set_weapon(self, weapon):
        self.weapon = weapon

    def get_weapon(self):
        return self.weapon

    def set_weapons(self, weapon):
        self.weapons.append(weapon)

    def get_weapons(self):
        return self.weapons
        
    def set_armour(self, armour):
        self.armour = armour

    def get_armour(self):
        return self.armour

    def set_armours(self, armour):
        self.armours.append(armour)

    def get_armours(self):
        return self.armours

    def set_accessory(self, accessory):
        self.accessory = accessory

    def get_accessory(self):
        return self.accessory

    def set_accessories(self, accessory):
        self.accessories.append(accessory)

    def get_accessories(self):
        return self.accessories