class Upgrade:
    def __init__(self):
        self.type = "upgrade"
        self.name = ""
        self.description = ""

class VirtualBoo(Upgrade):

    def __init__(self):
        super().__init__()
        self.name = "Virtual Boo"
        self.description = "The Virtual Boo is a high tech handheld created by Professor E. Gadd. It allows the user to see things not normally seen through the naked eye\nAllows the user to see enemy health and hidden loot when looking around a room"

class PortalGun(Upgrade):

    def __init__(self):
        super().__init__()
        self.name = "Portal Gun"
        self.description = "The Portal Gun is a hand-held device which has the ability to manufacture two linked portals. No matter the distance between them, any object which passes through one portal will emerge from the other and vice versa instantaneously\nAllows the user to teleport to any room they have been to before"

class Shield(Upgrade):
    """placeholder shield"""
    def __init__(self):
        super().__init__()
        self.name = "Shield"
        self.description = "literally sheet metal on a stick. good enough for shielding"

class Flee(Upgrade):
    """placeholder flee"""
    def __init__(self):
        super().__init__()
        self.name = "Flee"
        self.description = "The secret family technique of the joestars. use it wisely"