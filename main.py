# Import statements
import time, classes
def main():
    print("Intro")
    player = classes.Player(str(input("What is your name?")))
    print(player)
    # object = classes.Object(3, "ee")
    # object2 = classes.Object(4, "dd")
    dict = {}
    backpack = Backpack(10)
    backpack.store
    # dict[1] = object
    # dict[2] = object2
    # print(dict)
    # for i in dict.values():
    #     print(i.item)
if __name__ == "__main__":
    main()
