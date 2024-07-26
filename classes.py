class Gears:
    def __init__(self):
        self.helmet = (None)
        self.chestplate = (None)
        self.leggings = (None)
        self.boots = (None)
        self.accessories = (None)
        pass
class Backpack: #store, display, check, destroy
    def __init__(self, slots):
        self.items = {}
        self.backpack_size = slots

    def store(self, item):
        if item in self.items:
            self.items[item] += number
            print(f'{item} * {number} has been stored')
            return
        if len(self.items) >= self.backpack_size:
            print("Backpack is full!")
            return
        self.items[item] = number
        print(f'{item} * {number} has been stored.')
        return
        
    def display(self):
        lst = []
        for item in self.items:
            lst.append(item)
        disp = ', '.join(lst)
        return disp

    def check(self, item):
        pass