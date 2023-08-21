#File for QAE

from data import Labyrinth

def test_lbr_init():
    try:
        lb = Labyrinth()
    except:
        import pdb; pdb.set_trace()

# lb = Labyrinth()
# lb.generate()

from game import MUDGame

mg = MUDGame()
mg.show_options('restart')