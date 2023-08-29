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

class PortalGun(Upgrade):

    def __init__(self):
        super().__init__()
        self.name = "Portal Gun"
        self.description = "The Portal Gun is a hand-held device which has the ability to manufacture two linked portals. No matter the distance between them, any object which passes through one portal will emerge from the other and vice versa instantaneously"
    