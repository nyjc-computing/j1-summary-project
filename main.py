from game import Game

if __name__ == "__main__":
    player = Player()
    game = Game()
    #monster = Monster()
    game.start(player)

    while not game.game_over(player):
        choice = game.options()
        game.do(choice)

    print("Died")