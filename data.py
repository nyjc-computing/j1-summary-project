#File for data designer

import json
import random

NORTH = "NORTH"
SOUTH = "SOUTH"
WEST = "WEST"
EAST = "EAST"
# NOVICE = "NOVICE"
# JOURNEYMAN = "JOURNEYMAN"
# MASTER = "MASTER"
STARTROOM = "STARTROOM"
DIRLIST = [[0, 1], [0, -1], [1, 0], [-1, 0]] # according to N, S, E, W

#STANLEY TEST











def is_adjacent(room1: list[int], room2: list[int]) -> bool:
    xdiff = room1[0] - room2[0]
    ydiff = room1[1] - room2[1]
    for i in DIRLIST:
        if [xdiff, ydiff] == i:
            return True
    return False

def direction_of(targetcoords: list[int], neighbourcoords: list[int]) -> "NORTH or SOUTH or EAST or WEST":
    if not is_adjacent(targetcoords, neighbourcoords):
        return None
    xdiff = neighbourcoords[0] - targetcoords[0]
    ydiff = neighbourcoords[1] - targetcoords[1]
    if xdiff == 0:
        if ydiff == 1:
            return NORTH
        elif ydiff == -1:
            return SOUTH
    elif ydiff == 0:
        if xdiff == 1:
            return EAST
        if xdiff == -1:
            return WEST

labsize = 10 # cannot be too small!!
def valid_coords(roomcoords: list[int]) -> bool:
    if type(roomcoords) is not list:
        return False
    if len(roomcoords) != 2:
        return False
    i, j = roomcoords
    if i not in list(range(labsize)) or j not in list(range(labsize)):
        return False
    return True

