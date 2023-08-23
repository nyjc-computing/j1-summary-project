import game
import data
import random
class Test:
    def __init__(self):
        pass

    def select_ag(self):
        p = game.Game
        print(p.agent_select(p, random.randint(0,3)))

    def select_map(self):
        p = game.Game
        p.map_select(p,random.randint(0,2))

    def omen_ab(self):
        p = game.Game
        p.omen(p,random.randint(0,15))







x = Test
x.select_ag(0)
x.select_map(0)
x.omen_ab(0)