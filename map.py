class map:
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
    def get_starting_tile(self):
        x = 1
        y = 1
        lst = self.map_list()
        for text in lst:
            for e in text:
                if e == "S":
                    return x,y
                else:
                    x += 1
            x = 1
            y += 1