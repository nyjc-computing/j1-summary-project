

class Item:
    def __init__(self, type, name, description, player):
        self.type = type
        self.name = name
        self.description = description
        self.player = player
        
    def get_name(self):
        return self.name

    def display_description(self):
        """
        edit the print message
        """
        print("description", self.description)

class HealthPotion(Item):
    def __init__(self, type, name, description, player, health_gain):
        super().__init__(type, name, description, player)
        self.health_gain = health_gain

    def use_item(self):
        self.player.gain_health(self.health_gain)

class AuraPotion(Item):
    def __init__(self, type, name, description, player, aura_gain):
        super().__init__(type, name, description, player)
        self.aura_gain = aura_gain

    def use_item(self):
        self.player.gain_aura(self.aura_gain)

class Weapon(Item):
    def __init__(self, type, name, description, player, damage):
        super().__init__(type, name, description, player)
        self.damage = damage

    def use_item(self,monster):
        monster.take_damage(self.damage)

    


    


        
        
        
    
    
    
    
        
        
        
        