from game import Game

def test_1():
    game = Game()
    game.set_player_name("testplayer")
    here = game.current_room()
    game.move("left")
    game.move("right")
    assert game.current_room() == here

def test_2():
    pass

if __name__ == "__main__":
    test_1()