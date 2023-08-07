class Room:

    def __init__(self, name: str, paths: list, creature: bool, reyna: bool,
                 orb: bool):
        self.name = name
        self.paths = paths
        self.creature = creature
        self.reyna = reyna
        self.orb = orb


class Map:

    def __init__(self, rooms):
        pass

    def arrange(rooms):
        pass


class Character:

    def __init__(self):
        pass

    class Player:

        def hp(hp: int, self, creature: bool, buff: bool):  #Are we using buff?
            if creature:
                pass
            if buff:
                pass

    class Reyna:
        pass


# Randomly assign room name to every room
#Create path network for map
#Modify Character & its child classes later after discussion

roomlist = [
    "Spike Plant Hideout", "Breeze Bunker", "Haven Hold", "Bind Battlezone",
    "Split Strategy Chamber", "Icebox Infiltration Point",
    "Agent Training Arena", "Radiant Retreat", "Valorant Victory Vault",
    "Phoenix's Firepit", "Viper's Venom Den", "Jett's Jetway",
    "Killjoy's Contraption Corner", "Reyna's Soul Sanctuary",
    "Sova's Surveillance Nest", "Cypher's Cipher Room",
    "Astra's Astral Parlor", "Sage's Healing Haven", "Raze's Boombox Lounge",
    "Brimstone's Inferno Lounge", "Omen's Shadowy Chamber",
    "Yoru's Dimensional Den", "KAY/O's Tech Lab", "Skye's Nature Oasis",
    "Team Valorant War Room", "Duelist Dueling Grounds",
    "Spike Rush Social Spot", "Map Rotations Retreat",
    "Ranked Grind Gathering", "Radiant Rendezvous"
]
