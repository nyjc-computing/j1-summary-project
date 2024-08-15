from player import Player
import sys
import random

class Game:
    def __init__(self):
        self.turns_to_monster = 1

    def start(self, player):
        player.set_name()

    def display_options(self): # change later
        print("""
What would you like to do?
1. Exercise
2. Eat
3. Sleep 
4. Display Stats
        """)
        self.choice = input()
        self.do()

    def do(self): # changer later also
        if self.choice == "1":
            print("you exercised")
            self.turns_to_monster -= 1
        elif self.choice == "2":
            print("you eat")
            self.turns_to_monster -= 1
        elif self.choice == "3":
            print("you slept")
            self.turns_to_monster -= 1
        else:
            print("invalid choice")
            self.display_options()

        if self.turns_to_monster == 0:
            self.final_battle()

    def final_battle(self):
        print("you fought and won")
        sys.exit(0)

    def game_over(self, player):
        return player.get_hp() <= 0