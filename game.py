import data
import random

class Game:

    def __init__(self):
        pass

    def gameover(self) -> bool:
        """
        returns True if game is over, else return False
        """
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
    
    def sova(self, room: str) -> None:
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
        modifies health based on orbs/creatures/reyna
        """
        pass
    
    def prompt(self) -> None:
        """
        get the user's action
        returns the selected action as a string
        """
        pass

    def reyna_turn(self) -> None:
        """
        Moves reyna to a room adjacent to her current
        room randomly
        """
        pass

    



    
    def run(self):
        """
        run the game
        """
        #initialise
        self.intro()
        agent = self.agent_select()
        map = self.map_select()

        kill me now please
        
        while not self.gameover():
            self.desc()
            advance = False
            while not advance:
                action = self.prompt()
                if action == move:
                    self.move()
                    advance = True
                elif action == ability:
                    self.ability()
            self.reyna_turn()
            