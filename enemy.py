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

class Radiance(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Radiance")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(VengefulSpirit())

class MrOshiro(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Mr Oshiro")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(GoldenFeather())

class HighDragun(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("High Dragun")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(MasterRound())

class GodrickTheGrafted(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Godrick The Grafted")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(GlintstoneCometshard())

class Glados(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Glados")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(PortalGun())

class Yaldabaoth(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Yaldabaoth")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(Megidolan())

class Ridley(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Ridley")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(PowerSuit())

class Emil(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Emil")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(VirtuousTreaty())

class BoneHyrda(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Bone Hydra")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(Coronacht())

class GeneralMugen(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("General Mugen")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(None)

class DoctorEggman(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Doctor Eggman")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(None)

class MoonLord(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Moon Lord")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(TerraBlade())

class Mithrix(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Mithrix")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(None)

class Sephiroth(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Sephiroth")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(BusterSword())

class Ganondorf(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Ganondorf")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(MasterSword())

class EnderDragon(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Ender Dragon")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(NetheriteArmour())

class Shibusawa(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Shibusawa")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(DragonAmulet())

class Enchantress(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Enchantress")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(OrnatePlate())

class Freya(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Freya")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(LeviathanAxe())

class Reyna(Enemy):
    def __init__(self):
        super().__init__()
        self.set_name("Reyna")
        self.set_health(10)
        self.set_description("")
        self.set_attack(10)
        self.set_move("")
        self.set_loot(RGXButterflyKnife())