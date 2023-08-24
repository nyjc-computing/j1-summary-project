class loot:

    def __init__(self):
        self.name = ""
        self.description = ""
        self.health = 0
        self.mana = 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_health(self, health):
        self.health = health

    def get_health(self):
        return self.health

    def set_mana(self, mana):
        self.mana = mana

    def get_mana(self):
        return self.mana

class FlaskOfCrimsonTears(loot):

    def __init__(self):
        super().__init__()
        self.set_name("Flask of Crimson Tears")
        self.set_health(10)
        self.set_description(f"The Flask of Crimson Tears is a sacred flask modelled after a golden holy chalice that was once graced by a tear of life\nHeals {self.get_health()} health")

class FlaskOfCeruleanTears(loot):

    def __init__(self):
        super().__init__()
        self.set_name("Flask of Cerulean Tears")
        self.set_mana(10)
        self.set_description(f"The Flask of Cerulean Tears is a sacred flask modelled after a golden holy chalice that was once graced by a tear of life\nHeals {self.get_mana()} mana")

class DectusMedallionRight(loot):

    def __init__(self):
        super().__init__()
        self.set_name("Dectus Medallion (right)")
        self.set_description("The right half of a medallion with the power to break a powerful spell")

class DectusMedallionLeft(loot):

    def __init__(self):
        super().__init__()
        self.set_name("Dectus Medallion (left)")
        self.set_description("The left half of a medallion with the power to break a powerful spell")
        