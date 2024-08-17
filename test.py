from game import Game

def test_1():
    game = Game()
    game.set_player_name("testplayer")
    here = game.get_player_position()
    game.move("left")
    game.move("right")
    assert game.get_player_position() == here

def test_2():
    pass

if __name__ == "__main__":
    test_1()