import json
import random

import entities
import items



class Level:
    """
    generate new level by the size given
    level_num --> int
    """
    def __init__(self, tile_list, level_num):
        self.tile_list = tile_list
        self.level_num = level_num
        self.monsters_list = []
        self.items_list = []
        self.BigBoss = entities.Monsters("BIGBOSS", 1000, [20,10], 90, "FINAL BOSS, Defeat to Complete Level")

    def get_levelnumber(self):
        """
        print the level number
        """
        print(self.level_num)

    def get_floorplan(self):
        """
        return the level generated
        """
        return self.tile_list

    def take_monster(self, monster: entities.Monsters) -> None:
        self.monsters_list.append(monster)

    def take_item(self, item: items.Item) -> None:
        self.items_list.append(item)

    def spawn_BigBoss(self):
        last_tile = Tile([20,10], "FINAL TILE")
        last_tile.set_monster(self.BigBoss)
        
    def spawn_monsters(self):
        """
        randomly add monsters into tiles
        """
        for i in range(len(self.monsters_list)):
            new_tile = random.choice(self.tile_list)
            if new_tile.get_monster() is None:
                self.monsters_list[i].position = new_tile.position
                new_tile.set_monster(self.monsters_list[i])
            else:
                i -= 1

    def spawn_items(self):
        """
        randomly add items into tiles
        """
        for i in range(len(self.items_list)):
            new_tile = random.choice(self.tile_list)
            if new_tile.get_item() is None:
                self.items_list[i].position = new_tile.position
                new_tile.set_item(self.items_list[i])
            else:
                i -= 1







class Tile:

    def __init__(self, position, description):
        self.position = position
        self.description = description
        self.monster = None
        self.item = None

    def get_position(self):
        return self.position

    def get_description(self):
        return self.description
    
    def set_monster(self,monster):
        self.monster = monster

    def set_item(self,item):
        self.item = item
    
    def get_item(self):
        return self.item

    def get_monster(self):
        return self.monster





