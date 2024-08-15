from time import sleep
import storyline
import level
import entities

# Util function for clearing console
def clearConsole():
    print("\033c", end="", flush=True)

class Game:
    def __init__(self):
        self.storyData = storyline.Storyline()
        self.level = level.level()
        
        self.currentTilePos = self.storyData.starting_tile
        self.levelEnded = False
        self.hasIntroduced = False
        
        # TODO: read tile data from storyline and populate level tilelist
    
    def runGame(self, currentLevel):
        """
        Get current tile info
        This stores tile with all its data. 
        self.currentTile stores the coordinates
        """
        while not self.levelEnded:
            # Do an intro, if necessary
            if self.hasIntroduced == False:
                print("Brave adventurer! What is your name?")
                name = input()
                # Init player object
                self.player = entities.Player(name, 100, 100, self.currentTilePos)
                intro = self.storyData.getIntro(currentLevel)
                
                print(intro)
                sleep(3000)
                clearConsole()
            
            currTile = self.findTile(self.currentTilePos)
            
            # Display description
            print(currTile.display())
            
            # TODO: print out possible actions
            # Optional: add minimap? If we have a lot of time
            # Take movement input
            playerInput = input().lower()
            # Check if its valid
            if self.actions.actionList.count(playerInput) == 1:
                #TODO: carry out action
                
                pass
            #TODO: add monster validation logic
    
    def findTile(self, targetTileCoord):
        """
        Utility function for finding tiles.
        Takes a coordinate and returns a tile object
        """
        for tile in self.level.tileList:
            if tile.position == targetTileCoord:
                return tile
        
    def findAdjacentTiles(self, targetTileCoord):
        """
        Utility function for finding tiles.
        Takes a coordinate and returns a list of adjacent tile objects
        """
        db = {}
        for tile in self.level.tileList:
            if tile.position == targetTileCoord:
                # We have our target tile
                return {
                    "UP":  self.findTile([tile.position[0], tile.position[1] + 1]),
                    "DOWN":  self.findTile([tile.position[0], tile.position[1] - 1]),
                    "LEFT":  self.findTile([tile.position[0] - 1, tile.position[1]]),
                    "RIGHT":  self.findTile([tile.position[0] + 1, tile.position[1]]),
                }
               
