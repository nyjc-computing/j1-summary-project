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
        print("""Welcome to Valorant.
        
Your team all got killed by the Ranked Demon Reyna on the enemy team, 
you need to clutch. 

The Reyna will certainly one tap you the second you get into an encounter so the only way you're going to win this is by picking up enough shields (total 300hp) to not instantly die. 

Shield orbs can be found randomly throughout the map, and add 50hp to your character. 

There is still enemy utility scattered around the map, each piece you encounter will deduct 30hp from your character. 

You also have an agent ability, which will hopefully give you an edge over this no-lifer. 

Remember, Clutch or Gae.
=====================================================""")

    def agent_select(self) -> str:
        """
        retrive agent choice from player
        return agent name as string
        """
        confirm = "n"
        agents = ["jett","sova","omen","sage"]
        while confirm.lower() == "n":
            print("""Choose your agent:

[1] Jett: Dash into an adjacent room if you would otherwise die (does not refresh)\n
[2] Sova: Scan an adjacent room for information (cooldown: 1 turn)\n
[3] Omen: Move to any room on the map (cooldown: 5 turns)\n
[4] Sage: Block a path from your current room to an adjacent one permanently (cooldown: 3 turns)
=====================================================""")
            out = input("Enter 1, 2, 3 or 4 to choose: ")
            while out not in [str(x) for x in range(1,5)]:
                print("Invalid Choice")
                out = input("Enter 1, 2, 3 or 4 to choose: ")
            print(f"\nYou have chosen {agents[int(out)-1]}.")
            confirm = input("Confirm? (y/n): ")
            print("=====================================================")
        print("--GAME START--")
        print("=====================================================")
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
            room.set_creature(True)
            
        spawn_orbs = random.sample(spawn_areas, orbs)
        for room in spawn_orbs:
            room.set_orb(True)
            
        self.player = data.Player(100, agent)
        self.player_cooldown = 0

        self.player_pos = self.map[0]
        self.reyna_pos = self.map[-1]

    def desc(self) -> None:
        """
        describe the current room, presence of objects,
        available paths, current hp and ability usage options
        """
        print(f"You are in {self.player_pos.get_name()}.")
        print(f"You have {self.player.get_hp()} hp.")
        print("\nYou can move to the following rooms: ")
        paths = self.player_pos.get_paths()
        for path in paths:
            print(path)
        print()
        if self.player_cooldown == 0:
            print("You can use your ability.")
        else:
            print(f"{self.player_cooldown} turns until you can use your ability.")
        print("=====================================================")
    
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
    
    def omen(self) -> None:
        """
        moves player to any room
        """
        for i, room in enumerate(self.map):
            print(f"[{i+1}]: {room.get_name()}")
        print(f"[{len(self.map)+1}]: Cancel action")
        choice = input("Choose a number: ")
        while choice not in [str(x) for x in range(1, len(self.map)+2)]:
            print("Invalid input")
            choice = input("Choose a number: ")
        if int(choice) == len(self.map)+1:
            return None
        else:
            choice = self.map[int(choice)-1]
            self.player_pos = choice
            self.player_cooldown = 5
            self.update()

    def ability(self) -> None:
        """
        uses the player's ability based on
        the agent they selected
        """
        if self.player_cooldown == 0:
            agent = self.player.get_agent()
            if agent == "omen":
                self.omen()
            elif agent == "sova":
                self.sova()
            elif agent == "sage":
                self.sage()
            else:
                print("jett's ability cannot be manually activated")
        else:
            print("Your ability is on cooldown.")
    def move(self) -> int:
        """
        move the player into an adjacent room
        or keeps them in the current one while
        passing the turn
        returns 1 if the turn passes, 0 if it does not
        """
        rooms = data.roomlist
        print("\nWhere do you want to go?")
        paths = self.player_pos.get_paths()
        for i, path in enumerate(paths):
            print(f"[{i+1}]: {path}")
        print(f"[{len(paths)+1}]: Cancel action")
        loc = input("Choose a number: ")
        while loc not in [str(x) for x in range(1, len(paths)+2)]:
            print("Invalid Input")
            loc = input("Choose a number: ")
        if int(loc) == len(paths) + 1:
            print("=====================================================")
            return 0
        else:
            loc = paths[int(loc)-1]
            print(loc)
            for room in self.map:
                if room.get_name() == loc:
                    self.player_pos = room
                    print("=====================================================")
                    return 1
            else:
                print("something has gone very wrong")


    def prompt(self) -> str:
        """
        get the user's action
        returns the selected action as a string
        """
        print("Choose an action, Move (1) or Ability (2):")
        action = input()
        while action.lower() not in ["1", "2"]:
            print("Invalid Choice")
            print("Choose an action, Move (1) or 'Ability' (2):")
            action = input()
            
        return action

    def reyna_turn(self) -> None:
        """
        Moves reyna to a room adjacent to her current
        room randomly
        """
        rooms = data.roomlist
        paths = self.reyna_pos.get_paths()
        move = random.choice(paths)
        for room in self.map:
            if room.get_name() == move:
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
        if self.reyna_pos == self.player_pos:
            print("Reyna has found you!")
            self.gameover = True
            if self.player.get_hp() >= 300:
                self.win = True
                print("Somehow, you manage to win the gunfight.")
            else:
                print("Reyna annihilates you before you can even register her presence.")
        else:
            if self.player_pos.has_creature():
                print("There is utility in this room, you lose 30 hp handling it.\n")
                self.player.set_hp(True, False)
                self.player_pos.set_creature(False)
                if self.player.get_hp() <= 0:
                    print("Unfortunately, it was enough to kill you.")
                    self.gameover = True
    
            if self.player_pos.has_orb():
                print("There is a shield orb in this room, you gain 50 hp.\n")
                self.player.set_hp(False, True)
                self.player_pos.set_orb(False)
            
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
                if action == "1":
                    temp = self.move()
                    if temp == 1:
                        advance = True
                elif action == "2":
                    self.ability()
                    if self.gameover == True:
                        break
                    else:
                        self.desc()
            if self.player_cooldown != 0:
                self.player_cooldown -= 1
            if self.gameover == True:
                break
            else:
                self.update()
            if self.gameover == True:
                break
            else:
                self.reyna_turn()
                self.update()
        if self.win:
            print("VICTORY")
        else:
            print("DEFEAT")