# import character
import csv

class Room:

    def __init__(self, name, prev_room, next_room, enemy_num):
        self.name = name
        self.prev = prev_room
        self.next = next_room
        self.enemy_num = enemy_num

    def prev_room(self):
        return self.prev
        
    def next_room(self):
        return self.next

    def get_enemy_num(self):
        return self.enemy_num

    def enemy_defeated(self):
        self.enemy_num -= 1
        if self.enemy_num <= 0:
             print(f'Enemies in {self.name} have all been defeated!')

    