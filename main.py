
# Import statements
import random
import item
import character

#main game loop

import time
import rng
intro_text = "Myserious voice: 'I don't care! I seriously DON'T CARE! I have locked you up in my dungeon and you will never ever have the slightest of slimmer of hope in having the ability to even attempt to escape from this hell Ho of mine!"

# def main():
#     yes = True
#     while True:
#         print("Intro")
#         time.sleep(1)
#         print(intro_text)
#         time.sleep(5)
#         print("You wake up, dazed, who are you again?")
#         player = classes.Player(str(input("What is your name?")))
#         while yes:
#             confirm = input(f"Are you sure your name is {player}?(y/n):")
#             if confirm == "y":
#                 yes = False
#             elif confirm == "n":
#                   player = .Player(str(input("What is your name?")))
#             else:
#                 print("Answer the question please")


if __name__ == "__main__":
    hero = character.Player("Matthew", 10)
    print(hero.health)
    
