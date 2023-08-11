class Room:

    def __init__(self, name: str, paths: list, creature: bool, reyna: bool,
                 orb: bool):
        self.name = name
        self.paths = paths
        self.creature = creature
        self.reyna = reyna
        self.orb = orb


class Map:

    def __init__(self, roompaths: dict):
        self.rooms = roompaths.keys()
        self.paths = roompaths.values()

    def arrange(rooms) -> None:
        pass


class Character:

    def __init__(self, hp: int):
        self.hp = hp

    class Player:

        def hp(self, creature: bool, buff: bool) -> None:  #Are we using buff?
            if creature:
                self.hp -= 30
            if buff:
                self.hp += 30

        def win(self, reyna: bool) -> bool:
            if reyna:
                if self.hp >= 300:
                    return True
                else:
                    return False


# Randomly assign room name to every room
#Create path network for map
#Modify Character & its child classes later after discussion

roompaths = {
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
