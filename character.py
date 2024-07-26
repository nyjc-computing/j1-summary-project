class Character():

    def __init__(self, type, health, strength, items=[]):
        self.type = type
        self.health = health
        self.strength = strength
        self.items = items

    def __repr__(self):
        return f"Character: {self.type}\nHealth: {self.health}\nStrength: {self.strength}"  #Add items?

    def attack(self, character):
        character.health -= self.strength
        print("Die")

    def recieve_damage(self, damage):
        self.health -= damage
        print("Ouch")


class Player(Character):

    def __init__(self, health, strength, items=[]):
        super().__init__("Player", health, strength, items)

    def shout(self):
        print(f"I am a {self.type}")


class Soldier(Character):

    def __init__(self, health, strength, items=[]):
        super().__init__("Soldier", health, strength, items)

    def shout(self):
        print(f"I am a {self.type}")


class Princess(Character):

    def __init__(self, health, strength, items=[]):
        super().__init__("Princess", health, strength, items)

    def shout(self):
        print(f"I am a {self.type}")
