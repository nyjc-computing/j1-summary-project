import storyline
import level
import entities
class Game():
    def __init__(self):
        self.storyData = storyline.Storyline()
        self.level = level.level()
        
        self.currentTilePos = self.storyData.starting_tile
        self.levelEnded = False
        self.hasIntroduced = False
        # TODO: read tile data from storyline and populate level tilelist
    
    def runGame(self, currentLevel):
        while not self.levelEnded:
            # Do an intro, if necessary
            if self.hasIntroduced == False:
                intro = self.storyData.getIntro(currentLevel)
                print(intro)
            """
            Get current tile info
            This stores tile with all its data. 
            self.currentTile stores the coordinates
            """
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
        Takes a coordinate and returns a tile object
        """
        db = {}
        for tile in self.level.tileList:
            if tile.position == targetTileCoord:
                
                