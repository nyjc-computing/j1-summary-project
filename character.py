class Character:

    def __init__(self, _type, health, strength, items=None):
        self._type = _type
        self.health = health
        self.strength = strength
        self.items = items or []

    def __repr__(self):
        return f"Character: {self._type}\nHealth: {self.health}\nStrength: {self.strength}"  #Add items?

    def attack(self, character):
        """
        Deal damage to another character object
        """
        character.receive_damage(self.strength)
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


class Player(Character):

    def __init__(self, health, strength, items=[]):
        super().__init__("Player", health, strength, items)


class Soldier(Character):

    def __init__(self, health, strength):
        super().__init__("Soldier", health, strength)


class Princess(Character):

    def __init__(self, health, strength):
        super().__init__("Princess", health, strength)
