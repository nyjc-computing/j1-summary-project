import data
import random

class Game:

    def __init__(self):
        self.gameover = False
        self.win = False

    def intro(self) -> None:
        """
        print intro message, instructions, etc.
        returns nothing 
        """
        print("""
Welcome to Valorant.
        
Your team all got killed by the Ranked Demon Reyna on the enemy team, you need to clutch. The Reyna will certainly one tap you the second you get into an encounter so the only way you're going to win this is by picking up enough shields (total 300hp) to not instantly die. Shield orbs can be found randomly throughout the map, and add 50hp to your character. There is still enemy utility scattered around the map, each piece you encounter will deduct 30hp from your character. You also have an agent ability, which will hopefully give you an edge over this no-lifer. 

Remember, Clutch or Gae.
        """)

    def agent_select(self) -> str:
        """
        retrive agent choice from player
        return agent name as string
        """
        confirm = "n"
        agents = ["jett","sova","omen","sage"]
        while confirm.lower() == "n":
            print("""
Choose your agent:
[1] Jett: Dash into an adjacent room if you would otherwise die (does not refresh)\n
[2] Sova: Scan an adjacent room for information (cooldown: 1 turn)\n
[3] Omen: Move to any room on the map (cooldown: 5 turns)\n
[4] Sage: Block a path from your current room to an adjacent one permanently (cooldown: 3 turns)
            """)
            out = input("Enter [1], [2], [3] or [4] to choose: ")
            while out not in [str(x) for x in range(1,5)]:
                print("Invalid Choice")
                out = input("Enter [1], [2], [3] or [4] to choose: ")
            print(f"\nYou have chosen {agents[int(out)-1]}.\n")
            confirm = input("Confirm? (y/n): ")
        return agents[int(out)-1]
            

    def map_select(self) -> None:
        """
        retrive map choice from player
        gets map
        """
        self.map = data.roomlist

    def initialise(self, agent: str) -> None:
        """
        scatters orbs and creatures through the map
        creates player class
        sets cooldown for player
        sets starting positions for reyna and player
        """
        
        creatures = 5
        orbs = 8
        spawn_areas = self.map[1:-1]
        
        spawn_creatures = random.sample(spawn_areas, creatures)
        for room in spawn_creatures:
            room.setcreature(True)
            
        spawn_orbs = random.sample(spawn_areas, orbs)
        for room in spawn_orbs:
            room.setorb(True)
            
        self.player = data.Player(100, agent)
        self.player_cooldown = 0

        self.player_pos = self.map[0]
        self.reyna_pos = self.map[-1]

    def desc(self) -> None:
        """
        describe the current room, presence of objects,
        available paths, current hp and ability usage options
        """
        print(f"\nYou are in {getattr(self.player_pos, 'name')}.")
        print(f"You have {getattr(self.player, 'hp')} hp.")
        print(f"\nYou can move to the following rooms: ")
        paths = getattr(self.player_pos, 'paths')
        for path in paths:
            print(path)
        print()
        if self.player_cooldown == 0:
            print("You can use your ability.")
        else:
            print(f"{self.player_cooldown} turns until you can use your ability.")
    
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

    def move(self) -> int:
        """
        move the player into an adjacent room
        or keeps them in the current one while
        passing the turn
        returns 1 if the turn passes, 0 if it does not
        """
        rooms = data.roomlist
        print("\nWhere do you want to go?")
        paths = getattr(self.player_pos, 'paths')
        for i, path in enumerate(paths):
            print(f"[{i+1}]: {path}")
        print(f"[{len(paths)+1}]: Cancel action")
        loc = input("Choose a number: ")
        while loc not in [str(x) for x in range(1, len(paths)+2)]:
            print("Invalid Input")
            loc = input("Choose a number: ")
        if int(loc) == len(paths) + 1:
            return 0
        else:
            loc = paths[int(loc)-1]
            print(loc)
            for room in self.map:
                if getattr(room, "name") == loc:
                    self.player_pos = room
                    return 1
            else:
                print("something has gone very wrong")


    def prompt(self) -> str:
        """
        get the user's action
        returns the selected action as a string
        """
        print("\nChoose an action 'Move' or 'Ability':")
        action = input()
        while action.lower() not in ["move", "ability"]:
            print("Invalid Choice")
            print("Choose an action 'Move' or 'Ability':")
            action = input()
        return action.lower()

    def reyna_turn(self) -> None:
        """
        Moves reyna to a room adjacent to her current
        room randomly
        """
        rooms = data.roomlist
        paths = getattr(self.reyna_pos, 'paths')
        move = random.choice(paths)
        for room in self.map:
            if getattr(room, "name") == move:
                self.reyna_pos = room
                return 1
        else:
            print("something has gone very wrong")

    def update(self) -> None:
        """
        adjust player hp based on presence of orbs, 
        creatures, and reyna
        returns None
        """
        print()
        if self.reyna_pos == self.player_pos:
            print("Reyna has found you!")
            self.gameover = True
            if getattr(self.player, "hp") >= 300:
                self.win = True
                print("Somehow, you manage to win the gunfight.")
            else:
                print("Reyna annihilates you before you can even register her presence.")

        if getattr(self.player_pos, "creature"):
            print("There is utility in this room, you lose 30 hp handling it.")
            self.player.set_hp(True, False)
            self.player_pos.setcreature(False)
            if getattr(self.player, "hp") <= 0:
                print("Unfortunately, it was enough to kill you.")
                self.gameover = True

        if getattr(self.player_pos, "orb"):
            print("There is a shield orb in this room, you gain 50 hp.")
            self.player.set_hp(False, True)
            self.player_pos.setorb(False)
            
    #main loop
    def run(self):
        """
        run the game
        """
        #initialise
        self.intro()
        agent = self.agent_select()
        self.map_select()
        self.initialise(agent)
        
        while not self.gameover:
            self.desc()
            advance = False
            while not advance:
                action = self.prompt()
                if action == "move":
                    temp = self.move()
                    if temp == 1:
                        advance = True
                elif action == "ability":
                    self.ability()
            self.update()
            self.reyna_turn()
            self.update()
        if self.win:
            print("VICTORY")
        else:
            print("DEFEAT")