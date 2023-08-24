#File for QAE
# for each critical method, test the method (template is test_attack(), think abt what the mtd does/outcome aft method is run) !!!!!

from data import Labyrinth

def test_lbr_init():
    lb = Labyrinth()
    
# test_lbr_init()
# lb = Labyrinth()
# lb.generate()

from game import MUDGame

mg = MUDGame()

def test_attack():
    """Check that the attack() method"""
    mg.attack()
    assert mg.steve.isdead() or mg.creature.isdead()

mg.item_found()