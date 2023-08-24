class Weapon:

    def __init__(self):
        self.type = "weapon"
        self.name = ""
        self.description = ""
        self.attack = 0
        self.move = ""
        self.win_front = ""
        self.win_back = ""

    def get_type(self):
        return self.type
        
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

    def set_win_front(self, win_front):
        self.win_front = win_front
        
    def get_win_front(self):
        return self.win_front

    def set_win_back(self, win_back):
        self.win_back = win_back
        
    def get_win_back(self):
        return self.win_back

class BusterSword(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Buster Sword")
        self.set_attack(10)
        self.set_description(f"The Buster Sword is an enormous broadsword. From tip to handle, it is approximately five to six feet long, with a single-edged large blade approximately one foot wide\nDeals {self.get_attack()} damage")
        self.set_move(" used Focused Thrust")
        self.set_win_front(" used braver and smashed ")
        self.set_win_back(" into the ground")

class MasterSword(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Master Sword")
        self.set_attack(10)
        self.set_description(f"The Master Sword is a divine magic sword with the power to vanquish evil. Infused with the sacred flames provided by the Golden Goddesses and blessed with Hylia's power\nDeals {self.get_attack()} damage")
        self.set_move(" used Sword beam")
        self.set_win_front(" used the power of the triforce to vanquish ")
        self.set_win_back(" from the face of the earth")

class LeviathanAxe(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Leviathan Axe")
        self.set_attack(10)
        self.set_description(f"The Leviathan axe legendary two-handed battle axe imbuded with elemental magic allowing it to return to the user\nDeals {self.get_attack()} damage")
        self.set_move(" threw the Leviathan Axe")
        self.set_win_front(" lunged towards ")
        self.set_win_back(" and decapitated it")

class PortalGun(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Portal Gun")
        self.set_attack(10)
        self.set_description(f"The Portal Gun is a hand-held device which has the ability to manufacture two linked portals. No matter the distance between them, any object which passes through one portal will emerge from the other and vice versa instantaneously\nDeals {self.get_attack()} damage")
        self.set_move(" used portals")
        self.set_win_front(" used a portal to send ")
        self.set_win_back(" to the moon")

class VirtuousTreaty(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Virtuous Treaty")
        self.set_attack(10)
        self.set_description(f"The Virtuous Treaty is a pure white samurai blade not sullied by a single drop of blood\nDeals {self.get_attack()} damage")
        self.set_move(" used Virtuous Treaty")
        self.set_win_front(" struck ")
        self.set_win_back(" down in one clean slash")

class Coronacht(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Coronacht")
        self.set_attack(10)
        self.set_description(f"The Coronacht is an infernal arm, the finest bow ever concevied, once weilded by Mistress Hera\nDeals {self.get_attack()} damage")
        self.set_move(" used power shot")
        self.set_win_front(" Used the aspect of Hera to shoot a power shot right through ")
        self.set_win_back("")

class Zenith(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Zenith")
        self.set_attack(10)
        self.set_description(f"The Zenith is a legendary blade crafted using 10 different powerful swords\nDeals {self.get_attack()} damage")
        self.set_move(" used The Zenith")
        self.set_win_front(" obliterated ")
        self.set_win_back(" using the power of 10 swords")

class RGXButterflyKnife(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("RGX Butterfly Knife")
        self.set_attack(10)
        self.set_description(f"The RGX Butterfly Knife is the most powerful butterfly knife on earth due its RGB\nDeals {self.get_attack()} damage")
        self.set_move(" used behind the 8 ball")
        self.set_win_front(" performed the valorant inspect flawlessly causing ")
        self.set_win_back(" to self destruct")

class ElderWand(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Elder Wand")
        self.set_attack(10)
        self.set_description("The most powerful wand on earth")
        self.set_move("")
        self.set_win_front("")
        self.set_win_back("")

class Wand(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Wand")
        self.set_attack(10)
        self.set_description(f"The Wand is a generic wand\nDeals {self.get_attack()} damage")
        self.set_move(" threw the wand")
        self.set_win_front(" poked ")
        self.set_win_back(" to death")  

class MarksmanRevolver(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Marksman Revolver")
        self.set_attack(10)
        self.set_description(f"A revolver. Every few seconds a coin pops out of the bottom of the gun. The purpose of this function is lost on you\nDeals {self.get_attack()} damage")
        self.set_move(" +HEADSHOT")
        self.set_win_front(" threw $4.32 of change at ")
        self.set_win_back(", knocking it out")  