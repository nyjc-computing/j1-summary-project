#File for QAE

from data import Labyrinth

def test_labyrinth():
    try:
        lb = Labyrinth()
    except:
        import pdb; pdb.set_trace()
        
from game import MUDGame

def test_game():
    # Write code to test the game object here
    # Raise an error if the test fails

test_labyrinth()
test_game()
