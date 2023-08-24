from setup import *
import time

class Game:
    '''
    a class that runs when the game runs

    attributes
    ----------
    end : True when game ends, False otherwise
    room : class for monster in the room and rooms it is connected to (refer to map.py)
    character : class for the character (refer to character.py)

    methods
    -------
    intro() : runs when the game starts for the first time
    run() : runs everytime the character choose an option
    move() : method for character to traverse to different rooms
    attack() : method for character to attack enemy and vise versa
    while_fighting() : runs when character is in a fight, disabling move option
    use_item(): method for character to use item
    '''
    def __init__(self):
        temp = setup()
        self.end = False
        self.room = temp[0]
        self.character = temp[1]
        self.actions = ["help", "look", "move", "attack", "equip", "info"]
        self.description = ["Gets the list of possible actions", "Looks around the room", "Move to another room", "Attack the enemny", "Change your equipment", "Find out more about your items"]
    
    def intro(self):
        # start of the game
        print('Welcome to Hogwarts School of Witchcraft and Wizardry')
        time.sleep(1)
        print("\nThe Dark Lord Voldermort has taken over Hogwarts School and opened multiple interdimensional gates, bringing hoards of enemies into the school. Your job as the chosen one is to traverse the school in order to locate the Principal's Office and thwart Voldermort's evil plan to take over the world\n")
        time.sleep(2)
        decision = input('Do you wish to enter the school? ( yes / no ): ')
        
        if decision.lower() == "yes":
            self.character.set_name(input('\nTarnished, key in your name: '))
            print("\nYou boldly opened the front gates of the school and made your way into the first room")
            time.sleep(1)
        elif decision.lower() == "no":
            print("\nDue to your utter cowardice, voldermort continued gaining power, spreading his control and chaos all over the world, leading to the complete annihlation of the human race")
            self.end = True
            time.sleep(1)
            self.end_game()
            return
        else:
            print("\nDue to your indecision, voldermort continued gaining power, spreading his control and chaos all over the world, leading to the complete annihlation of the human race")
            self.end = True
            time.sleep(1)
            self.end_game()
            return
        
    def run(self):
        self.display_room_name()

        # Checks if the player has entered the room before
        if not self.room.get_been_here():
            # Displays a description of the room if the player has not been there before
            self.display_room_description()
        
        decision = self.get_action()
        
        if decision.lower() == "help":
            self.help()

        elif decision.lower() == "look":
            self.look()
            
        elif decision.lower() == "move":
            self.move()
            
        elif decision.lower() == "attack":
            self.attack(self.character, self.room.get_enemy())

        elif decision.lower() == "equip":
            self.equip(self.character)

        elif decision.lower() == "info":
            self.info(self.character)
        
    def help(self):
        print("You are able to:")
        for i, action in enumerate(self.actions):
            print(f"- {action} ({self.description[i]})")
        time.sleep(1)
        
    def look(self):
        print("\n", end="")
        
        if self.room.get_left() != None:
            print(f"To the left is {self.room.get_left().get_name()}")
            
        if self.room.get_right() != None:
            print(f"To the right is {self.room.get_right().get_name()}")
            
        if self.room.get_forward() != None:
            print(f"In front of you is {self.room.get_forward().get_name()}")
            
        if self.room.get_back() != None:
            print(f"Behind you is {self.room.get_back().get_name()}")

        time.sleep(1)
        if self.room.get_enemy() != None:
            print(f"\nIn the middle of the room is {self.room.get_enemy().get_name()}, {self.room.get_enemy().get_description()}")

        time.sleep(1)

    def move(self):
        movement = input('\nWhich direction do you wish to move in? (left, right, forward, back): ')
        
        if movement.lower() not in ["left", "right", "forward", "back"]:
            print(f"You do not know what direction {movement} is and got confused")

        if movement.lower() == "left":
            if self.room.get_left() == None:
                print("You walked to the left and smashed into a wall")

            else:
                self.room = self.room.get_left()

        if movement.lower() == "right":
            if self.room.get_right() == None:
                print("You walked to the right and smashed into a wall")
            else:
                self.room = self.room.get_right()

        if movement.lower() == "forward":
            if self.room.get_forward() == None:
                print("You walked forward and smashed into a wall")
            else:
                self.room = self.room.get_forward()

        if movement.lower() == "back":
            if self.room.get_back() == None:
                print("You turned back and smashed into a wall")
            else:
                self.room = self.room.get_back()
    
    def attack(self, attacker, victim):
        if victim == None:
            print("\nYou attacked the air and realised how insane you looked")
            time.sleep(1)
        else:
            while attacker.get_health() > 0:
                print(f"\n{'-'*50}\n")
                print(f"{attacker.get_name()} has {attacker.get_health()} health")
                print(f"{attacker.get_name()} has {attacker.get_mana()} mana")
                time.sleep(1)
                print(f"\n{victim.get_name()} has {victim.get_health()} health\n")
                time.sleep(1)

                damage, weapon = self.get_attack(self.character)
                
                victim.set_health(victim.get_health() - damage)
                if victim.get_health() > 0:
                    print(f"\n{attacker.get_name()}{weapon.get_move()}, dealing {damage} damage to {victim.get_name()}")
                    time.sleep(1)
                
                if victim.get_health() > 0:
                    attacker.set_health(attacker.get_health() - victim.get_attack())
                    print(f"\n{victim.get_name()} dealt {victim.get_attack()} damage to {attacker.get_name()}")
                    time.sleep(1)

                else:
                    if victim.get_name() == "Voldermort":
                        self.win(weapon)
                        return
                    print(f"\n{attacker.get_name()}{weapon.get_win_front()}{victim.get_name()}{weapon.get_win_back()}")
                    time.sleep(1)
                    print(f"\n{victim.get_name()} dropped a {victim.get_loot().get_name()}")
                    time.sleep(1)
                    choice = input(f"\nDo you want to pick {victim.get_loot().get_name()}? ( yes / no ): ")
                    if choice.lower() == "yes":
                        self.collect_loot(attacker, victim.get_loot())
                    else:
                        print(f"\nYour indecisiveness allowed the resourceful rat to steal the {victim.get_loot().get_name()} when you weren't looking")
                        time.sleep(1)
                    self.room.set_enemy(None)
                    break

            if attacker.get_health() < 0:
                self.end()

        return None

    def get_attack(self, user):
        
        decision = input(f"What do you want to use? ({user.get_weapon().get_name()} / Spell): ")

        cost = []
        for spell in user.get_spells():
            cost.append(spell.get_cost())
            
        while True:
            if decision.lower() not in [user.get_weapon().get_name().lower(), "spell"]:
                print(f"You tried to use {decision} but nothing happened")
                decision = input("What do you want to use? (weapon / spell): ")
            elif decision.lower() == "spell" and user.get_mana() < min(cost):
                print("You do not have enough mana to cast spells")
                decision = input("What do you want to use? (weapon / spell): ")
            else:
                break
        
        if decision.lower() == user.get_weapon().get_name().lower():
            return user.get_weapon().get_attack(), user.get_weapon()

        elif decision.lower() == "spell":
            self.display_spells(user)
            time.sleep(1)
            spells = []
            for spell in user.spells:
                spells.append(spell.get_name().lower())
            choice = input("\nWhich spell would you like to cast?: ")
            while choice.lower() not in spells:
                print(f"\nYou tried to cast {choice} but it blew up in your face")
                time.sleep(1)
                choice = input("\nWhich spell would you like to cast?: ")
            cost = user.get_spells()[spells.index(choice)].get_cost()
            print(f"\nYou used up {cost} mana points")
            time.sleep(1)
            user.set_mana(user.get_mana() - cost)
            return user.get_spells()[spells.index(choice)].get_attack(), user.get_spells()[spells.index(choice)]
            
    def equip(self, user):

        self.display_equipment(user)

        decision = input("\ndo you want to change your equipment? ( yes / no ): ")

        if decision.lower() == "no":
            return

        elif decision.lower() == "yes":
            choice = ""
            while choice != "finish":
                choice = input("\nwhat do you want to change? (type finish to quit): ")
                while choice.lower() not in ["armour", "weapon", "accessory", "finish"]:
                    print(f"\nYou tried changing your {choice} but nothing happened")
                    choice = input("\nwhat do you want to change?: ")
    
                if choice.lower() == "armour":
                    self.equip_armour(user)

                elif choice.lower() == "weapon":
                    self.equip_weapon(user)

                elif choice.lower() == "accessory":
                    self.equip_accessory(user)
    
    def display_equipment(self, user):
        
        if user.armour == None:
            print("Armour : Empty")
        else:
            print(f"Armour : {user.armour.get_name()}")

        if user.weapon == None:
            print("Weapon : Empty")
        else:
            print(f"Weapon : {user.weapon.get_name()}")

        if user.accessory == None:
            print("Accessory : Empty")
        else:
            print(f"Accessory : {user.accessory.get_name()}")
        time.sleep(1)

    def display_spells(self, user):
        print("\nYou can use:")
        for i, spell in enumerate(user.spells):
            print(f"- {spell.get_name()} ({spell.get_cost()} mana)")

    def equip_armour(self, user):
        if len(user.get_armours()) == 0:
            print("\nYou do not have any armour to equip")
        else:
            print("\nIn your inventory you have: ")
            items = []
            for armour in user.get_armours():
                items.append(armour.get_name().lower())
            for armour in items:
                print(f"- {armour}")
            time.sleep(1)
            option = input("\nWhich armour do you want to equip?: ")
            if option.lower() not in items:
                print(f"\nYou tried equipping {option} but realised you cant create things out of thin air")
                time.sleep(1)
            else:
                print(f"\nYou equipped {option}")
                time.sleep(1)
                armour = user.get_armours()[items.index(option.lower())]
                user.set_defence(armour.get_defence())
                user.set_armour(armour)

    def equip_weapon(self, user):
        if len(user.get_weapons()) == 0:
            print("\nYou do not have any weapon to equip")
        else:
            print("\nIn your inventory you have: ")
            items = []
            for weapon in user.get_weapons():
                items.append(weapon.get_name().lower())
            for weapon in items:
                print(f"- {weapon}")
            time.sleep(1)
            option = input("\nWhich weapon do you want to equip?: ")
            if option.lower() not in items:
                print(f"\nYou tried equipping {option} but realised you cant create things out of thin air")
            else:
                print(f"\nYou equipped {option}")
                user.get_weapon(user.get_weapons()[items.index(option.lower())])

    def equip_accessory(self, user):
        if len(user.accessories) == 0:
            print("\nYou do not have any accessories to equip")
        else:
            print("\nIn your inventory you have: ")
            items = []
            for accessory in user.get_accessories():
                items.append(accessory.get_name().lower())
            for accessory in items:
                print(f"- {accessory}")
            time.sleep(1)
            option = input("\nWhich accessory do you want to equip?: ")
            if option.lower() not in items:
                print(f"\nYou tried equipping {option} but realised you cant create things out of thin air")
            else:
                print(f"\nYou equipped {option}")
                accessory = user.get_accessories()[items.index(option.lower())]
                user.set_health(user.get_health() + accessory.get_health_boost())
                user.set_max_health(user.get_max_health() + accessory.get_health_boost())
                user.set_attack(user.get_attack() + accessory.get_attack_boost())
                user.set_mana(user.get_mana() + accessory.get_mana_boost())
                user.set_max_mana(user.get_max_mana() + accessory.get_mana_boost())
                user.accessory = accessory

    def info(self, user):
        choice = input("What do you want to find out more about? (weapons, spells, armours, accessories): ")
        
        if choice.lower() not in ["weapons", "spells", "armours", "accessories"]:
            print(f"\nYou do not own any {choice}")

        elif choice == "weapons":
            self.weapon_info(user)

        elif choice == "spells":
            self.spell_info(user)

        elif choice == "armours":
            self.armour_info(user)

        elif choice == "accessories":
            self.accessory_info(user)
                
        
    def weapon_info(self, user):
        if len(user.get_weapons()) == 0:
            print("\nYou do not own any weapons yet")

        else:
            weapons = []
            for weapon in user.get_weapons():
                print("\nIn your inventory you have: ")
                print(f"- {weapon.get_name()}")
                weapons.append(weapon.get_name().lower())

            decision = input("\nWhich weapon do you want to find out more about? : ")
            if decision not in weapons:
                print(f"You do not own {decision}")

            else:
                print("\n")
                print(user.get_weapons()[weapons.index(decision)].get_description())

    def spell_info(self, user):
        if len(user.get_spells()) == 0:
            print("\nYou do not own any spells yet")

        else:
            spells = []
            print("\nIn your inventory you have: ")
            for spell in user.get_spells():
                print(f"- {spell.get_name()}")
                spells.append(spell.get_name().lower())

            decision = input("\nWhich spell do you want to find out more about? : ")
            if decision not in spells:
                print(f"You do not own {decision}")

            else:
                print("\n")
                print(user.get_spells()[spells.index(decision)].get_description())

    def armour_info(self, user):
        if len(user.get_armours()) == 0:
            print("\nYou do not own any amours yet")

        else:
            armours = []
            for armour in user.get_armours():
                print("\nIn your inventory you have: ")
                print(f"- {armour.get_name()}")
                armours.append(armour.get_name().lower())

            decision = input("\nWhich armour do you want to find out more about? : ")
            if decision not in armours:
                print(f"You do not own {decision}")

            else:
                print("\n")
                print(user.get_armours()[armours.index(decision)].get_description())

    def accessory_info(self, user):
        if len(user.get_accessories()) == 0:
            print("\nYou do not own any accessories yet")

        else:
            accessories = []
            for accessory in user.get_accessories():
                print("\nIn your inventory you have: ")
                print(f"- {accessory.get_name()}")
                accessories.append(accessory.get_name().lower())

            decision = input("\nWhich accesssory do you want to find out more about? : ")
            if decision not in accessories:
                print(f"You do not own {decision}")

            else:
                print("\n")
                print(user.get_accessories()[accessories.index(decision)].get_description())
                
    def display_room_name(self):
        print("\n=========================")
        space = " "*int((25-len(self.room.get_name()))/2)
        print(f"{space}{self.room.get_name()}{space}")
        print("=========================")

    def display_room_description(self):
        print("\n", end="")
        time.sleep(1)
        print(self.room.description)
        time.sleep(2)
        self.look()
        self.room.set_been_here(True)

    def get_action(self):
        
        decision = input("\nWhat do you wish to do? (type help for list of actions): ")
        
        while decision not in self.actions:
            print(f"\nYou do not have the physical and mental capability to {decision}")
            decision = input("\nWhat do you wish to do? (type help for list of actions): ")

        return decision

    def collect_loot(self, attacker, loot):
        
        if loot.get_type() == "weapon":
            attacker.set_weapons(loot)
            print(f"\nYou obtained a {loot.get_name()}, a powerful weapon")
            time.sleep(1)
            
        elif loot.get_type() == "spell":
            attacker.set_spells(loot)
            print(f"\nYou obtained a {loot.get_name()}, a powerful spell")
            time.sleep(1)

        elif loot.get_type() == "armour":
            attacker.set_armours(loot)
            print(f"\nYou obtained a {loot.get_name()}, a powerful armour")
            time.sleep(1)

        elif loot.get_type() == "accessory":
            attacker.set_accessories(loot)
            print(f"\nYou obtained a {loot.get_name()}, a powerful accessory")
            time.sleep(1)

    def end_game(self):
        print("__   _______ _   _  ______ _____ ___________")
        print("\ \ / /  _  | | | | |  _  \_   _|  ___|  _  \\")
        print(" \ V /| | | | | | | | | | | | | | |__ | | | |")
        print("  \ / | | | | | | | | | | | | | |  __|| | | |")
        print("  | | \ \_/ / |_| | | |/ / _| |_| |___| |/ /")
        print("  \_/  \___/ \___/  |___/  \___/\____/|___/ ")
        self.end = True

    def win(self, weapon):
        print(f"\nUsing the almighty {weapon.get_name()}, you struck the Dark Lord Voldermort down, crippling him of all his powers and stop his evil tyranny over the school")
        print(" _____ ___________   _____ _       ___  _____ _   _ ")
        print("|  __ \  _  |  _  \ /  ___| |     / _ \|_   _| \ | |")
        print("| |  \/ | | | | | | \ `--.| |    / /_\ \ | | |  \| |")
        print("| | __| | | | | | |  `--. \ |    |  _  | | | | . ` |")
        print("| |_\ \ \_/ / |/ /  /\__/ / |____| | | |_| |_| |\  |")
        print(" \____/\___/|___/   \____/\_____/\_| |_/\___/\_| \_/")
        self.end = True