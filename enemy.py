from armour import *
from weapon import *
from accessory import *
from spell import *

class Enemy:
    """
    creates the enemies that are in the room

    Attributes
    ----------
    + name: str
    + spell: str
    - health: int
    + battle_points: int
    + loot: str

    Methods
    -------
    + set_health(): updates the enemy's health
    - is_dead(): checks the state of the enemy
    + get_health(): gets the health of the enemy
    
    """

    def __init__(self) -> None:
        self.name = None
        self.health = 0
        self.attack = 0
        self.loot = None
        self.description = ""
        self.move = ""

    def set_health(self, bp: int) -> None:
        """
        Updates the enemy's health
        """
        self.health = bp

    def get_health(self) -> int:
        """
        Returns the enemys health
        """
        return self.health

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_attack(self, attack):
        self.attack = attack

    def get_attack(self):
        return self.attack

    def set_move(self, move):
        self.move = move

    def get_move(self):
        return self.move

    def set_loot(self, loot):
        self.loot = loot

    def get_loot(self):
        return self.loot

class TheRadiance(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("The Radiance")
        self.set_health(20)
        self.set_description("a higher being of light similar to Essence, and as such, opposed to the Void, her ancient enemy. The Moth Tribe is born from her light and in return revered her.")
        self.set_attack(10)
        self.set_move("wall of light")
        self.set_loot(VengefulSpirit())

class MrOshiro(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Mr Oshiro")
        self.set_health(20)
        self.set_description("a well-meaning but tormented ghostly hotel owner in Celeste, haunted by his past and struggling to maintain his crumbling establishment")
        self.set_attack(10)
        self.set_move("charge")
        self.set_loot(GoldenFeather())

class TheHighDragun(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("The High Dragun")
        self.set_health(10)
        self.set_description("a powerful dragon armed to the teeth with an array of deadly attacks and a formidable challenge for any gungeoneer")
        self.set_attack(10)
        self.set_move("bullet stream")
        self.set_loot(MasterRound())

class GodrickTheGrafted(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Godrick The Grafted")
        self.set_health(10)
        self.set_description("a grotesque and formidable boss, a creature amalgamation of flesh and metal that presents a formidable challenge to you with his overwhelming power and monstrous appearance")
        self.set_attack(10)
        self.set_move("dragon arm")
        self.set_loot(GlintstoneCometshard())

class Glados(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Glados")
        self.set_health(10)
        self.set_description("a malevolent AI antagonist, known for her dark sense of humor and penchant for testing subjects with life-threatening puzzles")
        self.set_attack(10)
        self.set_move("neurotoxin gas")
        self.set_loot(PortalGun())

class Yaldabaoth(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Yaldabaoth")
        self.set_health(10)
        self.set_description("an imposing and god-like antagonist, representing the oppressive control and distorted order imposed upon society")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(Megidolaon())

class Ridley(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Ridley")
        self.set_health(10)
        self.set_description("a fearsome space pirate leader and recurring antagonist, known for his ruthless cruelty and iconic draconic appearance")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(PowerSuit())

class Emil(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Emil")
        self.set_health(10)
        self.set_description("a nightmarish and relentless foe, with multiple heads and powerful attacks")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(VirtuousTreaty())

class TheBoneHyrda(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("The Bone Hydra")
        self.set_health(10)
        self.set_description("a fearsome and multi-headed boss, a relentless adversary that guards the underworld's entrance and challenges you with its deadly attacks.")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(Coronacht())

class GeneralMugen(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("General Mugen")
        self.set_health(10)
        self.set_description("a formidable and ruthless military leader, known for his strategic prowess and unwavering dedication to his nation's conquest")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(DragonMail())

class DoctorEggman(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Doctor Eggman")
        self.set_health(10)
        self.set_description("a brilliant yet perpetually thwarted scientist with a penchant for constructing nefarious machines and plots to conquer the world")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(ChaosEmerald())

class TheMoonLord(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("The Moon Lord")
        self.set_health(10)
        self.set_description("a towering eldritch entity with a menacing appearance and an array of devastating attacks that challenge you to your limits")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(Zenith())

class Mithrix(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Mithrix")
        self.set_health(10)
        self.set_description("a vengeful and godlike being with the power to manipulate time and space, posing a significant threat to whoever attempts to escape")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(WillOTheWisp())

class Sephiroth(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Sephiroth")
        self.set_health(10)
        self.set_description("a brooding and immensely powerful warrior with a deep-seated desire to harness the destructive force of the planet for his own malevolent purposes")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(BusterSword())

class Ganondorf(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Ganondorf")
        self.set_health(10)
        self.set_description("a malevolent Gerudo sorcerer who seeks to obtain the Triforce's power and plunge Hyrule into darkness and chaos")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(MasterSword())

class TheEnderDragon(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("The Ender Dragon")
        self.set_health(10)
        self.set_description("a fearsome and colossal winged creature that challenges you with its destructive abilities and formidable strength")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(NetheriteArmour())

class Shibusawa(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Shibusawa")
        self.set_health(10)
        self.set_description("a ruthless and power-hungry underworld figure who manipulates events to achieve his sinister goals within the criminal landscape of Kamurocho")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(DragonAmulet())

class Enchantress(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Enchantress")
        self.set_health(10)
        self.set_description("a mastermind behind the Order of No Quarter, shrouded in mystery and wielding dark magic")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(OrnatePlate())

class Freya(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Freya")
        self.set_health(10)
        self.set_description("a formidable and relentless adversary, harnessing her powerful magic and fierce determination to protect her son, Baldur")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(LeviathanAxe())

class Reyna(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Reyna")
        self.set_health(10)
        self.set_description("a deadly duelist agent with the ability to absorb the souls of defeated enemies, empowering herself to become an even more formidable threat on the battlefield")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(RGXButterflyKnife())

class Voldermort(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Reyna")
        self.set_health(10)
        self.set_description("a deadly duelist agent with the ability to absorb the souls of defeated enemies, empowering herself to become an even more formidable threat on the battlefield")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(RGXButterflyKnife())