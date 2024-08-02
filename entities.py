
class Entity():

    def __init__(self, name, health, aura, position):
        self.name = name
        self.health = health
        self.aura = aura
        self.position = position

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def set_health(self,health):
        self.health = health

    def move(self, position, move):
        if move == "W":
            position[1] += 1
        elif move == "A":
            position[0] -= 1
        elif move == "S":
            position[1] -= 1
        elif move == "D":
            position[0] += 1
            
        
    


class Player(Entity):

    def __init__(self, name, health, aura, position,inventory = []):
        super().__init__(name, health, aura, position)
        self.inventory = inventory

    def get_aura(self):
        return self.aura

    def set_aura(self,aura):
        self.aura = aura

    def add_item(self,item):
        self.inventory.append(item)

    def remove_item(self,item):
        self.inventory.remove(item)

    def get_inventory(self):
        return self.inventory

    
class Monster(Entity):
    
    def __init__(self, name, health, aura, position, damage, description, inventory = []):
        super().__init__(name, health, aura, position)
        self.damage = damage
        self.description = description
        self.inventory = inventory
        

    def pickup_item(self,item):
        self.inventory.append(item)

    def get_inventory(self):
        return self.inventory
    
        
class Creature(Entity):

    def __init__(self, name, health, aura, position, damage, description):
        super().__init__(name, health, aura, position)
        self.damage = damage
        self.description = description


    def get_damage(self):
        return self.damage

    def set_damage(self, damage):
        self.damage = damage

        
        
    
    
    
