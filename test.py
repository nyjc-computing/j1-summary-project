#File for QAE

from data import Labyrinth

def test_lbr_init():
    try:
        lb = Labyrinth()
    except:
        import pdb; pdb.set_trace()

lb = Labyrinth()

# def test_lbr_repr():
#     #not implemented
#     pass

# def test_lbr_generate():
#     try:
#         lb.generate()
#         print("OK")
#     except:
#         import pdb; pdb.set_trace()
        
# from game import MUDGame

# def test_game():
#     # Write code to test the game object here
#     # Raise an error if the test fails
#     pass

# test_lbr_init()
# test_lbr_repr()
# test_lbr_generate()
# test_game()

lb.generate()
