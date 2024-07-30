# import character
import csv

class Room:

    def __init__(self, name, next, enemy_num):
        self.name = name
        self.next = next
        self.enemy_num = enemy_num

    def display(self):
        print(f'name: {self.name}, next rooms: {self.next}, number of enemies: {self.enemy_num}')

with open('room_data.csv', 'r') as f:
    header = f.readline().strip().split(',')
    for room in f.readlines():
        room = room.strip().split(',')
        print(room)
#         name = room[0]
#         name = Room(room[0], room[1], room[2], room[3])
#         name.display()

# bedroom.display()