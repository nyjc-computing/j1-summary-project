
class Entity():

    def __init__(self, name, health, aura, position):
        self.name = name
        self.health = health
        self.aura = aura
        self.position = position
        self.items = []

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_aura(self):
        return self.aura

    def set_health(self,health):
        self.health = health

    def set_aura(self,aura):
        self.aura = aura

    def add_item(self,item):
        self.items.append(item)

    def remove_item(self,item):
        self.items.remove(item)

    def move(self,position):
        move = input()
        if move == "W":
            position[1] += 1
        elif move == "A":
            position[0] -= 1
        elif move == "S":
            position[1] -= 1
        elif move == "D":
            position[0] += 1
            
        
    


class Player(Entity):
    pass
    
    
