class Character:

    def __init__(self, _type, health, items=None):
        self._type = _type
        self.health = health
        self.items = items or []


    def attack(self, character):
        """
        Deal damage to another character object
        """
        character.receive_damage(1)
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

class Player(Character):

    def __init__(self, health, strength, items=[]):
        super().__init__("Player", health, items)


class Soldier(Character):

    def __init__(self, health):
        super().__init__("Soldier", health)


class Princess(Character):

    def __init__(self, health):
        super().__init__("Princess", health)
