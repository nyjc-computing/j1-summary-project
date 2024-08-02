class Room:

    def __init__(self, name, enemy_num):
        self.name = name
        self.enemy_num = enemy_num

    def get_enemy_num(self):
        return self.enemy_num

    def enemy_defeated(self):
        self.enemy_num -= 1
        if self.enemy_num <= 0:
             print(f'Enemies in {self.name} have all been defeated!')

    def __repr__(self):
        return f"Name: {self.name}\nNumber of enemies: {self.enemy_num}"
