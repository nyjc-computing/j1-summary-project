class Room:

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None

    def start(self):
        print(f'############{self.name}############')


def start_room():
    pass