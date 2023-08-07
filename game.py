import data
import random

class Game:

    def __init__(self):
        pass

    def intro(self) -> None:
        """
        print intro message, instructions, etc.
        returns nothing 
        """
        pass

    def agent_select(self) -> str:
        """
        retrive agent choice from player
        return agent name as string
        """
        pass

    def map_select(self) -> str:
        """
        retrive map choice from player
        return map name as string
        """
        pass

    def desc(self) -> str:
        """
        describe the current room, presence of objects,
        available paths, and ability usage options
        """
        pass
    
    def sova(self, room: str) -> list:
        """
        return creature presence and orb presence in a room
        adjacent to the player's
        """
        pass

    def sage(self, room: str) -> None:
        """
        blocks a path between two rooms permanently
        """
        pass

    def jett(self, room: str) -> None:
        """
        if player is about to die, moves player
        to an adjacent room of the player's choice
        and avoid death
        """
        pass
    
    def omen(self, room: str) -> None:
        """
        moves player to any room
        """
        pass

    def ability(self, agent) -> None:
        """
        uses the player's ability based on
        the agent they selected
        """
        pass

    def move(self) -> None:
        """
        move the player into an adjacent room,
        modifies health based on orbs/creatures,
        advance turn
        """
        pass
    
    def prompt(self) -> None:
        """
        get the user's action
        """
        pass

    def 





    
    def run(self):
        """
        run the game
        """
        #initialise
        self.intro()
        agent = self.agent_select()
        map = self.map_select()
        cont = True

        kill me now please
        
        while cont:
            self.desc()
            self.prompt()