class Labyrinth:
    """
    -- ATTRIBUTES --
    - lab: list[list[Room]]
    - difficulty_level
    - boss_pos: list[int]
    - steve_pos: list[int]

    -- METHODS
    + generate(self) -> None
    - generate_place_steve_boss() -> None:
    - generate_cmaze(startroom_pos: list) -> None:
    - generate_link_rooms(room1coords: list, room2coords: list) -> None:
    - generate_rooms_connected() -> bool:
    + move_boss(self) -> None:
    + can_move_here(self, coords: list(int), direction):
    + steve_useitem(self, item: Item) -> None
    + monster_roar(self) -> None
    
    """
    def __init__(self):
        nonelist = [None] * labsize
        self.lab = []
        for i in range(labsize):
            self.lab.append(nonelist.copy())
        self.difficulty_level = None
        self.boss_pos = [-1, -1] # Decided upon generation
        self.steve_pos = [-1, -1] # Decided upon generation
        self.posscoords = list(range(labsize))

    def __repr__(self):
        outputstr = ""
        for y in range(labsize):
            fulltopstr = ""
            fullmidstr = ""
            fullbottomstr = ""
            for x in range(labsize):
                room = self.lab[x][labsize - y - 1]
                N, S, E, W = room.get_neighbours_accessibility()
                if N:
                    topstr = " || "
                else:
                    topstr = "    "
                if S:
                    bottomstr = " || "
                else:
                    bottomstr = "    "
                if W:
                    midstr = "="
                else:
                    midstr = " "
                if room.steve_ishere():
                    midstr += "S"
                else:
                    midstr += "/"
                if room.boss_ishere():
                    midstr += "B"
                else:
                    midstr += "/"
                if E:
                    midstr += "="
                else:
                    midstr += " "
                fulltopstr += topstr
                fullmidstr += midstr
                fullbottomstr += bottomstr
            outputstr += fulltopstr + "\n" + fullmidstr + "\n" + fullbottomstr + "\n"
        return outputstr                    
                
                    

    def generate(self) -> None:
        """Generates a maze without walls"""
        for x in range(labsize):
            for y in range(labsize):
                self.lab[x][y] = Room(x, y)
        self._generate_place_steve_boss()
        self._generate_nowalls()

    def _generate_nowalls(self) -> None:
        for x in range(labsize):
            for y in range(labsize):
                this = self.lab[x][y]
                for i in range(4):
                    directionnum = DIRLIST[i]
                    neighbourx, neighboury = x + directionnum[0], y + directionnum[1]
                    if valid_coords([neighbourx, neighboury]):
                        neighbour = self.lab[neighbourx][neighboury]
                        direction = [NORTH, SOUTH, EAST, WEST][i]
                        this.connect_dir(direction, neighbour)
                                                     
        
    def generate_random(self) -> None:
        """Generates the maze by:
        1. Filling in empty rooms in the empty maze
        2. Chooses (somewhat) randomly which room is the startroom room where Steve is placed
        3. Places the boss room opposite to startroom
        4. Makes the rooms connected like a maze structure
        6. (Unimplemented functionality) Takes in a difficulty level and sets the game accordingly
        
        Requires the use of helper methods, namely:

        Too many LOL
        """
        # self.difficulty_level = difficulty_level
        # put in empty rooms
        for x in range(labsize):
            for y in range(labsize):
                self.lab[x][y] = Room(x, y)
        self._generate_place_steve_boss()
        self._generate_maze(self.steve_pos)
    

    def _generate_place_steve_boss(self) -> None:
        """One of many helper methods of the generate() method.

        Chooses a startroom somewhat randomly, places Steve there,
        and places the boss in a room opposite of startroom

        How startroom is chosen:
        - The possible rooms to be picked are rooms nearer to the perimeter than the center.
        - e.g. If the labyrinth is 10 by 10 rooms, the middle 6 by 6 rooms cannot be chosen as startroom. the surrounding 64 rooms can be chosen as rooms.
        - Of the 64 rooms nearing the far sides of the labyrinth, one room is chosen at random.
        - This means that labsize cannot be too small, or the generation may break. ie labsize cannot be less than 4.

        How bossroom is chosen:
        - e.g. labsize is set to 10 and startroom coords are [1, 7]
        - bossroom is at the opposite of the labyrinth at [8, 2]

        Startroom will be remembered throughout the game, the starting position of the boss will not be remembered. 
        """
        # choose position of Start room randomly
        n = labsize // 4
        n = random.randint(-n, n - 1) % labsize
        m = random.randint(0, labsize - 1)
        nm = [n, m]
        random.shuffle(nm)
        steve_x, steve_y = nm
        self.lab[steve_x][steve_y].settype_startroom()
        self.steve_pos = [steve_x, steve_y]
        
        # choose position of Monster room opposite to where steve is
        boss_x = labsize - 1 - (steve_x % labsize)
        boss_y = labsize - 1 - (steve_y % labsize)
        
        if (boss_x, boss_y) == (steve_x, steve_y): # if they happen to be placed in the same room
            raise ValueError("Steve and the Boss have been put at the same location.")
        self.lab[boss_x][boss_y].boss_enters()    

    def _generate_maze(self, startroom_pos: list[int]) -> None:
        # link up a large number of rooms
        print("Loading: Generating maze...")
        self._generate_recursive_linking(startroom_pos)
        unconnected = self._generate_count_unconnected_rooms()
        print("Loading: Tying loose ends...")
        while unconnected != 0:
            for x in range(labsize):
                for y in range(labsize):
                    room = self.lab[x][y]
                    if not room.is_connected_tostart():
                        self._generate_force_connect([x, y])
            unconnected = self._generate_count_unconnected_rooms()

    def _generate_force_connect(self, roomcoords: list[int]) -> None:
        """links holes in connectivity of maze to as many adjacent rooms as possible"""
        newdirlist = DIRLIST.copy()
        random.shuffle(newdirlist)
        for i in range(4):
            neighbourcoords = [roomcoords[0] + newdirlist[i][0], roomcoords[1] + newdirlist[i][1]]
            if valid_coords(neighbourcoords):
                self._generate_link_rooms(roomcoords, neighbourcoords) # forcing a connection.
                
    def _generate_is_linkable_by_recursive(self, roomcoords: list[int]) -> bool:
        if not valid_coords(roomcoords):
            return False
        x, y = roomcoords
        room_object = self.lab[x][y]
        if room_object.is_connected_tostart(): # has access to 
            return False
        return True
                     
    
    def _generate_recursive_linking(self, thisroomcoords: list[int]) -> None:
        """
        Attempts to link a large number of rooms, recursively
        Rules for whether a neighbour room is linkable:
        0. The room exists.
        1. The room is not already linked.

        thisroom will make an attempt to link to linkable neighbour rooms.
        The success of the attempt is based on chance.
        This chance can be changed, but is hardcoded.
        This chance should be quite high above 25%; the lower the odds, the more holes in connectivity, the more cleanup linking has to be done.
        
        """
        # current room should already be connected
        x, y = thisroomcoords
        thisroom = self.lab[x][y] # object thisroom object
        if not thisroom.is_connected_tostart():
            raise ValueError("Room that is trying to (recursively) link to others is not yet connected, should not happen.")
        # iteration through N, S, E, W:
        # checking whether they are linkable by rules
        # if linkable, there is a chance of linking
        for i in range(4):
            neighbourcoords = [x + DIRLIST[i][0], y + DIRLIST[i][1]]
            if self._generate_is_linkable_by_recursive(neighbourcoords):
                odds = random.randint(1, 100)
                if odds <= 58: # n% chance of linking; 
                    self._generate_link_rooms(thisroomcoords, neighbourcoords)
                    self._generate_recursive_linking(neighbourcoords) # recursion call
        # base case should be inherently built into this loop:
        # Recursion branch ends at a room where
        # 1. All adjacent rooms are not linkable
        # 2. By chance, the labyrinth chooses not to link this room to any other room.
    
    def _generate_link_rooms(self, room1coords: list[int], room2coords: list[int]) -> None:
        # validation
        x1, y1 = room1coords
        x2, y2 = room2coords
        if not valid_coords(room1coords) or not valid_coords(room2coords):
            raise IndexError("_generate_link_rooms(): a room passed in has coords outside of labyrinth. Cannot be linked.")
        if x1 == x2 and y1 == y2:
            raise IndexError("_generate_link_rooms(): the same room is passed twice, cannot be linked.")
        if not is_adjacent(room1coords, room2coords):
            raise IndexError("_generate_link_rooms(): non adjacent rooms are passed, cannot be linked.")
        # linking rooms
        room1 = self.lab[x1][y1]
        room2 = self.lab[x2][y2]
        if room1.is_connected_tostart() or room2.is_connected_tostart():
            room1.set_connected_True()
            room2.set_connected_True()
        if not room1.is_connected_tostart() and not room2.is_connected_tostart():
            # every linking must happen between rooms of which 1 MUST be connected.
            return None # no linking done if both are unconnected.
        # print(room1.coords) #xyzxyz
        # print(room2.coords) #xyzxyz
        room1.set_access(room2)
        room2.set_access(room1)
            
    
    def _generate_count_unconnected_rooms(self) -> int:
        """
        One of many helper methods of the generate() method.
        
        Linearly search the rooms to check whether the rooms are connected to the startroom.
        Returns the number of rooms that are not connected.
        
        """
        number_of_unconnected = 0
        for column in self.lab:
            for room in column:
                # room is an instance of the Room class
                if not room.is_connected_tostart():
                    number_of_unconnected += 1 # counter
        return number_of_unconnected

    def get_current_pos(self) -> "Room":
        return self.steve_pos


        

    def move_boss(self) -> None:
        dirlist = [NORTH, SOUTH, EAST, WEST]
        random.shuffle(dirlist)
        for randomdir in dirlist:
            if self.can_move_here(self.boss_pos, randomdir):
                x, y = self.boss_pos
                self.lab[x][y].boss_leaves()
                for i in range(4):
                    if randomdir == [NORTH, SOUTH, EAST, WEST][i]:
                        randomdir = DIRLIST[i]
                self.boss_pos = [x + randomdir[0], y + randomdir[1]]
                x, y = self.boss_pos
                self.lab[x][y].boss_leaves()
                return None
        raise RuntimeError(f"Boss cannot move because its room {self.boss_pos} is unlinked to neighbours.")
                
    def move_steve(self, direction) -> None:
        if not self.can_move_here(self.steve_pos, direction):
            raise ValueError("move_steve() attempted to move steve to a direction that is not possible.")
        for i in range(4):
            if direction == [NORTH, SOUTH, EAST, WEST][i]:
                direction = DIRLIST[i]
        x, y = self.steve_pos
        self.lab[x][y].steve_leaves()
        self.steve_pos = [x + direction[0], y + direction[1]]
        x, y = self.steve_pos
        self.lab[x][y].steve_enters()
        

    def can_move_here(self, this_coords: list[int], direction) -> bool:
        if not valid_coords(this_coords): # this should not happen at all
            raise IndexError("entity is not inside of maze")
        thisroom = self.lab[this_coords[0]][this_coords[1]]
        return thisroom.dir_is_accessible(direction)

    def _steve_useitem(self, item) -> None:
        raise NotImplementedError

    def _monster_roar(self):
        raise NotImplementedError

