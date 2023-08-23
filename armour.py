class Armour:
    
    def __init__(self):
        self.type = "armour"
        self.name = ""
        self.description = ""
        self.defence = 0

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

    def set_defence(self, defence):
        self.defence = defence

    def get_defence(self):
        return self.defence

class NetheriteArmour(Armour):

    def __init__(self):
        super().__init__()
        self.set_name("Netherite Armour")
        self.set_description("")
        self.set_defence(10)

class OrnatePlate(Armour):

    def __init__(self):
        super().__init__()
        self.set_name("Ornate Plate")
        self.set_description("")
        self.set_defence(10)

class PowerSuit(Armour):

    def __init__(self):
        super().__init__()
        self.set_name("Power Suit")
        self.set_description("")
        self.set_defence(10)
