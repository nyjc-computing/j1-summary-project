from armour import *
from weapon import *
from accessory import *
from spell import *
from item import *

class Character:
    """
    A class that creates an instance of the game

    Attributes
    ----------
    - name : str
      Name of the player
    - health : int
      Amount of health the player has
    - max_health : int
      Maximum health of the player
    - spells : list[Spell]
      List of spells the player knows
    - attack : int
      Amount of extra damage the player deals
    - mana: int
      Amount of mana the player has
    - max_mana : int
      Maximum mana of the player
    - defence : int
      Amount of damage the player resists
    - armour : Armour
      The armour the player is wearing
    - armours : list[Armour]
      List of armours the player owns
    - weapon : Weapon
      The weapon the player is using
    - weapons : list[Weapon]
      List of weapons the player owns
    - accessory : Accessory
      The accessory the player is using
    - accessories : list[Accessory]
      List of accessories the player owns
    - health_flask : int
      Number of Flask of Crimson Tears the player owns
    - mana_flask : int
      Number of Flask of Cerulean Tears the player owns
    - items : list[Item]
      List of items the player owns


    Methods
    -------
    + set_name(self, name) -> None
    + get_name(self) -> str
    + set_health(self, health : int) -> None
    + get_health(self) -> int
    + set_max_health(self, max_health : int) -> None
    + get_max_health(self) -> int
    + set_defence(self, defence : int) -> None
    + get_defence(self) -> int
    + set_spells(self, spell : Spell) -> None
    + get_spells(self) -> list[Spell]
    + set_attack(self, attack : int) -> None
    + get_attack(self) -> int
    + set_mana(self, mana : int) -> None
    + get_mana(self) -> int
    + set_max_mana(self, max_mana : int) -> None
    + get_max_mana(self) -> int
    + set_weapon(self, weapon : Weapon) -> None:
    + get_weapon(self) -> Weapon
    + set_weapons(self, weapon : Weapon) -> None
    + get_weapons(self) -> list[Weapon]
    + set_armour(self, armour : Armour) -> None
    + get_armour(self) -> Armour
    + set_armours(self, armour : Armour) -> None
    + get_armours(self) -> list[Armour]
    + set_accessory(self, accessory : Accessory) -> None
    + get_accessory(self) -> Accessory
    + set_accessories(self, accessory : Accessory) -> None
    + get_accessories(self) -> list[Accessory]
    + set_health_flask(self, number : int) -> None
    + get_health_flask(self) -> int
    + set_mana_flask(self, number : int) -> None
    + get_mana_flask(self) -> int
    + set_items(self, item : Item) -> None
    + get_items(self) -> list[Item]

    """
    
    def __init__(self) -> None:
        self.name = ""
        self.health = 0
        self.max_health = 0
        self.spells = []
        self.attack = 0
        self.mana = 0
        self.max_mana = 0
        self.defence = 0
        self.armour = None
        self.armours = []
        self.weapon = None
        self.weapons = []
        self.accessory = None
        self.accessories = []
        self.health_flask = 0
        self.mana_flask = 0
        self.items = []

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
        
    def set_health(self, health : int) -> None:
        """Sets the character's health"""
        self.health = health

    def get_health(self) -> int:
        """Returns the character's health"""
        return self.health

    def set_max_health(self, max_health : int) -> None:
        self.max_health = max_health

    def get_max_health(self) -> int:
        return self.max_health

    def set_defence(self, defence : int) -> None:
        self.defence = defence

    def get_defence(self) -> int:
        return self.defence
        
    def set_spells(self, spell : Spell) -> None:
        self.spells.append(spell)

    def get_spells(self) -> list[Spell]:
        return self.spells

    def set_attack(self, attack : int) -> None:
        self.attack = attack

    def get_attack(self) -> int:
        return self.attack

    def set_mana(self, mana : int) -> None:
        self.mana = mana

    def get_mana(self) -> int:
        return self.mana

    def set_max_mana(self, max_mana : int) -> None:
        self.max_mana = max_mana

    def get_max_mana(self) -> int:
        return self.max_mana

    def set_weapon(self, weapon : Weapon) -> None:
        self.weapon = weapon

    def get_weapon(self) -> Weapon:
        return self.weapon

    def set_weapons(self, weapon : Weapon) -> None:
        self.weapons.append(weapon)

    def get_weapons(self) -> list[Weapon]:
        return self.weapons
        
    def set_armour(self, armour : Armour) -> None:
        self.armour = armour

    def get_armour(self) -> Armour:
        return self.armour

    def set_armours(self, armour : Armour) -> None:
        self.armours.append(armour)

    def get_armours(self) -> list[Armour]:
        return self.armours

    def set_accessory(self, accessory : Accessory) -> None:
        self.accessory = accessory

    def get_accessory(self) -> Accessory:
        return self.accessory

    def set_accessories(self, accessory : Accessory) -> None:
        self.accessories.append(accessory)

    def get_accessories(self) -> list[Accessory]:
        return self.accessories

    def set_health_flask(self, number : int) -> None:
        self.health_flask += number

    def get_health_flask(self) -> int:
        return self.health_flask

    def set_mana_flask(self, number : int) -> None:
        self.mana_flask += number

    def get_mana_flask(self) -> int:
        return self.mana_flask

    def set_items(self, item : Item) -> None:
        self.items.append(item)

    def get_items(self) -> list[Item]:
        return self.items

