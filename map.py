from enemy import *
from weapon import *
from armour import *
from spell import *

class Room:
    """
    creates the room weapon and enemy

    Attribute
    ---------
    + name: str
    + enemy: str
    + right: str
    + left: str
    + up: str
    + down: str
    + been_here: bool
    + discription: str
    - is_fighting: bool

    Method
    ------
    + link_left(): updates the room to the left of the home room(self.name)
    + link_right(): updates the room to the right of the home room(self.name)
    + link_up(): updates the room to the up of the home room(self.name)
    + link_down(): updates the room to the down of the home room(self.name)
    + set_is_fighting: updates the status of the character in the room
    + get_is_fighting: gets the status of the character in the room
    + set_been_here(): updates the status of wether the character has been to this room
    + get_been_here(): gets the status of wether the character has been to this room
    """
   
    def __init__(self):
        self.name = ""
        self.enemy = None
        self.description = ""
        self.left = None
        self.right = None
        self.forward = None
        self.back = None
        self.been_here = False
        self.is_fighting = False
        self.loot = None

    def set_been_here(self, status: bool) -> None:
        self.been_here = status
        
    def get_been_here(self) -> bool:
        return self.been_here

    def set_is_fighting(self, status: bool) -> None:
        self.is_fighting = status

    def get_is_fighting(self) -> bool:
        return self.is_fighting
    
    def link_left(self, room):
        temp = room
        temp.right = self
        self.left = temp

    def get_left(self):
        return self.left

    def link_right(self, room):
        temp = room
        temp.left = self
        self.right = temp

    def get_right(self):
        return self.right

    def link_forward(self, room):
        temp = room
        temp.back = self
        self.forward = temp

    def get_forward(self):
        return self.forward

    def link_back(self, room):
        temp = room
        temp.forward = self
        self.back = temp

    def get_back(self):
        return self.back

    def set_enemy(self, enemy):
        self.enemy = enemy

    def get_enemy(self):
        return self.enemy

    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
        
class Dirtmouth(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Radiance())
        self.set_name("Dirtmouth")
        self.set_description("You stepped into Dirtmouth, a haunting cliffside town in the depths of Hallownest, standing as a silent sentinel overlooking a dark and mysterious underground world. Its dilapidated buildings and eerie stillness set the tone for your perilous journey")
        self.link_left(Midgar())
        self.link_right(HyruleKingdom())
        self.link_forward(TheEnd())

class CelestialResort(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(MrOshiro())
        self.set_name("Celestial Resort")
        self.set_description("")
        self.link_back(Ascent())

class TheForge(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(HighDragun())
        self.set_name("The Forge")
        self.set_description("")
        self.link_forward(Mementos())

class StormveilCastle(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(GodrickTheGrafted())
        self.set_name("Stormveil Castle")
        self.set_description("")
        self.link_forward(Kamurocho())
        self.link_right(TheHallow())

class ApertureLab(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Glados())
        self.set_name("Aperture Lab")
        self.set_description("")
        self.link_forward(StormveilCastle())
        self.link_back(TowerOfFate())

class Zebes(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Ridley())
        self.set_name("Zebes")
        self.set_description("")

class Bunker(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Emil())
        self.set_name("Bunker")
        self.set_description("")

class Asphodel(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(BoneHyrda())
        self.set_name("Asphodel")
        self.set_description("")
        self.link_back(Commencement())
        self.link_forward(GreenhillZone())

class KingdomOfKu(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(GeneralMugen())
        self.set_name("Kingdom of Ku")
        self.set_description("")
        self.link_right(Bunker())
        self.link_forward(Zebes())

class GreenhillZone(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(DoctorEggman())
        self.set_name("Greenhill Zone")
        self.set_description("")
        self.link_forward(KingdomOfKu())

class TheHallow(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(MoonLord())
        self.set_name("The Hallow")
        self.set_description("")

class Commencement(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Mithrix())
        self.set_name("Commencement")
        self.set_description("")

class Midgar(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Sephiroth())
        self.set_name("Midgar")
        self.set_description("")
        self.link_forward(TheForge())

class HyruleKingdom(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Ganondorf())
        self.set_name("Hyrule Kingdom")
        self.set_description("")
        self.link_back(CelestialResort())

class TheEnd(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(EnderDragon())
        self.set_name("The End")
        self.set_description("")

class Kamurocho(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Shibusawa())
        self.set_name("Kamurocho")
        self.set_description("")

class TowerOfFate(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Enchantress())
        self.set_name("Tower of Fate")
        self.set_description("")

class ShoresOfNine(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Freya())
        self.set_name("Shores of Nine")
        self.set_description("")

class Mementos(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Yaldabaoth())
        self.set_name("Mementos")
        self.set_description("")
        self.link_right(ShoresOfNine())
        self.link_left(Asphodel())

class Ascent(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Reyna())
        self.set_name("Ascent")
        self.set_description("")
        self.link_right(ApertureLab())