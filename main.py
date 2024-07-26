
# Import statements
import time, classes
import rng
def main():
    yes = True
    while True:
        print("Intro")
        time.sleep(1)
        print("Myserious voice: 'I don't care! I seriously DON'T CARE! I have locked you up in my dungeon and you will never ever have the slightest of slimmer of hope in having the ability to even attempt to escape from this hell Ho of mine!")
        time.sleep(5)
        print("You wake up, dazed, who are you again?")
        player = classes.Player(str(input("What is your name?")))
        while yes:
            confirm = input(f"Are you sure your name is {player}?(y/n):")
            if confirm == "y":
                yes = False
            elif confirm == "n":
                  player = classes.Player(str(input("What is your name?")))
            else:
                print("Anser the question please")
                
        
        # object = classes.Object(3, "ee")
        # object2 = classes.Object(4, "dd")
        dict = {}
        print(dict[2])
        # dict[1] = object
        # dict[2] = object2
        # print(dict)
        # for i in dict.values():
        #     print(i.item)

if __name__ == "__main__":
    rng.rng_game()
