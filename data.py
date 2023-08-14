class Room:
    """
    The Room class for each room

    Attributes:
    name: Name of room
    paths: List of rooms that this room has paths connected to
    creature: A boolean for creature presence
    orb: A boolean for powerup presence

    Methods:
    - setpaths
    - setcreature
    - setorb
    """

    def __init__(self, name: str, paths: list, creature: bool, orb: bool):
        self.name = name
        self.paths = paths
        self.creature = creature
        self.orb = orb

    def setpaths(self, paths: list):
        """
        Allows for modification of the list of paths for the room
        """
        self.paths = paths

    def setcreature(self, creature: bool):
        """
        Allows for modification of the presence of a creature
        """
        self.creature = creature

    def setorb(self, orb: bool):
        """
        Allows for modification of the presence of an orb
        """
        self.orb = orb


class Character:
    """
    A Character class for each character
    Contains the following attribute only:

    hp : Health points of the character
    """

    def __init__(self, hp: int):
        self.hp = hp

    class Player:
        """
        A sub class of Character class

        Attributes:
        agent : Name of agent
        
        Methods:
         - hp(self, creature : bool, buff : bool)
         - win(self, reyna : bool)
        """

        def __init__(self, agent: str, hp : int):
            self.agent = agent
            self.hp = hp

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
    "CT-side spawn": ["A site", "Market", "B site"],
    "B site": ["CT-side spawn", "Market", "B main"],
    "B main": ["B site", "B lobby"],
    "B lobby": ["T-side spawn", "Tiles", "B main"],
    "Tiles": ["B lobby", "Catwalk", "Garden", "Market"],
    "Catwalk": ["A lobby", "Tiles", "Market", "Garden"],
    "Garden": ["A site", "Market", "Catwalk", "Tiles"],
    "Market": ["CT-side spawn", "B site", "Tiles", "Catwalk", "Garden"]
}

roomlist = []
for room in _roompaths:
    roomlist.append(Room(room, _roompaths[room], False, False))