SOMEROOM = "SOMEROOM"
class Room:
    """
    -- ATTRIBUTES --
    + coords: list[int]
    + type: dict
    + connected: bool
    + mynorth: dict
    + mysouth: dict
    + myeast: dict
    + mywest: dict

    
    -- METHODS --
    + settype_startroom(self) -> None
    + steve_leaves(self) -> None
    + steve_enters -> None
    + steve_leaves -> None
    + steve_enters -> None

    
    """

    def __init__(self, x: int, y: int):
        self.coords = [x, y]
        self.cleared = True
        self.type = {"startroom?": False, "steve?": False, "boss?": False}
        self.connected = False
        self.creature = None
        self.item = None
        # setting mynorth, mysouth, myeast, mywest status attributes where possible
        self.mynorth = None
        self.mysouth = None
        self.myeast = None
        self.mywest = None
        if y + 1 >= labsize:
            self.mynorth = None
        else:
            self.mynorth = SOMEROOM
        if y <= 0:
            self.mysouth = None
        else:
            self.mysouth = SOMEROOM
        if x + 1 >= labsize:
            self.myeast = None
        else:
            self.myeast = SOMEROOM
        if x <= 0:
            self.mywest = None
        else:
            self.mywest = SOMEROOM

    def get_coords(self) -> list[int]:
        return self.coords

    def settype_startroom(self) -> None:
        self.type["startroom?"] = True
        self.type["steve?"] = True
        self.connected = True

    def steve_leaves(self) -> None:
        if not self.steve_ishere(): # Steve was not even here in this room in the first place
            raise RuntimeError(f"Steve is not in room {self.coords}, yet steve_leaves() is called.\nPossible desync between Labyrinth object's steve_pos attribute and this room object's type attribute values.")
        self.type["steve?"] = False
        self.cleared = True

    def steve_enters(self) -> None:
        if self.steve_ishere():
            raise RuntimeError(f"Steve is already in room {self.coords}, yet steve_enters() is called.\nPossible desync between Labyrinth object's steve_pos attribute and this room object's type attribute values.")
        self.type["steve?"] = True
        if not self.cleared:
            if random.randint(1, 100) <= 50: # 50% chance a creature spawn
                self.creature = random_creature()
                if random.randint(1, 100) <= 60: # if creature spawns, 60% chance an item spawns
                    self.item = random_item()
            elif random.randint(1, 100) <= 40: # if no creature spawned, 40% chance an item spawns
                self.item = random_item()
                
        

    def boss_leaves(self) -> None:
        if not self.boss_ishere():
            raise RuntimeError(f"Boss is not in room {self.coords}, yet boss_leaves() is called.\nPossible desync between Labyrinth object's boss_pos attribute and this room object's type attribute values.")
        self.type["boss?"] = False
            
    def boss_enters(self) -> None:
        if self.boss_ishere():
            raise RuntimeError(f"Boss is already in room {self.coords}, yet boss_enters() is called.\nPossible desync between Labyrinth object's boss_pos attribute and this room object's type attribute values.")
        self.type["boss?"] = True

    def connect_dir(self, direction, neighbour: "Room") -> None:
        if not isinstance(neighbour, Room):
            print(self.coords, neighbour.coords)
            raise ValueError(f"neighbour variable {neighbour} passed is not a room")
        if not is_adjacent(self.coords, neighbour.coords):
            print(self.coords, neighbour.coords)
            raise RuntimeError("neighbour variable passed is not an adjacent room")

        # makes assumptions that {direction} of this room is neighbour.
        if direction == NORTH:
            self.mynorth = neighbour
        elif direction == SOUTH:
            self.mysouth = neighbour
        elif direction == EAST:
            self.myeast = neighbour
        elif direction == WEST:
            self.mywest = neighbour
        else:
            raise ValueError("Direction passed is not of the right value")
    
    def set_connected_True(self) -> None:
        self.connected = True

    def get_creature(self) -> "Creature":
        return self.creature

    def get_item(self) -> "Item":
        return self.item

    def set_creature(self, creature: "Creature") -> None:
        if self.creature is not None:
            return None
        self.creature = creature
        return None

    def set_item(self, item: "Item") -> None:
        if self.item is not None:
            return None
        self.item = item

    def set_access(self, room: "Room") -> None:
        targetx, targety = room.get_coords()
        myx, myy = self.coords
        xdiff = targetx - myx
        ydiff = targety - myy
        i = 0
        directionnum = -1
        while i < 4:
            if DIRLIST[i] == [xdiff, ydiff]:
                directionnum = i
            i += 1
        if directionnum == -1:
            raise ValueError(f"set_access(), room {[targetx, targety]} is not adjacent to this room {self.coords}")
        direction = [NORTH, SOUTH, EAST, WEST][directionnum]
        if direction == NORTH:
            if self.mynorth is None:
                raise ValueError(f'Room {self.coords} has no room to the north of it, access cannot be set.')
            self.mynorth = room
        elif direction == SOUTH:
            if self.mysouth is None:
                raise ValueError(f'Room {self.coords} has no room to the south of it, access cannot be set.')
            self.mysouth = room
        elif direction == EAST:
            if self.myeast is None:
                raise ValueError(f'Room {self.coords} has no room to the east of it, access cannot be set.')
            self.myeast = room
        elif direction == WEST:
            if self.mywest is None:
                raise ValueError(f'Room {self.coords} has no room to the west of it, access cannot be set.')
            self.mywest = room
        else:
            raise ValueError(f'Room {self.coords} set_access() had argument passed that is not a direction value.')
        

    def is_connected_tostart(self) -> bool:
        return self.connected

    def get_neighbours_statuses(self) -> list["Room or SOMEROOM or None"]: # corresponding to N, S, E, W
        return [self.mynorth, self.mysouth, self.myeast, self.mywest]

    def get_neighbours_accessibility(self) -> list[bool]:
        outputlist = []
        for direction in [NORTH, SOUTH, EAST, WEST]:
            outputlist.append(self.dir_is_accessible(direction))
        return outputlist # e.g. [False, True, True, False] according to N, S, E, W

    def dir_is_accessible(self, direction) -> bool:
        if direction == NORTH:
            if not isinstance(self.mynorth, Room):
                return False
            return True
        if direction == SOUTH:
            if not isinstance(self.mysouth, Room):
                return False
            return True
        if direction == EAST:
            if not isinstance(self.myeast, Room):
                return False
            return True
        if direction == WEST:
            if not isinstance(self.mywest, Room):
                return False
            return True
        raise ValueError("argument passed into dir_is_accessible() should be a direction value.")

    def steve_ishere(self) -> bool:
        return self.type["steve?"]

    def boss_ishere(self) -> bool:
        return self.type["boss?"]
        

