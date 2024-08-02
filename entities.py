
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

    def get_position(self):
        return self.position

    def set_position(self,position):
        self.position = position

    def move(self, move, adjacent_tiles):
        
        if move == "W":
            if adjacent_tiles["North"] is None:
                return "invalid"
            else:
                self.position[1] += 1
                
        elif move == "A":
            if adjacent_tiles["West"] is None:
                return "invalid"
            else:
                self.position[0] -= 1
            
        elif move == "S":
            if adjacent_tiles["South"] is None:
                return "invalid"
            else:
                self.position[1] -= 1
    
            
        elif move == "D":
            if adjacent_tiles["East"] is None:
                return "invalid"
            else:
                self.position[0] += 1
            
    


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

        
        
    
    
    
