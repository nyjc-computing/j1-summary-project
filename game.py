class MUDGame:
    def __int__(self):
        self.spawn = Room('home', up='closed')
        self.gameOver = True
    
    def run(self):
        while self.gameOver:
            


class Room:
    def __int__(self, type, up = None, down = None, left = None, right = None, number = 0):
        self.current = type
        self.up = up
        self.down = down 
        self.right = right
        self.left = left
        self.count = number

    def nextRoom(self, next : str):
        if next.lower() == 'w':
            if self.up == None:
                print('It seems that this door is locked.')
            else:
                prev = self
                self.up = Room('creature', up = prev, number=countRoom())
                self = self.up
        if next.lower() == 's':
            if self.down == None:
                print('It seems that this door is locked.')
            else:
                prev = self
                self.down = Room('creature', down = prev, number=countRoom())
                self = self.down
        if next.lower() == 'a':
            if self.left == None:
                print('It seems that this door is locked.')
            else:
                prev = self
                self.left = Room('creature', right = prev, number=countRoom())
                self = self.left
        if next.lower() == 'd':
            if self.right == None:
                print('It seems that this door is locked.')
            else:
                prev = self
                self.right = Room('creature', left = prev, number=countRoom())
                self = self.right

    def countRoom(self):
        return self.count + 1
        