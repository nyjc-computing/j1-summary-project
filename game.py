import entities
import level
import items
import map
import storyline
from level import Tile
import json

# Util function for clearing console

with open("Tile_data.json") as f:
    _tile_data = json.load(f)

class Game:
    def __init__(self):
        self.map = map.Map()
        self.storyline = storyline.Storyline()
        self.level = level.Level(_tile_data, 1)
        self.levelEnded = False
        self.hasIntroduced = False
        # TODO: read tile data from storyline and populate level tilelist
    
    def create_tile_from_position(self, x, y):
        for _tile in _tile_data:
            if _tile["position"] == [x, y]:
                return Tile([x, y], _tile["description"])
            else:
                return Tile([x, y], "Empty Tile")


    def start(self):
        self.level.spawn_BigBoss()
        self.level.spawn_monsters()
        self.level.spawn_items()
        self.storyline.do_intro()
        name = input("Brave adventurer! What is your name?")
        self.player = entities.Player(name, health = 100, aura = 0, position = [1,1])
        self.show_status()
        pass
        
    def win(self):
        return self.level.BigBoss.dead()
    
    def lose(self):
        return self.player.dead()
        
    def get_options(self) -> list[str]:
        """Returns player's current options as a list of strs"""
        options = []
        return options
    
    def enter(self, choice: str) -> None:
        """Carry out player choice"""
        pass
    
    def show_status(self) -> None:
        """Display player's current status"""
        player_position = self.get_player_position()
        player_inventory = self.get_player_inventory()
        player_health = self.get_player_health()
        player_aura = self.get_player_aura()
        print(f'Your Name: {self.player.get_name()} \nYour Health: {player_health} \nYour Aura: {player_aura} \nYour position: {player_position} \nYour Inventory: {player_inventory}')

    def get_player_position(self):
        return self.player.get_position()
    
    def get_player_inventory(self):
        return self.player.get_inventory()

    def get_player_health(self):
        return self.player.get_health()

    def get_player_aura(self):
        return self.player.get_aura()

    

    
    

