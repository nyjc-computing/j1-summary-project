import random
from Character import *


class Room:

  def __init__(self, name):
    self.name = name
    self.enemy_num = random.randint(2, 5)

  def fight(self):
    pass
