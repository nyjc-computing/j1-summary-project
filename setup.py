# importing from other files
from map import *
from character import *
from weapon import *
from spell import *

def setup() -> [Room, Character]:
    """
    Generates the map and the character and returns it in a list
    """

    map = Dirtmouth()
    character = Character()
    character.set_spells(WingardiumLeviosa())
    character.set_weapon(Wand())
    character.set_weapons(character.get_weapon())
    character.set_health(100)
    character.set_max_health(100)
    character.set_mana(100)
    character.set_max_mana(100)
    character.set_health_flask(2)
    character.set_mana_flask(2)
    
    return [map, character]