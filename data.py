# Import statements
import json

# class instantiation
class Item:
    def __init__(self):
        pass

class Creature:
    def __init__(self):
        pass

# write data into json file
with open("content/items.json", "r") as f:
    items = json.load(f)