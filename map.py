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
        self.set_enemy(TheRadiance())
        self.set_name("Dirtmouth")
        self.set_description("You stepped into Dirtmouth, a haunting cliffside town in the depths of Hallownest, standing as a silent sentinel overlooking a dark and mysterious underground world. Its dilapidated buildings and eerie stillness set the tone for your perilous journey")
        self.link_left(Midgar())
        self.link_right(HyruleKingdom())
        self.link_forward(TheEndDimension())

class CelestialResort(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(MrOshiro())
        self.set_name("Celestial Resort")
        self.set_description("You stepped into a towering sanctuary of serenity nestled amidst the treacherous slopes of Celeste Mountain, a paradoxical challenge and a refuge for your weary soul. Its elegant halls and perilous puzzles mirrored your personal journey, a delicate dance between inner turmoil and newfound strength.")
        self.link_back(Ascent())

class TheForge(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(TheHighDragun())
        self.set_name("The Forge")
        self.set_description("You stepped into a blistering hellscape deep within the Gungeon, a relentless crucible where you honed your combat skills to a razor's edge. Its molten rivers and infernal denizens pushed you to your limits, but you are determined to conquer it and uncover the ultimate weapon hidden within.")
        self.link_forward(Mementos())

class StormveilCastle(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(GodrickTheGrafted())
        self.set_name("Stormveil Castle")
        self.set_description("You stepped into a legacy dungeon, a castle that lies on the cliff of stormveil, littered with hoards of enemies")
        self.link_forward(Kamurocho())
        self.link_right(TheHallow())

class ApertureLab(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Glados())
        self.set_name("Aperture Lab")
        self.set_description("You stepped into a sprawling maze of test chambers filled with menacingly cheery robots and the enigmatic AI, GLaDOS. Your journey through this surreal laboratory is a relentless quest for answers, a desperate struggle to escape its surreal confines and unmask the secrets lurking within.")
        self.link_forward(StormveilCastle())
        self.link_back(TowerOfFate())

class Zebes(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Ridley())
        self.set_name("Zebes")
        self.set_description("You stepped into a hostile and alien world, where you face some of your most harrowing battles against the Space Pirates and their nefarious plans. Its treacherous landscapes, infested with hostile creatures, hide the secrets of the Chozo and your relentless pursuit of justice.")
        self.link_forward(PrincipalsOffice())

class Bunker(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Emil())
        self.set_name("Bunker")
        self.set_description("You stepped into a grim sanctuary suspended above the ravaged Earth, both a refuge and a reminder of the relentless war against the machines. you receive orders, grapple with the complexities of your existence, and prepare for the constant struggle to reclaim your planet from the alien invaders.")

class Asphodel(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(TheBoneHyrda())
        self.set_name("Asphodel")
        self.set_description("You stepped into a desolate collection of rocky islands amidst a sea of fire beyond Tartarus. You travel between these islands through small bone rafts")
        self.link_back(Commencement())
        self.link_forward(GreenhillZone())

class KingdomOfKu(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(GeneralMugen())
        self.set_name("Kingdom of Ku")
        self.set_description("You stepped into a nation in Hinoeuma with a long and bloody history of conflict and war. Their enemies numbers many, one among several being the fallen nation of U. It was recently ruled by the aging King Jigo Ku, until a coup removed him from power")
        self.link_right(Bunker())
        self.link_forward(Zebes())

class GreenhillZone(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(DoctorEggman())
        self.set_name("Greenhill Zone")
        self.set_description("You stepped into a high-speed playground, a vibrant expanse of lush grass and rolling hills, where you feel most at home. Its loop-de-loops and buzzing animal friends provide the perfect backdrop for your never-ending quest to thwart Dr. Robotnik and collect the precious Chaos Emerald")
        self.link_forward(KingdomOfKu())

class TheHallow(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(TheMoonLord())
        self.set_name("The Hallow")
        self.set_description("You stepped into a radiant but eerie biome, a stark contrast to the darkness that permeates the underground. It's a realm where fantastical creatures and rare resources await, but also a place where you must tread carefully to avoid its relentless and otherworldly foes.")

class Commencement(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Mithrix())
        self.set_name("Commencement")
        self.set_description("You stepped into a large domain located above the shattered breach of Petrichor V's moon. It is ostensibly the desolated seat of Mithrix's power, made up of the shattered remains of four individual sections, emblematic of Mithrix and Providence's tools of creation")

class Midgar(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Sephiroth())
        self.set_name("Midgar")
        self.set_description("You stepped into the capital city and power base of the Shinra Electric Power Company in the world of Gaia. your memories of this metropolis are a tangled web of both longing and resentment, forever intertwined with your quest for justice and redemption.")
        self.link_forward(TheForge())

class HyruleKingdom(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Ganondorf())
        self.set_name("Hyrule Kingdom")
        self.set_description("You stepped into a land steeped in legend and mystique, it is your sacred duty to protect as the Hero of Time. Its vast, rolling landscapes and iconic landmarks are both your home and the canvas upon which your destiny is written as you battle the forces of darkness and seek to rescue Princess Zelda.")
        self.link_back(CelestialResort())

class TheEndDimension(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(TheEnderDragon())
        self.set_name("The End Dimension")
        self.set_description("You stepped into a dark, space-like dimension consisting of separate islands in the void, made out of end stone. It is inhabited by endermen and shulkers.")

class Kamurocho(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Shibusawa())
        self.set_name("Kamurocho")
        self.set_description("You stepped into the nightlife capital of Japan. As Tojo Clan territory, the district is home to many yakuza and is often the setting of large and small-scale disputes between the Tojo Clan and their rivals such as the Omi Alliance, as well as intra-clan conflicts between Tojo subsidiaries")

class TowerOfFate(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Enchantress())
        self.set_name("Tower of Fate")
        self.set_description("You stepped in a looming bastion of darkness and danger, standing as the heart of your perilous journey to save your beloved Shield Knight and the realm from the Enchantress's curse. Its treacherous ascent tests your mettle and resolve, driving you to prove that you am truly a knight worthy of legend.")

class ShoresOfNine(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Freya())
        self.set_name("Shores of Nine")
        self.set_description("You stepped into a realm of Norse myth, it offers a temporary respite from the relentless chaos of your past. You navigate this strange land with your son, Atreus, in search of a new beginning, forging a path toward redemption while battling the threats lurking in these uncharted waters.")

class Mementos(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Yaldabaoth())
        self.set_name("Mementos")
        self.set_description("You stepped into a sprawling, ever-changing abyss beneath the city, is where you confront the twisted desires of society's heart. It's a labyrinthine reflection of the collective unconscious, where you as a Phantom Thief embark on a mission to change hearts and expose the hidden darkness that plagues Tokyo.")
        self.link_right(ShoresOfNine())
        self.link_left(Asphodel())

class Ascent(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Reyna())
        self.set_name("Ascent")
        self.set_description("You step into a clearing, in the middle of what seems to be a city. Surrounding you are buildings, their appearance reminding you of Ancient Roman Architecture. A skyscraper rises into the sky in the distance, its cold, geometric features clashing with the elegant, smooth lines of the buildings surrounding you. It is only when you turn around that you realise the entire city is several hundred metres above the ground.")
        self.link_right(ApertureLab())

class PrincipalsOffice(Room):
    def __init__(self):
        super().__init__()
        self.set_enemy(Voldermort())
        self.set_name("Principals Office")
        self.set_description("You step into a chamber where disciplinary matters are addressed by the headmaster or headmistress. It is an imposing and somber room, with a large wooden desk and portraits of previous headmasters lining the walls, serving as a place of both judgment and guidance for students.")