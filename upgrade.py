class Upgrade:
    def __init__(self):
        self.type = "upgrade"
        self.name = ""
        self.description = ""

class VirtualBoo(Upgrade):

    def __init__(self):
        super().__init__()
        self.name = "Virtual Boo"
        self.description = "The Virtual Boo is a high tech handheld created by Professor E. Gadd. It allows the user to see things not normally seen through the naked eye"
    