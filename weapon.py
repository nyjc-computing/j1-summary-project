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
        self.set_description("An enormous broadsword. From tip to handle, it is approximately five to six feet long, with a single-edged large blade approximately one foot wide.")
        self.set_attack(100)
        self.set_move("")
        self.set_win_front("")
        self.set_win_back("")

class MasterSword(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Master Sword")
        self.set_description("A divine magic sword with the power to vanquish evil. Infused with the sacred flames provided by the Golden Goddesses and blessed with Hylia's power")
        self.set_attack(100)
        self.set_move("")
        self.set_win_front("")
        self.set_win_back("")

class LeviathanAxe(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Leviathan Axe")
        self.set_description("a two-handed battle axe. It was forged by Brok and Sindri for Laufey, in hopes that she would help undo their mistake in creating Mjolnir")
        self.set_attack(100)
        self.set_move("")
        self.set_win_front("")
        self.set_win_back("")

class PortalGun(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Portal Gun")
        self.set_description("A hand-held device which has the ability to manufacture two linked portals. No matter the distance between them, any object which passes through one portal will emerge from the other and vice versa instantaneously")
        self.set_attack(100)
        self.set_move("")
        self.set_win_front("")
        self.set_win_back("")

class VirtuousTreaty(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Virtuous Treaty")
        self.set_description("")
        self.set_attack(100)
        self.set_move("")
        self.set_win_front("")
        self.set_win_back("")

class Coronacht(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Coronacht")
        self.set_description("")
        self.set_attack(100)
        self.set_move("")
        self.set_win_front("")
        self.set_win_back("")

class TerraBlade(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("Terra Blade")
        self.set_description("")
        self.set_attack(100)
        self.set_move("")
        self.set_win_front("")
        self.set_win_back("")

class RGXButterflyKnife(Weapon):

    def __init__(self):
        super().__init__()
        self.set_name("RGX Butterfly Knife")
        self.set_description("")
        self.set_attack(100)
        self.set_move("")
        self.set_win_front("")
        self.set_win_back("")
