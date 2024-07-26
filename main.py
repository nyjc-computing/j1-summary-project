# Import statements
import random
class William:
    def shout(self):
        print(''.join([i.upper() if random.randint(0,1) else i.lower() for i in "Hong Wei Lian"]))

if __name__ == "__main__":
    william = William()
    william.shout()