FOODITEM = "FOODITEM"
WEAPONITEM = "WEAPONITEM"
ARMOURITEM = "ARMOURITEM"
UTILITYITEM = "UTILITYITEM"

class Item:
    """
    -- ATTRIBUTES --
    
    -- METHODS --
    """
    def __init__(self, name, item_type):
        self.name = name
        self.item_type = item_type

    def __repr__(self) -> str:
        outputstr = f"Name: {self.name}\nType: {self.item_type}"
        return outputstr

    def __str__(self) -> str:
        outputstr = f"Name: {self.name}\nType: {self.item_type}"
        return outputstr

class Food(Item):
    def __init__(self, name, item_type, hprestore):
        super().__init__(name, item_type)
        self.hprestore = hprestore

    def __repr__(self):
        return super().__repr__() + f"\nRestores: {self.hprestore} HP"

    def __str__(self):
        return super().__str__() + f"\nRestores: {self.hprestore} HP"
    
    def get_restore(self):
        return self.hprestore

class Armor(Item):
    def __init__(self, name, item_type, defence, armor_slot):
        super().__init__(name, item_type)
        self.defence = defence
        self.armor_slot = armor_slot
        
    def __repr__(self):
        return super().__repr__() + f"\nProvides: {self.defence} defence"

    def __str__(self):
        return super().__str__() + f"\nProvides: {self.defence} defence"
        
    def get_defence(self):
        return self.defence

