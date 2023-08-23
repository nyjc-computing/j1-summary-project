class Spell:

    def __init__(self):
        self.type = "spell"
        self.name = ""
        self.description = ""
        self.attack = 0
        self.cost = 0
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

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

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

class WingardiumLeviosa(Spell):
    def __init__(self):
        super().__init__()
        self.set_name("Wingardium Leviosa")
        self.set_description("Wingardium Leviosa is a magic spell that can make objects levitate\nDeals 10 damage")
        self.set_attack(10)
        self.set_cost(0)
        self.set_move("")
        self.set_win_front("levitated ")
        self.set_win_back(" so high that it breached the atmosphere and exploded")
    
class VengefulSpirit(Spell):

    def __init__(self):
        super().__init__()
        self.set_name("Vengeful Spirit")
        self.set_description("")
        self.set_attack(10)
        self.set_cost(0)
        self.set_move("")
        self.set_win_front("")
        self.set_win_back("")

class Megidolan(Spell):

    def __init__(self):
        super().__init__()
        self.set_name("Megidolan")
        self.set_description("")
        self.set_attack(10)
        self.set_cost(0)
        self.set_move("")
        self.set_win_front("")
        self.set_win_back("")

class GlintstoneCometshard(Spell):

    def __init__(self):
        super().__init__()
        self.set_name("Glintstone Cometshard")
        self.set_description("")
        self.set_attack(10)
        self.set_cost(0)
        self.set_move("")
        self.set_win_front("")
        self.set_win_back("")