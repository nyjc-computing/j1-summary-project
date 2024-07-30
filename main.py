# Import statements

if __name__ == "__main__":
    player = create_player()
    game = Game()
    game.setup()
    while not game.over():
        # get list of choices
        choices = game.get_choices()
        choice = get_player_choice(choices)
        game.execute(choice)


class Game:
    def __init__(self):
        self.player = None
        self.rooms = []
        self.now = 0

    def setup(self):
        self.player = Player()
        self.rooms.append(Bedroom())

    def isover(self):
        return self.player.isdead()