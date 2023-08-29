#import from python built in libraries
import time
import random

#import from other files
from setup import *

class Game:
    """
    A class that creates an instance of the game

    Attributes
    ----------
    - end : bool
      True when game ends, False otherwise
    - room : Room
      Class for the room the player is in
    - character : Character
      Class of the character
    - actions : list[str]
      List of possible actions
    - description : list[str]
      List of description of possible actions

    Methods
    -------
    + intro(self) -> None
    + run(self) -> None
    - help(self) -> None
    - look(self, room : Room) -> None
    - move(self, room : Room) -> None
    - loot(self, user : Character, loot : Item) -> None
    - flask(self, user : Character) -> None
    - attack(self, attacker : Character , victim: Enemy) -> None
    - get_choice(self, user : Character) -> str
    - get_attack(self, user : Character, decision : str) -> [int, Weapon]
    - use_flask_battle(self, user : Character) -> None
    - use_flask(self, user : Character) -> None
    - display_flask(self, user : Character) -> None
    - equip(self, user) -> None
    - display_equipment(self, user : Character) -> None
    - display_spells(self, user : Character) -> None
    - equip_armour(self, user : Character) -> None
    - equip_weapon(self, user : Character) -> None
    - equip_accessory(self, user : Character) -> None
    - status(self, user : Character) -> None
    - info(self, user : Character) -> None
    - weapon_info(self, user : Character) -> None
    - spell_info(self, user : Character) -> None
    - armour_info(self, user : Character) -> None
    - accessory_info(self, user : Character) -> None
    - flask_info(self) -> None
    - item_info(self, user : Character) -> None
    - display_room_name(self) -> None
    - display_room_description(self) -> None
    - get_action(self) -> str
    - collect_loot(self, attacker : Character, loot : Item) -> None
    - end_game(self) -> None
    - win(self, weapon) -> None
    - die(self) -> None
    - meow(self) -> None
    - secret(self) -> None
    """
    
    def __init__(self) -> None:
        temp = setup()
        self.end = False
        self.room = temp[0]
        self.character = temp[1]
        self.rooms = []
        self.actions = ["help", "look", "move", "loot", "flask", "attack", "equip", "status", "info", "die", "settings", "meow"]
        self.description = ["Gets the list of possible actions", "Looks around the room","Move to another room", "Search the room for loot", "Drink your flasks", "Attack the enemny", "Change your equipment", "See your statistics", "Find out more about your items", "Ends the game", "Change settings", "Meow"]
        self.teleportable = False
        
        out = []
        with open("settings.txt", "r") as f:
            out = f.readlines()
            out = [x.split()[1] for x in out]
        self.sleep = int(out[0])
    
    def intro(self) -> None:
        """print introduction for the start of the game """
        
        # Displays the introduction messages
        print('Welcome to Hogwarts School of Witchcraft and Wizardry')
        time.sleep(self.sleep)
        print("\nThe Dark Lord Voldemort has taken over Hogwarts and opened multiple interdimensional gates, bringing hordes of enemies into the school. Your job as the chosen one is to traverse the school in order to locate The Shrieking Shack and thwart Voldemort's evil plan to take over the world.\n")
        time.sleep(self.sleep)

        decision = input('Do you wish to enter the school? ( yes / no ): ')
        
        if decision.lower() == "yes":
            name = input('\nTarnished, key in your name: ')
            self.character.name = name
            # Check if the user used the secret easter egg name
            if name == "meow":
                self.secret()
            else:
                print("\nYou boldly opened the front gates of the school and made your way into the first room\n")
                time.sleep(self.sleep)
        elif decision.lower() == "no":
            print("\nDue to your utter cowardice, voldemort continued to gain power, spreading his control and chaos all over the world, leading to the complete annihilation of the human race.")
            self.end = True
            time.sleep(self.sleep)
            self.end_game()
            return
        else:
            print("\nDue to your indecision, voldemort continued to gain power, spreading his control and chaos all over the world, leading to the complete annihlation of the human race.")
            self.end = True
            time.sleep(self.sleep)
            self.end_game()
            return
        
    def run(self) -> None:
        """to be run in a loop to prompt user's action"""
        self.display_room_name()

        # Checks if the player has entered the room before
        if not self.room.been_here:
            # Displays a description of the room if the player has not been there before
            self.display_room_description()
            self.rooms.append(self.room)
        
        decision = self.get_action()

        # Does the action the user selected
        
        if decision.lower() == "help":
            self.help()

        elif decision.lower() == "look":
            self.look(self.room)
            
        elif decision.lower() == "move":
            self.move(self.room)
            
        elif decision.lower() == "attack":
            self.attack(self.character, self.room.enemy)

        elif decision.lower() == "loot":
            self.loot(self.character, self.room.loot)

        elif decision.lower() == "flask":
            self.flask(self.character)

        elif decision.lower() == "equip":
            self.equip(self.character)

        elif decision.lower() == "status":
            self.status(self.character)

        elif decision.lower() == "info":
            self.info(self.character)

        elif decision.lower() == "die":
            self.die()

        elif decision.lower() == "meow":
            self.meow()

        elif decision.lower() == "settings":
            self.settings()

        elif self.teleportable == True and decision.lower() == "teleport":
            self.teleport()
        
    def help(self) -> None:
        """main action for user to get the list of possible actions"""
        # Displays the list of actions the user can do
        print("\nYou are able to:")
        for i, action in enumerate(self.actions):
            print(f"- {action} ({self.description[i]})")
        time.sleep(self.sleep)
        
    def look(self, room : Room) -> None:
        """main action to look around the room including rooms linked to the room and enemies in the room"""
        print("\n", end="")

        # Displays the connected rooms
        if room.left != None:
            print(f"To the left is {room.left.name}")
            
        if room.right != None:
            print(f"To the right is {room.right.name}")
            
        if room.forward != None:
            print(f"In front of you is {room.forward.name}")
            
        if room.back != None:
            print(f"Behind you is {room.back.name}")

        time.sleep(self.sleep)
        upgrades = self.character.get_upgrades()

        if "Virtual Boo" in upgrades:
            if room.enemy != None:
                print(f"\nIn the middle of the room is {room.enemy.name}, {room.enemy.description}")
                time.sleep(self.sleep)
                print(f"\n{room.enemy.name} has {room.enemy.health} health")
                time.sleep(self.sleep)
            if room.loot != None:
                print(f"\nThere is {room.loot.name} hidden in {room.name}")
                time.sleep(self.sleep)
            else:
                print(f"\nThere is no loot hidden in {room.name}")
                time.sleep(self.sleep)
            
        elif room.enemy != None:
        # Displays the enemy in the room
            print(f"\nIn the middle of the room is {room.enemy.name}, {room.enemy.description}")

        time.sleep(self.sleep)

    def move(self, room : Room) -> None:
        """main action for user to traverse from one room to another"""
        movement = input('\nWhich direction do you wish to move in? (left, right, forward, back): ')

        # Validates the users choice
        if movement.lower() not in ["left", "right", "forward", "back"]:
            print(f"\nYou do not know what direction {movement} is and got confused")
            time.sleep(self.sleep)

        # Generate a random number to see if you managed to sneak past the enemy
        caught = False

        if self.character.name == "meow":
            chance = 2
        else:
            chance = random.randint(1, 3)
            
        if room.enemy != None:
            if chance == 1:
                caught = True
            else:
                print(f"\nYou managed to sneak past {room.enemy.name}")
                time.sleep(self.sleep)

        if not caught:
            if movement.lower() == "left":
                if room.left == None:
                    print("\nYou walked to the left and smashed into a wall")
                    time.sleep(self.sleep)
    
                else:
                    self.room = room.left
    
            if movement.lower() == "right":
                if room.right == None:
                    print("\nYou walked to the right and smashed into a wall")
                    time.sleep(self.sleep)
                else:
                    self.room = room.right
    
            if movement.lower() == "forward":
                if room.forward == None:
                    print("\nYou walked forward and smashed into a wall")
                    time.sleep(self.sleep)
                # Check if you are going to the final boss room
                elif room.forward.name == "The Shrieking Shack":
                    items = self.character.get_items()
                    # Checks if you have the required items to enter the final boss room
                    if "Dectus Medallion (right)" in items and "Dectus Medallion (left)" in items:
                        print("\nCongratulations, you placed the two Dectus Medallions together releasing trememndous amounts of energy, breaking the powerful spell on the door")
                        time.sleep(self.sleep)
                        self.room = room.forward
                    else:
                        print("\nYou tried entering the The Shrieking Shack but the door was locked by a powerful spell")
                        time.sleep(self.sleep)
                        print("\nYou probably need to find a special item to break the spell (remember to loot all the rooms)")
                        time.sleep(self.sleep)
                else:
                    self.room = room.forward
    
            if movement.lower() == "back":
                if room.back == None:
                    print("\nYou turned back and smashed into a wall")
                    time.sleep(self.sleep)
                else:
                    self.room = room.back

        else:
            print(f"\nYou tried to sneak to another room but {room.enemy.name} noticed you")
            time.sleep(self.sleep)
            self.attack(self.character, room.enemy)

    def loot(self, user : Character, loot : Item) -> None:
        """main action for user to search the room for loot"""

        # Generate a random number to see if you successfully loot the room whithout the enemy noticing
        caught = False

        if self.user.name == "meow":
            chance = 1
        else:
            chance = random.randint(1, 3)

        if self.room.enemy != None:
            if chance != 1:
                caught = True
            else:
                print(f"\nBy some miracle you managed to loot the room without {self.room.enemy.name} noticing")
                
                time.sleep(self.sleep)

        if not caught:
            # Allow the user to loot the room
            if loot == None:
                print("\nYou searched every nook and cranny but there was nothing to be found")
                time.sleep(self.sleep)
            
            elif loot.name == "Flask of Crimson Tears":
                print(f"\nYou found a {loot.name}, a powerful flask")
                time.sleep(self.sleep)
                user.health_flask += 1
                self.room.loot = None
    
            elif loot.name == "Flask of Cerulean Tears":
                print(f"\nYou found a {loot.name}, a powerful flask")
                time.sleep(self.sleep)
                user.mana_flask += 1
                self.room.loot = None
                
            elif loot.name == "Dectus Medallion (right)":
                print(f"\nYou found a {loot.name}, a powerful item")
                time.sleep(self.sleep)
                user.items.append(loot)
                self.room.loot = None
    
            elif loot.name == "Dectus Medallion (left)":
                print(f"\nYou found a {loot.name}, a powerful item")
                time.sleep(self.sleep)
                user.items.append(loot)
                self.room.loot = None

        else:
            print(f"\n{self.room.enemy.name} noticed you while you tried to loot the room")
            time.sleep(self.sleep)
            self.attack(user, self.room.enemy)

    def flask(self, user : Character) -> None:
        """main action for user to drink their flasks"""
        # Check if the user still has available flasks
        if (user.health_flask + user.mana_flask) == 0:
            print("\nYou ran out of flasks\n")
            time.sleep(self.sleep)
        else:
            self.use_flask(user)

    def attack(self, attacker : Character , victim: Enemy) -> None:
        """main action for user to attack the enemy in the room"""
        # Check if there is an enemy in the room
        if victim == None:
            print("\nYou attacked the air and realised how insane you looked")
            time.sleep(self.sleep)
        else:
            while attacker.health > 0:
                # Display users health and mana
                print(f"\n{'-'*50}\n")
                print(f"{attacker.name} has {attacker.health} health")
                print(f"{attacker.name} has {attacker.mana} mana")
                print(f"{attacker.name} has {attacker.health_flask} Flask of Crimson Tears")
                print(f"{attacker.name} has {attacker.mana_flask} Flask of Cerulean Tears")
                time.sleep(self.sleep)
                # Display enemy's health
                print(f"\n{victim.name} has {victim.health} health\n")
                time.sleep(self.sleep)

                decision = self.get_choice(attacker)
                
                if decision == "flask":
                    self.use_flask_battle(attacker)
                    if victim.health > 0:
                        damage = max(1, victim.attack - attacker.defence)
                        attacker.health = attacker.health - damage
                        print(f"\n{victim.name} used {victim.move}, dealing {damage} damage to {attacker.name}")
                        time.sleep(self.sleep)
                    
                else:
                    damage, weapon = self.get_attack(attacker, decision)

                    # Deal damage to enemy
                    damage += attacker.attack
                    victim.health = victim.health - damage
                    # Check if enemy died
                    if victim.health > 0:
                        print(f"\n{attacker.name}{weapon.move}, dealing {damage} damage to {victim.name}")
                        time.sleep(self.sleep)
                    # Allow enemy to attack if it didn't die yet
                    if victim.health > 0:
                        damage = max(1, victim.attack - attacker.defence)
                        attacker.health = attacker.health - damage
                        print(f"\n{victim.name} used {victim.move}, dealing {damage} damage to {attacker.name}")
                        time.sleep(self.sleep)
    
                    else:
                        # Check if dead enemy is the final boss
                        if victim.name == "Voldemort":
                            self.win(weapon)
                            return
                        print(f"\n{attacker.name}{weapon.win_front}{victim.name}{weapon.win_back}")
                        time.sleep(self.sleep)
                        if victim.name == "Sentinels":
                            self.secret_room()
                            self.room.enemy = None
                            return
                        print(f"\n{victim.name} dropped a {victim.loot.name}")
                        time.sleep(self.sleep)
                        choice = input(f"\nDo you want to pick {victim.loot.name}? ( yes / no ): ")
                        if choice.lower() == "yes":
                            self.collect_loot(attacker, victim.loot)
                            time.sleep(self.sleep)
                            print(f"\n{victim.loot.description}\n")
                            time.sleep(self.sleep)

                        elif choice.lower() == "no":
                            print(f"\nYou left {victim.loot.name} on the ground and allowed the resourceful rat to steal it")
                            time.sleep(self.sleep)
                        else:
                            print(f"\nYour indecisiveness allowed the resourceful rat to steal the {victim.loot.name} when you weren't looking")
                            time.sleep(self.sleep)
                        # Removes the enemy from the room
                        self.room.enemy = None
                        break
            # Check if the user died
            if attacker.health <= 0:
                self.end_game()

    def get_choice(self, user : Character) -> str:
        """sub action from attack() to prompt user for attack methods or use of flask"""
        decision = input(f"What do you want to use? ({user.weapon.name} / Spell / Flask): ")

        # Get a list of spell cost
        cost = []
        for spell in user.spells:
            cost.append(spell.cost)

        valid = False
        while not valid:
            valid = True
            if decision.lower() not in [user.weapon.name.lower(), "spell", "flask"]:
                print(f"\nYou tried to use {decision} but nothing happened")
                time.sleep(self.sleep)
                decision = input(f"\nWhat do you want to use? ({user.weapon.name} / Spell / Flask): ")
                valid = False
            # Check if user has enough mana to cast spells
            elif decision.lower() == "spell" and user.mana < min(cost):
                print("\nYou do not have enough mana to cast spells\n")
                time.sleep(self.sleep)
                decision = input(f"What do you want to use? ({user.weapon.name} / Spell / Flask): ")
                valid = False
            # Check if user has any flask to drink
            elif decision.lower() == "flask" and (user.health_flask + user.mana_flask) == 0:
                print("\nYou ran out of flasks\n")
                time.sleep(self.sleep)
                decision = input(f"What do you want to use? ({user.weapon.name} / Spell / Flask): ")    
                valid = False

        return decision
    
    def get_attack(self, user : Character, decision : str) -> [int, Weapon]:
        """sub action from attack() to get total damage done to victim"""

        # Check if user used his weapon
        if decision.lower() == user.weapon.name.lower():
            return user.weapon.attack, user.weapon

        # check if user used spells
        elif decision.lower() == "spell":
            self.display_spells(user)
            time.sleep(self.sleep)
            spells = user.get_spells()
            choice = input("\nWhich spell would you like to cast?: ")
            while choice.lower() not in spells:
                print(f"\nYou tried to cast {choice} but it blew up in your face")
                time.sleep(self.sleep)
                choice = input("\nWhich spell would you like to cast?: ")
            choice = choice.lower()
            cost = user.spells[spells.index(choice)].cost
            print(f"\nYou used up {cost} mana points")
            time.sleep(self.sleep)
            user.mana = user.mana - cost
            return user.spells[spells.index(choice)].attack, user.spells[spells.index(choice)]

    def use_flask_battle(self, user : Character) -> None:
        """sub action from get_choice() to prompt user for the flask to drink"""
        self.display_flask(user)
        selection = input("Which flask would you like to drink?: ")
        valid = False
        while not valid:
            valid = True
            # Validates user selection
            if selection.lower() not in ["flask of crimson tears", "flask of cerulean tears"]:
                print(f"\nYou tried drinking {selection} but nothing happened\n")
                time.sleep(self.sleep)
                selection = input("Which flask would you like to drink?: ")
                valid = False
            # Checks if the user has enough flask of crimson tears
            elif selection.lower() == "flask of crimson tears" and user.health_flask == 0:
                print("\nYou ran out of Flask of Crimson Tears\n")
                time.sleep(self.sleep)
                selection = input("Which flask would you like to drink?: ")
                valid = False
            # Checks if the user has enough flask of cerulean tears
            elif selection.lower() == "flask of cerulean tears" and user.mana_flask == 0:
                print("\nYou ran out of Flask of Cerulean Tears\n")
                time.sleep(self.sleep)
                selection = input("Which flask would you like to drink?: ")
                valid = False

        if selection.lower() == "flask of crimson tears":
            # Makes sure the health healed does not exceed the maximum health
            final_health = min(user.max_health, user.health + FlaskOfCrimsonTears().health)
            healing = final_health - user.health
            print(f"\nYou drank a Flask of Crimson Tears and gained {healing} health")
            time.sleep(self.sleep)
            user.health = final_health
            user.health_flask -= 1
            
        elif selection.lower() == "flask of cerulean tears":
            # Makes sure the mana gained does not exceed the maximum mana
            final_mana = min(user.max_mana, user.mana + FlaskOfCeruleanTears().mana)
            healing = final_mana - user.mana
            print(f"\nYou drank a Flask of Cerulean Tears and gained {healing} mana")
            time.sleep(self.sleep)
            user.mana = final_mana
            user.mana_flask -= 1
                
    def use_flask(self, user : Character) -> None:
        """Function to allow the user to use flask but also allows them to cancel the action"""
        self.display_flask(user)
        selection = input("Which flask would you like to drink? (type cancel to quit): ")
        valid = False
        while not valid:
            valid = True
            # Validates user selection
            if selection.lower() not in ["flask of crimson tears", "flask of cerulean tears", "cancel"]:
                print(f"\nYou tried drinking {selection} but nothing happened\n")
                time.sleep(self.sleep)
                selection = input("Which flask would you like to drink?: ")
                valid = False
            # Checks if the user has enough flask of crimson tears
            elif selection.lower() == "flask of crimson tears" and user.health_flask == 0:
                print("\nYou ran out of Flask of Crimson Tears\n")
                time.sleep(self.sleep)
                selection = input("Which flask would you like to drink?: ")
                valid = False
            # Checks if the user has enough flask of cerulean tears
            elif selection.lower() == "flask of cerulean tears" and user.mana_flask == 0:
                print("\nYou ran out of Flask of Cerulean Tears\n")
                time.sleep(self.sleep)
                selection = input("Which flask would you like to drink?: ")
                valid = False

            elif selection.lower() == "cancel":
                return

        if selection.lower() == "flask of crimson tears":
            # Makes sure the health healed does not exceed the maximum health
            final_health = min(user.max_health, user.health + FlaskOfCrimsonTears().health)
            healing = final_health - user.health
            print(f"\nYou drank a Flask of Crimson Tears and gained {healing} health")
            time.sleep(self.sleep)
            user.health = final_health
            user.health_flask -= 1
            
        elif selection.lower() == "flask of cerulean tears":
            # Makes sure the mana gained does not exceed the maximum mana
            final_mana = min(user.max_mana, user.mana + FlaskOfCeruleanTears().mana)
            healing = final_mana - user.mana
            print(f"\nYou drank a Flask of Cerulean Tears and gained {healing} mana")
            time.sleep(self.sleep)
            user.mana = final_mana
            user.mana_flask -= 1
    
    def display_flask(self, user : Character) -> None:
        """sub action from use_flask to display flask in inventory"""
        print(f"\nNumber of Flask of Crimson Tears in inventory : {user.health_flask} (restores {FlaskOfCrimsonTears().health} health)")
        print(f"Number of Flask of Cerulean Tears in inventory: {user.mana_flask} (restores {FlaskOfCeruleanTears().mana} mana)\n")
        time.sleep(self.sleep)
        
    def equip(self, user) -> None:
        """main action for user to equip various items"""

        self.display_equipment(user)

        decision = input("\ndo you want to change your equipment? ( yes / no ): ")

        while decision.lower() not in ["yes", "no"]:
            print("You briefly ponder the heavily nuanced and deeply intricate question of a choice between yes and no.")
            time.sleep(self.sleep)
            decision = input("\ndo you want to change your equipment? ( yes / no ): ")

        if decision.lower() == "no":
            return

        elif decision.lower() == "yes":
            choice = ""
            while choice != "finish":
                choice = input("\nwhat do you want to change? (type finish to quit): ")
                while choice.lower() not in ["armour", "weapon", "accessory", "finish"]:
                    print(f"\nYou tried changing your {choice} but nothing happened")
                    choice = input("\nwhat do you want to change? (type finish to quit): ")
    
                if choice.lower() == "armour":
                    self.equip_armour(user)

                elif choice.lower() == "weapon":
                    self.equip_weapon(user)

                elif choice.lower() == "accessory":
                    self.equip_accessory(user)
    
    def display_equipment(self, user : Character) -> None:
        """sub action for equip() to display equipments that the user have"""
        
        if user.armour == None:
            print("\nArmour : Empty")
        else:
            print(f"\nArmour : {user.armour.name}")

        if user.weapon == None:
            print("Weapon : Empty")
        else:
            print(f"Weapon : {user.weapon.name}")

        if user.accessory == None:
            print("Accessory : Empty")
        else:
            print(f"Accessory : {user.accessory.name}")
        time.sleep(self.sleep)

    def display_spells(self, user : Character) -> None:
        """sub action from attack to display spells that the user have"""
        # Displays all spells owned
        print("\nSpells:")
        for i, spell in enumerate(user.spells):
            print(f"- {spell.name} ({spell.cost} mana)")

    def equip_armour(self, user : Character) -> None:
        """sub action from equip() for user to choose an armour to equip"""
        if len(user.armours) == 0:
            print("\nYou do not have any armour to equip")
            time.sleep(self.sleep)
        else:
            # Displays the armours the user owns
            print("\nIn your inventory you have: ")
            armours = user.get_armours()
            for armour in armours:
                print(f"- {armour.name}")
            time.sleep(self.sleep)
            option = input("\nWhich armour do you want to equip?: ")
            # Validates the users choice
            if option.lower() not in armours:
                print(f"\nYou tried equipping {option} but realised you cant create things out of thin air")
                time.sleep(self.sleep)
            else:
                print(f"\nYou equipped {option}")
                time.sleep(self.sleep)
                # Removes the defence increase of the previous armour
                if user.armour != None:
                    user.defence = user.defence - user.armour.defence
                armour = user.armours[items.index(option.lower())]
                # Adds the defence of the new armour
                user.defence = user.defence + armour.defence
                user.armour = armour
                self.display_equipment(user)

    def equip_weapon(self, user : Character) -> None:
        """sub action from equip() for user to choose a weapon to equip"""
        if len(user.weapons) == 0:
            print("\nYou do not have any weapon to equip")
            time.sleep(self.sleep)
        else:
            # Displays the weapons the user owns
            print("\nIn your inventory you have: ")
            weapons = user.get_weapons()
            for weapon in weapons:
                print(f"- {weapon.name}")
            time.sleep(self.sleep)
            # Validates the user's choice
            option = input("\nWhich weapon do you want to equip?: ")
            if option.lower() not in weapons:
                print(f"\nYou tried equipping {option} but realised you cant create things out of thin air")
            else:
                print(f"\nYou equipped {option}")
                time.sleep(self.sleep)
                user.weapon = user.weapons[items.index(option.lower())]
                self.display_equipment(user)

    def equip_accessory(self, user : Character) -> None:
        """sub action from equip() for user to choose an accessory to equip"""
        if len(user.accessories) == 0:
            print("\nYou do not have any accessories to equip")
            time.sleep(self.sleep)
        else:
            print("\nIn your inventory you have: ")
            accessories = user.get_accessories()
            for accessory in accessories:
                print(f"- {accessory.name}")
            time.sleep(self.sleep)
            option = input("\nWhich accessory do you want to equip?: ")
            if option.lower() not in accessories:
                print(f"\nYou tried equipping {option} but realised you cant create things out of thin air")
            else:
                print(f"\nYou equipped {option}")
                time.sleep(self.sleep)

                # Removes the stat boost from the previous accessory
                if user.accessory != None:
                    user.max_health = user.max_health - user.accessory.health_boost

                    new_health = min(max(1, user.health - user.accessory.health_boost), user.max_health)
                    user.health = new_health
                    
                    user.max_mana -= user.accessory.mana_boost

                    new_mana = min(max(0, user.mana - user.accessory.mana_boost), user.max_mana)
                    user.mana = new_mana

                    user.attack -= user.accessory.attack_boost

                    user.defence -= user.accessory.defence_boost

                # Adds the stat boost from the new accessory
                accessory = user.accessories[items.index(option.lower())]
                user.health += accessory.health_boost
                user.max_health += accessory.health_boost
                user.attack += accessory.attack_boost
                user.mana += accessory.mana_boost
                user.max_mana += accessory.mana_boost
                user.defence += user.accessory.defence_boost
                
                user.accessory = accessory
                self.display_equipment(user)

    def status(self, user : Character) -> None:
        """main action that prints user's status"""
        # Displays the users statistics
        print(f"\nName: {user.name}")
        print(f"Health: {user.health} / {user.max_health}")
        print(f"Mana: {user.mana} / {user.max_mana}")
        print(f"Defence: {user.defence}")
        print(f"Strength: {user.attack}")
        time.sleep(self.sleep)

    def info(self, user : Character) -> None:
        """main action that prompts user for the type of item to find out more information about"""
        choice = input("\nWhat do you want to find out more about? (weapons, spells, armours, accessories, flasks, items): ")
        
        if choice.lower() not in ["weapons", "spells", "armours", "accessories", "flasks", "items"]:
            print(f"\nYou do not own any {choice}")

        elif choice == "weapons":
            self.weapon_info(user)

        elif choice == "spells":
            self.spell_info(user)

        elif choice == "armours":
            self.armour_info(user)

        elif choice == "accessories":
            self.accessory_info(user)

        elif choice == "flasks":
            self.flask_info()

        elif choice == "items":
            self.item_info(user)
                
    def weapon_info(self, user : Character) -> None:
        """sub action from equip() that prompts user for specific weapon to find out more about"""
        # Check if the user owns any weapons
        if len(user.weapons) == 0:
            print("\nYou do not own any weapons yet")

        else:
            # Displays the weapons the user owns
            weapons = user.get_weapons()
            print("\nIn your inventory you have: ")
            for weapon in weapons:
                print(f"- {weapon.name}")
            time.sleep(self.sleep)

            decision = input("\nWhich weapon do you want to find out more about? : ")
            if decision.lower() not in weapons:
                print(f"You do not own {decision}")

            else:
                # Displays the description of the weapon
                print("\n", end="")
                print(user.weapons[weapons.index(decision)].description)
                time.sleep(self.sleep)

    def spell_info(self, user : Character) -> None:
        """sub action from equip() that prompts user for specific spell to find out more about"""
        # Check if the user knows any spells
        if len(user.spells) == 0:
            print("\nYou do not own any spells yet")

        else:
            # Displays the spells the user knows
            spells = user.get_spells()
            print("\nIn your inventory you have: ")
            for spell in spells:
                print(f"- {spell.name}")
            time.sleep(self.sleep)

            decision = input("\nWhich spell do you want to find out more about? : ")
            if decision.lower() not in spells:
                print(f"You do not own {decision}")

            else:
                # Displays the description of the spell
                print("\n", end="")
                print(user.spells[spells.index(decision)].description)
                time.sleep(self.sleep)

    def armour_info(self, user : Character) -> None:
        """sub action from equip() that prompts user for specific armour to find out more about"""
        # Check if the user owns any armours
        if len(user.armours) == 0:
            print("\nYou do not own any amours yet")

        else:
            # Displays the armours the user owns
            armours = user.get_armours()
            print("\nIn your inventory you have: ")
            for armour in armours:
                print(f"- {armour.name}")
            time.sleep(self.sleep)

            decision = input("\nWhich armour do you want to find out more about? : ")
            if decision.lower() not in armours:
                print(f"You do not own {decision}")

            else:
                # Displays the description of the armour
                print("\n", end="")
                print(user.armours[armours.index(decision)].description)
                time.sleep(self.sleep)

    def accessory_info(self, user : Character) -> None:
        """sub action from equip() that prompts user for specific accessory to find out more about"""
        # Checks if the user owns any accessories
        if len(user.accessories) == 0:
            print("\nYou do not own any accessories yet")

        else:
            # Displays the accessories the user owns
            accessories = user.get_accessories()
            print("\nIn your inventory you have: ")
            for accessory in accessories:
                print(f"- {accessory.name}")
            time.sleep(self.sleep)

            decision = input("\nWhich accesssory do you want to find out more about? : ")
            if decision.lower() not in accessories:
                print(f"You do not own {decision}")

            else:
                # Displays the description of the accessory
                print("\n", end="")
                print(user.accessories[accessories.index(decision)].description)
                time.sleep(self.sleep)

    def flask_info(self) -> None:
        """sub action from equip() that prompts user for specific flask to find out more about"""
        print("\nIn your inventory you have: ")
        print("- Flask of Crimson Tears")
        print("- Flask of Cerulean Tears")

        decision = input("\nWhich accesssory do you want to find out more about? : ")
        if decision.lower() == "flask of crimson tears":
            print("\n", end ="")
            print(FlaskOfCrimsonTears().description)
            time.sleep(self.sleep)
        elif decision.lower() == "flask of cerulean tears":
            print("\n", end ="")
            print(FlaskOfCeruleanTears().description)
            time.sleep(self.sleep)
        else:
            print(f"You do not own {decision}")

    def item_info(self, user : Character) -> None:
        """sub action from equip() that prompts user for specific special item to find out more about"""
        # Check if the user owns any items
        if len(user.items) == 0:
            print("\nYou do not own any items yet")
        else:
            # Displays the items the user owns
            items = user.get_items()
            print("\nIn your inventory you have: ")
            for item in items:
                print(f"- {item}")
            time.sleep(self.sleep)
    
            decision = input("\nWhich item do you want to find out more about? : ")
            if decision.lower() not in items:
                print(f"You do not own {decision}")
    
            else:
                # Displays the description of the items
                print()
                print(user.items[items.index(decision)].description)
                time.sleep(self.sleep)
                
    def display_room_name(self) -> None:
        """prints the room's name in a cool way"""
        print("="*25)
        space = " "*int((25-len(self.room.name))/2)
        print(f"{space}{self.room.name}{space}")
        print("="*25)
        time.sleep(self.sleep)

    def display_room_description(self) -> None:
        """prints the room's description"""
        print()
        print(self.room.description)
        time.sleep(self.sleep)
        self.look(self.room)
        self.room.been_here = True

    def get_action(self) -> str:
        """sub action for run() that prompts user for a main action"""
        decision = input("\nWhat do you wish to do? (type help for list of actions): ")

        # Validate the users decision
        while decision.lower() not in self.actions:
            print(f"\nYou do not have the physical and mental capability to {decision}")
            time.sleep(self.sleep)
            decision = input("\nWhat do you wish to do? (type help for list of actions): ")

        return decision

    def collect_loot(self, attacker : Character, loot : Item) -> None:
        """sub method from attack() to collect loot of defeated monster"""
        if loot.type == "weapon":
            attacker.weapons.append(loot)
            print(f"\nYou obtained a {loot.name}, a powerful weapon")
            
        elif loot.type == "spell":
            attacker.spells.append(loot)
            print(f"\nYou obtained a {loot.name}, a powerful spell")

        elif loot.type == "armour":
            attacker.armours.append(loot)
            print(f"\nYou obtained a {loot.name}, a powerful armour")

        elif loot.type == "accessory":
            attacker.accessories.append(loot)
            print(f"\nYou obtained a {loot.name}, a powerful accessory")

        elif loot.type == "upgrade":
            attacker.upgrades.append(loot)
            print(f"\nYou obtained a {loot.name}, a powerful upgrade")
            if loot.name == "Portal Gun":
                self.teleportable = True
                self.actions.append("teleport")
                self.description.append("Teleport to any room you have been to before")

        time.sleep(self.sleep)

    def end_game(self) -> None:
        """displays scenario when user dies"""
        print("__   _______ _   _  ______ _____ ___________")
        print("\ \ / /  _  | | | | |  _  \_   _|  ___|  _  \\")
        print(" \ V /| | | | | | | | | | | | | | |__ | | | |")
        print("  \ / | | | | | | | | | | | | | |  __|| | | |")
        print("  | | \ \_/ / |_| | | |/ / _| |_| |___| |/ /")
        print("  \_/  \___/ \___/  |___/  \___/\____/|___/ ")
        self.end = True

    def win(self, weapon) -> None:
        """displays scenario when user wins"""
        print(f"\nUsing the almighty {weapon.name}, you struck the Dark Lord Voldemort down, crippling him of all his powers and stopping his evil tyranny over the school")
        time.sleep(self.sleep)
        print(" _____ ___________   _____ _       ___  _____ _   _ ")
        print("|  __ \  _  |  _  \ /  ___| |     / _ \|_   _| \ | |")
        print("| |  \/ | | | | | | \ `--.| |    / /_\ \ | | |  \| |")
        print("| | __| | | | | | |  `--. \ |    |  _  | | | | . ` |")
        print("| |_\ \ \_/ / |/ /  /\__/ / |____| | | |_| |_| |\  |")
        print(" \____/\___/|___/   \____/\_____/\_| |_/\___/\_| \_/")
        self.end = True

    def die(self) -> None:
        """to end the game"""
        self.end_game()
        self.end = True
           
    def secret(self) -> None:
        """secret account that gives God like stats by setting name as meow"""
        print("\nWelcome chosen one, the Gods smile upon you and have rained down their blessing\n")
        time.sleep(self.sleep)
        self.character.health = 999
        self.character.max_health = 999
        self.character.mana = 999
        self.character.max_mana = 999
        self.character.attack = 999
        self.character.defence = 999
        self.character.health_flask = 999
        self.character.mana_flask = 999

    def meow(self) -> None:
        if self.room.secret == True:
            print("""       
                
       ____ ___  ___  ____ _      __
      / __ `__ \/ _ \/ __ \ | /| / /
     / / / / / /  __/ /_/ / |/ |/ / 
    /_/ /_/ /_/\___/\____/|__/|__/  
                                   """)
            time.sleep(self.sleep)
            print("\nYou started communicating with the cat, leading you to discover a hidden passage\n")
            time.sleep(self.sleep)
            self.room.link_left(TheLastResort())
        else:
            choice = random.randint(1, 9)
            if choice == 1:
                print("""  
                
      __  __  U _____ u U  ___ u             
    U|' \/ '|u\| ___"|/  \/"_ \/__        __ 
    \| |\/| |/ |  _|"    | | | |\"\      /"/ 
     | |  | |  | |___.-,_| |_| |/\ \ /\ / /\ 
     |_|  |_|  |_____|\_)-\___/U  \ V  V /  U
    <<,-,,-.   <<   >>     \\  .-,_\ /\ /_,-.
     (./  \.) (__) (__)   (__)  \_)-'  '-(_/ 
                                            """)
            elif choice == 2:
                print("""       
                
       ____ ___  ___  ____ _      __
      / __ `__ \/ _ \/ __ \ | /| / /
     / / / / / /  __/ /_/ / |/ |/ / 
    /_/ /_/ /_/\___/\____/|__/|__/  
                                   """)
    
            elif choice == 3:
                print("""                              
                                  
     _ __ ___   ___  _____      __
    | '_ ` _ \ / _ \/ _ \ \ /\ / /
    | | | | | |  __/ (_) \ V  V / 
    |_| |_| |_|\___|\___/ \_/\_/  
                                  """)
    
            elif choice == 4:
                print(""" 
                
     _  _  ____  __   _  _ 
    ( \/ )(  __)/  \ / )( \
    / \/ \ ) _)(  O )\ /\ /
    \_)(_/(____)\__/ (_/\_)
                            """)
    
            elif choice == 5:
                print("""   
                
     _ __ ___   ___  _____      __
    | '_ ` _ \ / _ \/ _ \ \ /\ / /
    | | | | | |  __/ (_) \ V  V / 
    |_| |_| |_|\___|\___/ \_/\_/  
                                  """)
    
            elif choice == 6:
                print("""                                    
                                        
    ,--,--,--. ,---.  ,---. ,--.   ,--. 
    |        || .-. :| .-. ||  |.'.|  | 
    |  |  |  |\   --.' '-' '|   .'.   | 
    `--`--`--' `----' `---' '--'   '--' 
                                        """)
    
            elif choice == 7:
                print(""" 
     __    __     ______     ______     __     __    
    /\ "-./  \   /\  ___\   /\  __ \   /\ \  _ \ \   
    \ \ \-./\ \  \ \  __\   \ \ \/\ \  \ \ \/ ".\ \  
     \ \_\ \ \_\  \ \_____\  \ \_____\  \ \__/".~\_\ 
      \/_/  \/_/   \/_____/   \/_____/   \/_/   \/_/ 
                                                     """)
    
            elif choice == 8:
                print("""                                        
                                            
     _ .--..--.  .---.   .--.   _   _   __  
    [ `.-. .-. |/ /__\\/ .'`\ \[ \ [ \ [  ] 
     | | | | | || \__.,| \__. | \ \/\ \/ /  
    [___||__||__]'.__.' '.__.'   \__/\__/   
                                            """)
    
            elif choice == 9:
                print(""" 
     _      _____ ____  _     
    / \__/|/  __//  _ \/ \  /|
    | |\/|||  \  | / \|| |  ||
    | |  |||  /_ | \_/|| |/\||
    \_/  \|\____\\____/\_/  \|
                              """)
          
    def settings(self) -> None:
        """Show and change settings"""
        settings = []
        with open("settings.txt", "r") as f:
            settings = f.readlines()
            settings_dict = {}
            for row in settings:
                key, val = row.split()
                settings_dict[key] = val

        self.display_settings(settings_dict)
        
        change = input("\nDo you want to change your settings? ( yes / no ): ").lower()

        while change not in ["yes", "no"]:
            print("You briefly ponder the heavily nuanced and deeply intricate question of a choice between yes and no.")
            time.sleep(self.sleep)
            change = input("\nDo you want to change your settings? ( yes / no ): ").lower()
        
        if change == "yes":
        
            choice = ""
            accepted = list(settings_dict.keys())
            accepted.append("finish")
            while choice != "finish":
                choice = input("\nWhich setting do you want to change? (type finish to quit): ").lower()
                while choice not in accepted:
                    print(f"{choice} is a uniquely unmodifiable property of this realm.")
                    choice = input("\nWhich setting do you want to change? (type finish to quit): ").lower()

                if choice == "finish":
                    with open("settings.txt", "w") as f:
                        for entry in settings_dict:
                            f.write(entry + " " + settings_dict[entry] + "\n")
                    return
                
                if choice == "sleep":
                    new = self.set_sleep(settings_dict["sleep"])
                    settings_dict["sleep"] = new

                self.display_settings(settings_dict)
                
        elif change == "no":
            return

    def display_settings(self, settings: dict) -> None:
        """
        display the settings passed in
        """
        print("\nCurrent Settings:\n")
        for set in settings:
            print(f"{set}: {settings[set]}")

    def set_sleep(self, current: int) -> str:
        """
        Change the interval between messages
        returns new value for sleep as string
        """
        count = 0
        print("\nsleep: the interval between messages sent by the game in seconds.")
        print(f"Current value: {current}")
        
        accept = [str(x) for x in range(6)]
        accept.append("cancel")

        new = input("\nEnter a new value for sleep (0-5 seconds), or cancel to cancel: ")
        while new not in accept:
            print("You count up to five on your fingers. Slowly.")
            time.sleep(self.sleep)
            new = input("\nEnter a new value for sleep (0-5 seconds), or cancel to cancel: ")
        
        if new.lower() == "cancel":
            return current
        else:
            self.sleep = int(new)
            return new
                

    def secret_room(self):
        print("\nAfter you successfully defeated the sentinels, a stray ginger tabby cat emerges from behind a wall and stares at you playfully\n")
        self.room.secret = True
        time.sleep(self.sleep)

    def teleport(self):
        print("\nYou can teleport to: ")
        rooms = []
        for room in self.rooms:
            print(f"- {room.name}")
            rooms.append(room.name.lower())
        time.sleep(self.sleep)

        choice = input("\nWhich room do you want to teleport to?: ")
        
        if choice.lower() not in rooms:
            print(f"\nYou tried teleporting to {choice} but ended up in a dark abyss\n")
            time.sleep(self.sleep)

        else:
            self.room = self.rooms[rooms.index(choice.lower())]
            