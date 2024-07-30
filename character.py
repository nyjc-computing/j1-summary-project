class Character:

    def __init__(self, type, health, strength, items=[]):
        self.type = type
        self.health = health
        self.strength = strength
        self.items = items

    def __repr__(self):
        return f"Character: {self.type}\n\
                 Health: {self.health}\n\
                 Strength: {self.strength}"  #Add items?

    def attack(self, character):
        """
        Deal damage to another character object
        """
        character.recieve_damage(self.strength)
        # print("Die")

    def recieve_damage(self, damage):
        """
        Remove health
        """
        self.health -= damage
        # print("Ouch")



class Player(Character):

    def __init__(self, health, strength, items=[]):
        super().__init__("Player", health, strength, items)


class Soldier(Character):

    def __init__(self, health, strength):
        super().__init__("Soldier", health, strength)


class Princess(Character):

    def __init__(self, health, strength):
        super().__init__("Princess", health, strength)
