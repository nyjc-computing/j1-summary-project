import random
import json
class storyline:
    def map_list(self):
        lst = []
        with open('level1.txt','r') as f:
            for line in f.readlines():
                lst.append(line)
        return lst
    def map_load(self):
        map = ''
        lst = self.map_list()
        for tile in lst:
            map += tile
        return map

    def get_tile_info(self):
        with open('Tile_data.txt', 'r', encoding='utf-8') as f:
            data_dict = json.load(f)
        return data_dict

    def get_intro(self):
        return "Welcome to the game!"
                
        
                 
test = storyline()
print(test.map_load())
print(test.get_tile_info())