class Weapon(Item):
    def __init__(self, name, item_type, attack):
        super().__init__(name, item_type)
        self.attack = attack
        
    def __repr__(self):
        return super().__repr__() + f"\nDoes: {self.attack} damage"

    def __str__(self):
        return super().__str__() + f"\nDoes: {self.attack} damage"
        
    def get_attack(self):
        return self.attack

DEFAULT_HITPOINTS = 20
class Steve:
    """
    -- ATTRIBUTES --
    
    -- METHODS --
    """
    def __init__(self):
        self._inventory = [] # list of dict
        # each dict in self.inventory describes an item, as well as the number of it in the inventory.
        # e.g. {"item": Health_Potion, "number": 2}
        # There should NOT be duplicate dicts in self.inventory e.g. 2 different dicts in self.inventory with "item" being Health_Potions
        self.armour = {}
        for slot in ["helmet", "chestplate", "leggings", "boots"]:
            self.armour[slot] = None
        self.health = DEFAULT_HITPOINTS
        self.weapon = None
        self.base_damage = 2 # default

    def __repr__(self):
        return f"Steve has {self.health} HP."

    def _display_inventory(self) -> None:
        if self.inventory == []:
            print("You have no items in your inventory.\n")
            return None
        print("\nYou have:\n")
        for i in self.inventory:
            item, number = str(i["item"]), str(i["number"])
            print(f"{number:>2} {item}")
        print("\n")
        return None

    def _add_item_to_inv(self, new_item: "Item", num: int) -> None:
        for index, dict_ in enumerate(self._inventory): # Linear search through inventory
            if str(new_item) == str(dict_["item"]): # new_item is already in the inventory
                self._inventory[index]["number"] += num
                return None
        # If exit loop, inventory does not have any of new_item
        # create a dict to add to self.inventory
        self.inventory.append({"item": new_item, "number": num})
        return None

    def _discard_item(self, item: Item, num: int) -> None:
        for index, dict_ in enumerate(self._inventory): # Linear search through inventory
            if str(item) == str(dict_["item"]): # new_item is already in the inventory
                self._inventory[index]["number"] -= num
                if self._inventory[index]["number"] <=0:
                    self._inventory[index] = None
                return None
        print("Error: Item is not in inventory.")
        return None

    def equip_armour(self, armouritem: Item) -> None:
        self.armour[armouritem.armor_slot] = armouritem
        return None
        
    def eat(self, fooditem: "Item") -> None:
        #validation
        foodindex = self.find_item(fooditem)
        if foodindex == -1:
            raise RuntimeError(f"{fooditem} cannot be consumed as Steve's inventory does not have it.")
        if not fooditem.item_type == "Food":
            raise ValueError(f"{fooditem} cannot be consumed as it is not food.")
        # consumption
        self.remove_item_from_inv(foodindex)
        self.heal_health(fooditem.hprestore)

    def find_item(self, item: "Item") -> int:
        """Linear search through inventory to find the index of the item"""
        for i in self.inventory:
            if str(i["item"]) == str(item):
                return i
        return -1 # return value is -1 when not found.
        
    def remove_item_from_inv(self, index) -> None:
        if index not in list(range(len(self.inventory))):
            raise ValueError("Item that is trying to be removed from inventory has an index outside of the range of Steve's inventory.")
        if self.inventory[index]["number"] == 1: # Steve has only 1 of this such item left
            self.inventory.pop(index)
            # This dict is removed as there are no more of such items in the inventory
            return None
        self.inventory[index]["number"] -= 1
        return None
        
    def heal_health(self, change: int) -> None:
        if change == 0:
            return None
        prevhp = self.health
        if change > 0:
            self.health = min(self.health + change, 20)
            print(f"you were healed by {self.health - prevhp} HP and now have {self.health}.")
            return None
        self.health = max(self.health + change, 0)
        print(f"You got hurt by {prevhp - self.health} HP and have {self.health} left.")
        return None

    def get_defence(self):
        defence = 0
        for armor in self.armour.values():
            defence += armor.get_defence()
        return defence

    def equip_weapon(self, weapon):
        self.weapon = weapon
        
    def get_attack(self):
        return self.base_damage + self.weapon.get_attack()

    def isdead(self) -> bool:
        if self.health <= 0:
            return True
        return False

    def take_damage(self, damage):
        damage = int(damage * ((100 - self.get_defence())/100))
        self.hitpoints = max(0, self.hitpoints - damage)

