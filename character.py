import random

class Character:

    def __init__(self, _type, health, damage = 0):
        self._type = _type
        self.health = health
        self.damage = damage


    def attack(self, character):
        """
        Deal damage to another character object
        """
        character.receive_damage(self.damage)
        # print("Die")

    def receive_damage(self, damage):
        """
        Remove health
        """
        self.health -= damage
        # print("Ouch")

    def isdead(self):
        """
        Returns status of character (dead or alive)
        """
        return self.health <= 0

    def get_health(self):
        return self.health

    def get_type(self):
        return self._type

class Player(Character):

    def __init__(self, health, damage):
        super().__init__("Player", health, damage)


class Soldier(Character):

    def __init__(self, health):
        super().__init__("Soldier", health)
        self.damage = random.randint(2,7)

class Princess(Character):

    def __init__(self, health):
        super().__init__("Princess", health)
