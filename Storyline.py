import random
import json
class storyline:
    def __init__(self):
        self.size = 200
        self.starting_tile = [0,0]
        
    def map_creation(self):
        grid = []
        for tile in range(self.size):
            grid.append('0')
        return grid
        
    def map_display(self):
        grid = self.place_walls()
        map = ''
        count = 0
        for tile in grid:
            count += 1
            map += tile
            map += " "
            if count == 20:
                map += '\n'
                count = 0
        return map
        
    def place_walls(self):
        grid = self.map_creation
        wall_pos = 43
        checker = []
        for element in range(6):
            wall_pos2 = wall_pos + 3
            checker.append(wall_pos)
            checker.append(wall_pos2)
            wall_pos += 20
        for pos in range(len(grid)):
            for check in checker:
                if pos == check:       
                    grid[pos] = " "
        return grid

    def map_load(self):
        lst = []
        map = ''
        with open('level1.txt','r') as f:
            for x in f.readlines():
                lst.append(x)
        for tile in lst:
            map += tile
        return map

    def get_tile_info(self):
        with open('Tile_data.txt', 'r', encoding='utf-8') as f:
            data_dict = json.load(f)
        return data_dict
                
                
        
                 
test = storyline()
print(test.map_load())
print(test.get_tile_info())
