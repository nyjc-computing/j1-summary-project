import game 
import data
import random
class Test:
    def __init__(self):
        pass


    def select_ag(self):
        p = game.Game()
        print(p.agent_select(random.randint(0,3)))

    def select_map(self):
        p = game.Game()
        p.map_select(random.randint(0,2))
        

    def omen_ab(self):
        p = game.Game()
        p.map_select(1)
        a = random.randint(0,len(data.make_map('ascent')))
        print(a,data.make_map('ascent'))
        p.omen(a)

    def prompt_test(self):
        p = game.Game()
        p.prompt(['Option A', 'Option B', 'Option C','Option 4'],'Test input', False)





p = game.Game()
x = Test()
x.select_ag()
x.select_map()
x.prompt_test()
x.omen_ab()