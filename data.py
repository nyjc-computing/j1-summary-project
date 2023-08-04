#File for data designer

import json


class Item:
    def __init__(self, ...):
        ...


class Creature:
    def __init__(self, ...):
        ...


with open("content/items.json", "r") as f:
    items = json.load(f)
