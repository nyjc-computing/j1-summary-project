import random

class Room:

    def __init__(self, name):
        self.name = name
        self.enemies = []

    def get_enemies(self):
        return self.enemies

    def add_enemy(self, enemy):
        self.enemies.append(enemy)
        
    
    def all_enemies_defeated(self):
        # if enemy is deafeated, it is removed from self.enemies
        return len(self.enemies) == 0

    def get_name(self):
        return self.name


