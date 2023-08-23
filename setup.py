from map import *
from character import *
from spell import *

def setup():
    """
    Generates 3 rooms, named room1, room2, room3 and links them together
    """

    map = Dirtmouth()
    character = Character()
    character.set_spells(WingardiumLeviosa())
    character.set_health(100)
    character.set_attack(10)
    character.set_mana(100)
    
    return [map, character]