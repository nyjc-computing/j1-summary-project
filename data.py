#File for data designer

import json
import random

NORTH = "NORTH"
SOUTH = "SOUTH"
WEST = "WEST"
EAST = "EAST"
NOVICE = "NOVICE"
JOURNEYMAN = "JOURNEYMAN"
MASTER = "MASTER"


labsize = 10
class Labyrinth:
    def __init__(self):
        self.lab = [[None] * labsize] * labsize
        self.difficulty_level = None
        self.boss_pos = [-1, -1] # Decided upon generation
        self.steve_pos = [-1, -1] # Decided upon generation

    def generate(self) -> None:
        raise NotImplementedError
        # self.difficulty_level = difficulty_level
        # put in empty rooms
        for x in range(labsize):
            for y in range(labsize):
                self.lab[x][y] = Room(x, y)
        # set up walls

        # choose position of Start room randomly

        # choose position of Monster room randomly
        
        # give the rooms random contents

    
    
    def move_steve(self, direction) -> bool:
        if _can_move_here(self.steve_pos):
            if direction == NORTH:
                return None
            if direction ==  SOUTH:
                return None
            if direction == EAST:
                return None
            if direction == WEST:
                return None

    def move_boss(self, direction):
        shuffled_dirlist = random.shuffle([NORTH, SOUTH, EAST, WEST])
        for randomdir in shuffled_dirlist:
            if  _can_move_here(boss_pos, randomdir):



                return None
                
            

    def _can_move_here(self, coords: list(int), direction):
        x, y = coords
        if x < 0 or x >= labsize or y < 0 or y >= labsize: # this should not happen at all
            raise IndexError("entity is not inside of maze")
        raise NotImplementedError
        if direction == NORTH:
            return False

    def _steve_useitem(item: Item) -> None:
        raise NotImplementedError

    def _monster_roar(self):
        raise NotImplementedError



class Room:
    def __init__(self, x: int, y: int, type):
        self.coords = [x, y]
        self.type = type
        self.creature = None
        if self.type == CREATURE:
            # randomly choose some creature from 



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
        self.info = {}
        for i in ["name", "max hitpoints", "moves"]:
            self.info[i] = None
        self.hitpoints = None
        


    def set_name(self, name: str) -> None:
        self.info["name"] = name

    def set_maxhp(self, maxhp: int) -> None:
        self.info["max hitpoints"] = maxhp
        self.hitpoints = maxhp

    def set_moves(self, moveslist: list) -> None:
        self.info["moves"] = moveslist

    def set_creature(self, moves)


class Monster(Creature):
    def __init__(self):
        

with open("content/items.json", "r") as f:
    items = json.load(f)
