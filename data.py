class Room:
    """
    The Room class for each room

    Attributes:
    name: Name of room
    paths: List of rooms that this room has paths connected to
    creature: A boolean for creature presence
    orb: A boolean for powerup presence

    Methods:
    - get_name
    - get_paths
    - has_creature
    - has_orb
    - set_paths
    - set_creature
    - set_orb
    """

    def __init__(self, name: str, paths: list, creature: bool, orb: bool):
        self.name = name
        self.paths = paths
        self.creature = creature
        self.orb = orb

    def get_name(self) -> str:
        """Returns name of room"""
        return self.name

    def get_paths(self) -> list:
        """Return list of paths for the room"""
        return self.paths

    def has_creature(self) -> bool:
        """Returns creature presence in room"""
        return self.creature

    def has_orb(self) -> bool:
        """Returns orb presence in room"""
        return self.orb

    def set_paths(self, paths: list):
        """
        Allows for modification of the list of paths for the room
        """
        self.paths = paths

    def set_creature(self, creature: bool):
        """
        Allows for modification of the presence of a creature
        """
        self.creature = creature

    def set_orb(self, orb: bool):
        """
        Allows for modification of the presence of an orb
        """
        self.orb = orb


class Character:
    """
    A Character class for each character

    Attribrute:
    hp : Health points of the character

    Method:
    - get_hp
    """

    def __init__(self, hp: int):
        self.hp = hp

    def get_hp(self) -> int:
        """returns hp value of player"""
        return self.hp


class Player(Character):
    """
    A sub class of Character class

    Attributes:
    agent : Name of agent
    
    Methods:
     - get_agent
     - set_hp
    """

    def __init__(self, hp: int, agent: str):
        super().__init__(hp)
        self.agent = agent

    def get_agent(self) -> str:
        """Returns name of agent chosen"""
        return self.agent

    def set_hp(self, creature: bool, buff: bool) -> None:
        """
        Increases hp by 50 if buff found, and
        decreases it by 30 if creature found, no return value
        """
        if creature:
            self.hp -= 30
        if buff:
            self.hp += 50


# Randomly assign room name to every room
#Create path network for map
#Modify Character & its child classes later after discussion

_roompaths = {
    "T-side spawn": ["A lobby", "B lobby"],
    "A lobby": ["T-side spawn", "A long", "Catwalk"],
    "A long": ["A lobby", "A site"],
    "A site": ["A long", "Garden", "CT-side spawn"],
    "B site": ["CT-side spawn", "Market", "B main"],
    "B main": ["B site", "B lobby"],
    "B lobby": ["T-side spawn", "Tiles", "B main"],
    "Tiles": ["B lobby", "Catwalk", "Garden", "Market"],
    "Catwalk": ["A lobby", "Tiles", "Market", "Garden"],
    "Garden": ["A site", "Market", "Catwalk", "Tiles"],
    "Market": ["CT-side spawn", "B site", "Tiles", "Catwalk", "Garden"],
    "CT-side spawn": ["A site", "Market", "B site"]
}

roomlist = []
for room in _roompaths:
    roomlist.append(Room(room, _roompaths[room], False, False))
