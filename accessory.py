class Accessory:

    def __init__(self):
        self.type = "accessory"
        self.name = ""
        self.descripton = ""
        self.health_boost = 0
        self.attack_boost = 0
        self.mana_boost = 0

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

    def set_health_boost(self, health_boost):
        self.health_boost = health_boost

    def get_health_boost(self):
        return self.health_boost

    def set_attack_boost(self, attack_boost):
        self.attack_boost = attack_boost

    def get_attack_boost(self):
        return self.attack_boost

    def set_mana_boost(self, mana_boost):
        self.mana_boost = mana_boost

    def get_mana_boost(self):
        return self.mana_boost

class GoldenFeather(Accessory):

    def __init__(self):
        super().__init__()
        self.set_name("Golden Feather")
        self.set_description("")
        self.set_mana_boost(0)

class MasterRound(Accessory):

    def __init__(self):
        super().__init__()
        self.set_name("Master Round")
        self.set_description("")
        self.set_health_boost(0)

class DragonAmulet(Accessory):

    def __init__(self):
        super().__init__()
        self.set_name("Dragon Amulet")
        self.set_description("")
        self.set_attack_boost(0)

class ChaosEmerald(Accessory):

    def __init__(self):
        super().__init__()
        self.set_name("Chaos Emerald")
        self.set_description("")
        self.set_health_boost(0)

