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
        self.set_mana_boost(10)
        self.set_description(f"The Golden Feather is a coveted and shimmering collectible that enhances your mobility. Its radiant appearance and unique functionality make it a symbol of progress and determination\nBoost mana by {self.get_mana_boost()} points")
        

class MasterRound(Accessory):

    def __init__(self):
        super().__init__()
        self.set_name("Master Round")
        self.set_health_boost(10)
        self.set_description(f"The Master Round is a prestigious and rare item that boost the player's health and also serve as a symbol of their mastery of challenging battles\nBoost health by {self.get_health_boost()} points")

class DragonAmulet(Accessory):

    def __init__(self):
        super().__init__()
        self.set_name("Dragon Amulet")
        self.set_attack_boost(10)
        self.set_description(f"The Dragon Amulet is a prized and ornate accessory and a symbol of membership in the Dojima Family. It features a dragon motif that represents a connection to the Yakuza world\nBoost attack by {self.get_attack_boost()} points")
        

class ChaosEmerald(Accessory):

    def __init__(self):
        super().__init__()
        self.set_name("Chaos Emerald")
        self.set_health_boost(10)
        self.set_description(f"The Chaos Emerald is a mystical, multicolored gemstone of immense power. The gemstones is known for its ability to grant incredible abilities, including the power of super transformation\nBoost health by {self.get_health_boost()} points")
        

