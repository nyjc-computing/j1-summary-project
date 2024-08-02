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
            # Get current tile info
            #This stores tile with all its data. self.currentTile stores the coordinates
            currTile = self.findTile(self.currentTilePos)
            # Display description
            print(currTile.display())
            # TODO: print out possible actions
            # Optional: add minimap? If we have a lot of time
            # Take movement input
            playerInput = input()
            if self.actions.actionList.find
    def findTile(self, targetTile):
        """
        Utility function for finding tiles.
        Takes a coordinate and returns a tile object
        """
        for tile in self.level.tileList:
            if tile.position == targetTile:
                return tile
        
            