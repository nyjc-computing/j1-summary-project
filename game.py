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


class Player:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.position = (3, 3)
        self.inventory = []

    def pick_up(self, item_name):
        if item_name in items:
            self.inventory.append(item_name)
            print(f'You picked up a {item_name}!')
        else:
            print(f'There is no {item_name} here.')

    def use_item(self, item_name):
        if item_name not in self.inventory:
            print(f'You do not have a {item_name} to use.')
            return

        if item_name == 'Mango':
            self.attack += items['Mango']['value']
            print(f'You used a Mango. Your attack is now {self.attack}.')
            self.inventory.remove('Mango')
        elif item_name == 'Apple':
            if random.random() < 0.9:
                self.health += items['Apple']['value']
                print(f'You used an Apple. Your health is now {self.health}.')
            else:
                self.health -= 10
                print(
                    f'You used an Apple but felt weak. Your health is now {self.health}.'
                )
            self.inventory.remove('Apple')

    def display_stats(self):
        print(f'Health: {self.health}')
        print(f'Attack: {self.attack}')
        print(f'Inventory: {self.inventory}')


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
        self.item_positions = {(1, 1): 'Mango'}
        self.player = None

    def print_map(self):
        area = [['X' for _ in range(7)] for _ in range(7)]

        for (item_x, item_y), item_name in self.item_positions.items():
            area[item_x][item_y] = ITEM

        player_x, player_y = self.player.position
        area[player_x][player_y] = PLAYER

        for row in area:
            print(' '.join(row))
        print()

    def start(self):
        print("~ Welcome to the fruit forest! ~")
        name = input("Enter your name: ")
        self.player = Player(name)
        self.print_map()
        self.player.display_stats()

    def game_over(self):
        return self.player.health <= 0

    def options(self):
        return [
            'Move left', 'Move right', 'Move up', 'Move down',
            'Pick up an item', 'Use an item'
        ]

    def choose_option(self, options):
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        choice = input("Choose an option: ")

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            return None

    def do(self, choice):
        if choice == 1:
            self.move_player(0, -1)
        elif choice == 2:
            self.move_player(0, 1)
        elif choice == 3:
            self.move_player(-1, 0)
        elif choice == 4:
            self.move_player(1, 0)
        elif choice == 5:
            self.pick_up_item()
        elif choice == 6:
            item_name = input("Enter the item you want to use: ")
            self.player.use_item(item_name)
        else:
            print("Invalid choice!")

        self.print_map()
        self.player.display_stats()

    def move_player(self, dx, dy):
        new_x = self.player.position[0] + dx
        new_y = self.player.position[1] + dy
        if 0 <= new_x < 7 and 0 <= new_y < 7:
            self.player.position = (new_x, new_y)
        else:
            print("You can't move outside the map!")

    def pick_up_item(self):
        x, y = self.player.position
        if (x, y) in self.item_positions:
            item_name = self.item_positions[(x, y)]
            self.player.pick_up(item_name)
            del self.item_positions[(x, y)]
        else:
            print("There is no item here.")