# Import statements

from game import Game

if __name__ == "__main__":
    play = Game()
    play.intro()
    while play.end == False:
        play.run()
