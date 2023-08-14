import data
import random

class Game:

    def __init__(self):
        self.gameover = False

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
        confirm = "n"
        agents = ["jett, sova, omen, sage"]
        while confirm.lower() == n:
            print("""
            Choose your agent:
            [1] Jett: Dash into an adjacent 
            room if you would otherwise 
            die (does not refresh)\n
            [2] Sova: Scan an adjacent room for 
            information (cooldown: 1 turn)\n
            [3] Omen: Move to any room on 
            the map (cooldown: 5 turns)\n
            [4] Sage: Block a path from your 
            current room to an adjacent one 
            (cooldown: 3 turns)\n\n
            """)
            out = input("Enter [1], [2], [3] or [4] to choose: ")
            while int(out) not in range(1,5):
                print("Invalid Choice\n")
                out = input("Enter [1], [2], [3] or [4] to choose: ")
            print(f"You have chosen {agent[int(out)-1]}.\n")
            confirm = input("Confirm? (y/n): ")
        return agent[int(out)-1]
            

    def map_select(self) -> list:
        """
        retrive map choice from player
        return list of room objects
        """
        return data.roomlist

    def initialise(self, map: list, agent: string) -> list:
        """
        scatters orbs and creatures through the map
        sets starting positions for reyna and player
        returns modified map
        """
        
        creatures = 5
        orbs = 8
        spawn_areas = map[1:-1]
        
        spawn_creatures = random.sample(spawn_areas, creatures)
        for room in spawn_creatures:
            room.setcreature(True)  
            
        spawn_orbs = random.sample(spawn_areas, orbs)
        for room in spawn_orbs:
            room.setorb(True)
            
        self.player = data.Player(agent, 100)
        self.player_pos = map[0]
        self.reyna_pos = map[-1]
        
        return map

    def desc(self) -> None:
        """
        describe the current room, presence of objects,
        available paths, and ability usage options
        """
        print(f"You are in {getattr(self.player_pos, 'name')}.")
        
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

    def ability(self) -> None:
        """
        uses the player's ability based on
        the agent they selected
        """
        pass

    def move(self) -> None:
        """
        move the player into an adjacent room
        or keeps them in the current one while
        passing the turn
        returns None
        """
        pass
    
    def prompt(self) -> str:
        """
        get the user's action
        returns the selected action as a string
        """
        print("Choose an action:\n")
        action = input()
        while action.lower() not in ["move", "ability"]:
            print("Invalid Choice")
            print("Choose an action:\n")
            action = input()
        return action

    def reyna_turn(self) -> None:
        """
        Moves reyna to a room adjacent to her current
        room randomly
        """
        pass

    def update(self) -> None:
        """
        adjust player hp based on presence of orbs, 
        creatures, and reyna
        returns None
        """
        pass

    #main loop
    def run(self):
        """
        run the game
        """
        #initialise
        self.intro()
        agent = self.agent_select()
        map = self.map_select()
        self.initialise(map, agent)
        
        while not self.gameover():
            self.desc()
            advance = False
            while not advance:
                action = self.prompt()
                if action == "move":
                    self.move()
                    advance = True
                elif action == "ability":
                    self.ability()
            self.update()
            self.reyna_turn()
            self.update()