class Creature:
    """
    -- ATTRIBUTES --
    name: name
    attack: damage stat
    hitpoints: current health
    maxhp: highest possible health
    -- METHODS --
    get_attack
    get_health
    """
    def __init__(self, name, maxhp, attack):
        self.name = name
        maxhp = self._generate_maxhp(maxhp, turn)
        self.hitpoints = maxhp
        self.attack = self._generate_attack(attack, turn)
        self.maxhp = maxhp

    def __repr__(self):
        return f"Name: {self.name}, HP:{self.hitpoints}/{self.maxhp}"

    def _generate_maxhp(self, maxhp: int, turn_number: int) -> None:
        maxhp = int((maxhp * ((turn_number / 10) + 1) * random.randint(90, 110) / 100))
        return maxhp
        
    def _generate_attack(self, attack: int, turn_number: int) -> None:
        attack = int((attack) * ((turn_number / 10) + 1) * (random.randint(90, 110) / 100))
        return attack
        
    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.hitpoints

    def take_damage(self, damage: int):
        self.hitpoints = self.hitpoints - damage

class Boss(Creature):
    """
    -- ATTRIBUTES --
    
    -- METHODS --
    """
    def __init__(self):
        super().__init__("King Warden", 100, 10):

    def heal(hp: int) -> None:
        self.hitpoints = min(self.hitpoints + hp, self.maxhp)
        
def random_creature() -> "Creature":
    creature_data = random.choice(creature_list)
    return Creature(creature_data["name"], creature_data["base_hp"], creature_data["base_atk"])

item_type_list = ["Armor", "Food", "Weapon"]
def random_item() -> "Item":
    item_type = random.choice(item_type_list)
    if item_type == "Armor":
        item_data = random.choice(armor_list)
        return Armor(item_data["name"], item_type, item_data["defence"], item_data["slot"])
    elif item_type == "Food":
        item_data = random.choice(food_list)
        return Food(item_data["name"], item_type, item_data["hprestore"])
    elif item_type == "Weapon":
        item_data = random.choice(weapon_list)
        return Weapon(item_data["name"], item_type, item_data["atk"])
        
    

with open("content/creatures.json",'r', encoding = 'utf-8') as f:
    creature_list = json.load(f)
with open("content/items/armor.json",'r', encoding = 'utf-8') as f:
    armor_list = json.load(f)
with open("content/items/food.json",'r', encoding = 'utf-8') as f:
    food_list = json.load(f)
with open("content/items/weapon.json",'r', encoding = 'utf-8') as f:
    weapon_list = json.load(f)
turn = 10
test = random_creature()
print(test)
test2 = random_item()
print(test2)
