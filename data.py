#File for data designer

import json
import random

NORTH = "NORTH"
SOUTH = "SOUTH"
WEST = "WEST"
EAST = "EAST"


labsize = 10
class Labyrinth:
    def __init__(self):
        self.lab = [[None] * labsize] * labsize
        self.boss_pos = [-1, -1] # Decided upon generation
        self.steve_pos = [-1, -1] # Decided upon generation

    def generate(self):
        raise NotImplementedError
    
    def move_steve(self, dir) -> None:
        raise NotImplementedError
        if dir == NORTH:
            return None

    def move_boss(self, dir):
        raise NotImplementedError

    def _can_move_here(self, coords: list(int), dir):
        x, y = coords
        if dir == NORTH:
            return False

class Room:
    def __init__(self, x: int, y: int):
        self.coords = [x, y]
        self.type = 




class Item:
    def __init__(self):
        self.info = {}
        for i in ["name", "item type", "description"]:
            self.info[i] = None

    def __repr__(self) -> str:
        outputstr = ''
        for key, value in self.info.items():
            outputstr += key.capitalize() + ": " + value
        return outputstr

    def __str__(self) -> str:
        outputstr = ''
        for key, value in self.info.items():
            outputstr += key.capitalize() + ": " + value
        return outputstr

    def set_nametypedesc(self, name: str, type: str, desc: str) -> None:
        self.info["name"] = name
        self.info["type"] = type
        self.info["description"] = desc


DEFAULT_HITPOINTS = 20
class Steve:
    def __init__(self, n: int):
        self._inventory = [] # list of dict
        # each dict in self.inventory describes an item, as well as the number of it in the inventory.
        # e.g. {"item": Health_Potion, "number": 2}
        # There should NOT be duplicate dicts in self.inventory e.g. 2 different dicts in self.inventory with "item" being Health_Potions
        self.inv_slots_num = n
        self.armour = {}
        for slot in ["helmet", "chestplate", "leggings", "boots"]:
            self.armour[i] = None
        self.health = DEFAULT_HITPOINTS

    def __repr__(self):
        return f"Steve has {self.heatlh} HP."

    def _display_inventory(self) -> None:
        raise NotImplementedError

    def _add_item_to_inv(new_item: Item, num: int) -> None:
        for index, dict_ in enumerate(self._inventory): # Linear search through inventory
            if str(new_item) == str(dict_["item"]): # new_item is already in the inventory
                self._inventory[index]["number"] += num
                return None
        # If exit loop, inventory does not have any of new_item
        # create a dict to add to self.inventory
        self.inventory.append({"item": new_item, "number": num})
        return None

    def _discard_item(item: Item, num: int) -> None:
        raise NotImplementedError

    def _use_item_from_inv(item: Item) -> None:
        raise NotImplementedError

    def _equip_armour(self, armour_item: Item) -> None:
        raise NotImplementedError
        
    def _get_hurt(self, damage: int):
        raise NotImplementedError

    def isdead(self) -> bool:
        if self.health <= 0:
            return True
        return False
                

class Creature:
    def __init__(self, ...):
        self._name = 



    def _getname():
        return self.name

with open("content/items.json", "r") as f:
    items = json.load(f)
