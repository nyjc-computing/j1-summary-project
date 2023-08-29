# importing from other files
from room import *
from character import *
from weapon import *
from spell import *

def setup() -> [Room, Character]:
    """
    Generates the map and the character and returns it in a list
    """

    # Generates the starting room 
    map = Dirtmouth()

    # Generates the character
    character = Character()

    # Sets the default statistics of the character
    character.spells.append(WingardiumLeviosa())
    character.weapon = Wand()
    character.weapons.append(character.weapon)
    character.health = 100
    character.max_health = 100
    character.mana = 50
    character.max_mana = 100
    character.health_flask = 2
    character.mana_flask = 2
    
    return [map, character]