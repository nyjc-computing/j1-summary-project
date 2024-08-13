import random
import Character

class Battle:
    def __init__(self, player, enemies: list):
        self.player = player
        self.enemies = enemies
        self.damage = random.randint(2, 10)

    def player_attack(self):
        self.player.attack(self.enemies[0])

    def enemy_attack(self):
        self.enemies[0].attack(self.player])

    def battle_over(self):
        if self.player_hp == 0:
            return True
        for i in self.enemy:
            if i != 0:
                return False
        return True