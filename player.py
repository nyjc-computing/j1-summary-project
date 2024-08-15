from moves import Moves
from character import Character

class Player(Character):
    def __init__(self):
        super().__init__()
        self.moves = []
    
    def set_name(self):
        self.name = input("Enter the name of user: ")
        
    def display_stats(self):
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack}")