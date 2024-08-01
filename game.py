from player import Player
import random

BLANK = 'X'
ITEM = 'I'
PLAYER = 'P'

items = {
    'Mango': {
        'type': 'attack',
        'value': 5
    },
    'Apple': {
        'type': 'health',
        'value': 20,
        'chance': 0.1
    }
}

class Game:

    def __init__(self):
        self.map = [
            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'I', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'P', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ]
        self.player = Player()