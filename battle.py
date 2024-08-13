import random

class Battle:
  def __init__(self, player_hp, enemy_hp):
    self.player_hp = player_hp
    self.enemy_hp = enemy_hp
    self.damage = random.randint(1, 10)

  def player_attack(self):
    self.enemy_hp -= self.damage

  def enemy_attack(self):
    self.player_hp -= self.damage

  def battle_over(self):
    return self.player_hp == 0 or self.enemy_hp == 0