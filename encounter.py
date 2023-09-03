#import builtins
import random
import time

#import local files
import item
import enemy as enemies_


class encounter:
    """
    Parent class for fights
    """

    def __init__(self, enemy: "Enemy"):
        self.enemies = [enemy]
        self.dead = []
        with open("settings.txt", "r") as f:
            out = f.readlines()
            out = [x.split()[1] for x in out]
        self.sleep = int(out[0])

    def fight(self, player: "character") -> bool:
        """
        main loop for the encounter, return True if player wins, False if otherwise
        'player' is the player character
        """
        self.player = player
        #for the variable 'state', 0 means the fight is ongoing, 1 means the player wins, 2 means the player loses
        state = 0
        while state == 0:

            #display state of player and enemies
            self.status()

            advance = False
            while not advance:
                decision = self.get_choice()

                if decision == self.player.weapon.name.lower():
                    advance = self.attack()

                elif decision == "spell":
                    advance = self.spell()

                elif decision == "flask":
                    advance = self.flask()

                elif decision == "shield":
                    self.shield()
                    advance = True

                elif decision == "flee":
                    print("You activate your secret technique and disengage")
                    return False

            state = self.over()
            if state != 0:
                break
            
            self.enemy_turn(decision)

            state = self.over()

        if state == 1:
            return True

        elif state == 2:
            return False
        

    def status(self) -> None:
        """
        print the status of player and all enemies
        """
        player = self.player
        enemies = self.enemies
        dead = self.dead

        #print player health, mana, flasks
        print(f"\n{'-'*50}\n")
        print(f"{player.name} has {player.health} health")
        print(f"{player.name} has {player.mana} mana")
        print(f"{player.name} has {player.health_flask} Flask of Crimson Tears")
        print(f"{player.name} has {player.mana_flask} Flask of Cerulean Tears")

        #print enemy health
        print()
        for enemy in enemies:
            print(f"{enemy.name} has {enemy.health} health")

        #print dead enemies
        for die in dead:
            print(f"{die.name} has 0 health")
    
    def get_choice(self) -> str:
        """
        get choice of action from user
        """
        #setting accepted commands
        #setting prompt message
        accepted = [self.player.weapon.name.lower(), "spell", "flask"]
        add = ""
        
        if "Shield" in self.player.get_upgrades():
            accepted.append("shield")
            add += " / Shield"
            
        if "Flee" in self.player.get_upgrades():
            accepted.append("flee")
            add += " / Flee"
            
        prompt = f"\nWhat do you want to use? ({self.player.weapon.name} / Spell / Flask{add}): "

        #getting cost of cheapest spell
        min_cost = self.player.spells[0].cost
        for spell in self.player.spells:
            if spell.cost < min_cost:
                min_cost = spell.cost

        #getting cost of shield
        shield_cost = 10

        valid = False
        while not valid:

            #check if decision is in accepted commands
            decision = input(prompt)
            while decision.lower() not in accepted:
                print(f"\nYou tried to use {decision} but nothing happened")
                decision = input(prompt)

            decision = decision.lower()
            #check if user has enough mana for any spells
            if (decision == "spell") and (self.player.mana < min_cost):
                print("\nYou do not have enough mana to cast spells\n")
                time.sleep(self.sleep)

            #check if user has any flasks
            elif (decision == "flask") and (self.player.health_flask + self.player.mana_flask == 0):
                print("\nYou ran out of flasks\n")
                time.sleep(self.sleep)

            #check if user has enough mana to shield
            elif (decision == "shield") and (self.player.mana < shield_cost):
                print("\nYou do not have enough mana to shield yourself\n")
                time.sleep(self.sleep)

            else:
                return decision

    def enemy_turn(self, player_choice: str) -> None:
        """
        let enemies attack
        """

        #enemies take turns in random order
        enemies = self.enemies
        random.shuffle(enemies)
        
        for enemy in enemies:

            #negate damage if player is shielding
            if player_choice == "shield":
                print(f"\n{enemy.name} used {enemy.move}, but it was deflected by your shield")
                time.sleep(self.sleep)

            #deal damage to the player 
            else:
                damage = max(1, enemy.attack - self.player.defence)
                self.player.health = self.player.health - damage
                print(f"\n{enemy.name} used {enemy.move}, dealing {damage} damage to {self.player.name}")
                time.sleep(self.sleep)
                if self.player.health <= 0:
                    break

    def target(self) -> "Enemy":
        """
        let player choose a target for their attack/spell
        returns enemy object to be attacked, or none if cancelled
        """

        enemies = self.enemies
        print("Targets:\n")
        for enemy in enemies:
            print(f" - {enemy.name : <15} {str(enemy.health) + ' health remaining' : >20}")
        print()
        
        accepted = [enemy.name.lower() for enemy in enemies]
        accepted.append("cancel")
            
        target = input("Which enemy do you want to attack? (type cancel to cancel): ")
        while target.lower() not in accepted:
            print(f"\nYou tried to attack {target} but they seem to have mysteriously disappeared")
            time.sleep(self.sleep)
            target = input("Which enemy do you want to attack? (type cancel to cancel): ")

        if target.lower() == "cancel":
            return None

        return enemies[accepted.index(target.lower())]

    def damage(self, weapon: "Weapon/Spell", target: "enemy") -> None:
        """
        deal damage to target using the weapon
        """
        #calculate damage dealt
        damage = weapon.attack + self.player.attack - target.defence
        target.health = target.health - damage

        #check if enemy is dead
        if target.health > 0:
            print(f"\n{self.player.name}{weapon.move}, dealing {damage} damage to {target.name}")
            time.sleep(self.sleep)
        else:
            print(f"\n{self.player.name}{weapon.win_front}{target.name}{weapon.win_back}")
            self.enemies.remove(target)
            target.health = 0
            self.dead.append(target)
            time.sleep(self.sleep)

    def attack(self) -> None:
        """
        damages enemy using weapon
        return True if turn passes, return False if cancelled action
        """
        
        target = self.target()
        if target == None:
            return False

        self.damage(self.player.weapon, target)
        
        return True

    def spell(self) -> bool:
        """
        deducts mana from player for using a spell
        damages enemy using spell
        return True if turn passes, return False if cancelled action
        """
        print("\nSpells:")
        spells = self.player.spells
        for i, spell in enumerate(spells):
            print(f"- {spell.name} ({spell.cost} mana)")
        time.sleep(self.sleep)

        accepted = [spell.name.lower() for spell in spells]
        accepted.append("cancel")

        valid = False
        while not valid:
            
            choice = input("\nWhich spell would you like to cast? (type cancel to cancel): ")
            
            while choice.lower() not in accepted:
                print(f"\nYou tried to cast {choice} but it blew up in your face")
                time.sleep(self.sleep)
                choice = input("\nWhich spell would you like to cast? (type cancel to cancel): ")

            if choice.lower() == "cancel":
                return False
            
            elif self.player.spells[accepted.index(choice.lower())].cost > self.player.mana:
                print(f"You do not have enough mana to cast {choice}")
                
            else:
                valid = True

        target = self.target()
        if target == None:
            return False
        
        spell = self.player.spells[accepted.index(choice.lower())]
        cost = spell.cost
        self.player.mana = self.player.mana - cost
        print(f"\nYou used up {cost} mana points")

        self.damage(spell, target)

        return True

    def flask(self) -> bool:
        """
        let player choose a flask to use
        return True if turn passes, return False if cancelled action
        """
        user = self.player
        print()
        print(f"Number of Flask of Crimson Tears: {user.health_flask} (restores {item.FlaskOfCrimsonTears().health} health)")
        print(f"Number of Flask of Cerulean Tears: {user.mana_flask} (restores {item.FlaskOfCeruleanTears().mana} mana)\n")
        time.sleep(self.sleep)

        valid = False
        while not valid:
            
            selection = input("Which flask would you like to drink? (type cancel to cancel): ")
            
            while selection.lower() not in ["flask of crimson tears", "flask of cerulean tears", "cancel"]:
                print(f"\nYou tried drinking {selection} but nothing happened\n")
                selection = input("Which flask would you like to drink? (type cancel to cancel): ")

            if selection.lower() == "flask of crimson tears":
                if user.health_flask <= 0:
                    print("\nYou ran out of Flasks of Crimson Tears\n")
                    time.sleep(self.sleep)
                else:
                    self.health_flask()
                    valid = True

            elif selection.lower() == "flask of cerulean tears":
                if user.mana_flask <= 0:
                    print("\nYou ran out of Flasks of Cerulean Tears\n")
                    time.sleep(self.sleep)
                else:
                    self.mana_flask()
                    valid = True

            elif selection.lower() == "cancel":
                return False
            
        return True
    
    def health_flask(self) -> None:
        """
        remove one health flask from player
        restore hp to player up to their maximum hp
        """
        #remove flask
        self.player.health_flask = self.player.health_flask - 1

        #heal player
        healing = min(self.player.max_health - self.player.health, item.FlaskOfCrimsonTears().health)
        self.player.health = self.player.health + healing
        print(f"\nYou drank a Flask of Crimson Tears and gained {healing} health")
        time.sleep(self.sleep)

    def mana_flask(self) -> None:
        """
        remove one mana flask from player
        restore mana to player up to their maximum mana
        """
        #remove flask
        self.player.mana_flask = self.player.mana_flask - 1

        #restore player mana
        mana = min(self.player.max_mana - self.player.mana, item.FlaskOfCeruleanTears().mana)
        self.player.mana = self.player.mana + mana
        print(f"\nYou drank a Flask of Cerulean Tears and gained {mana} mana")
        time.sleep(self.sleep)

    def shield(self) -> None:
        """
        deducts 10 mana from player for using shield
        """
        #get shield cost
        cost = 10
        
        self.player.mana = self.player.mana - cost
        print(f"\nYou used up {cost} mana points to empower your shield")
        time.sleep(self.sleep)
        

    def over(self):
        """
        determines whether the fight should continue and outcome of fight
        return 0 for continue, 1 for player win, 2 for player loss
        """
        player = self.player
        enemies = self.enemies
        
        if player.health <= 0:
            return 2
        
        elif sum([enemy.health for enemy in enemies]) <= 0:
            return 1
        
        else:
            return 0

class voldemort_fight(encounter):
    """
    an encounter that inherits from the encounter class
    """
    def __init__(self, enemy: "Enemy"):
        super().__init__(enemy)
        self.phases = [enemies_.Phase2()]
        self.transfer = 0

    def damage(self, weapon: "Weapon/Spell", target: "enemy") -> None:
        """
        deal damage to target using the weapon

        changing this method so that voldemort can revive himself after phase 1
        """
        #calculate damage dealt
        damage = weapon.attack + self.player.attack - target.defence
        target.health = target.health - damage

        #check if enemy is dead
        if target.health > 0:
            print(f"\n{self.player.name}{weapon.move}, dealing {damage} damage to {target.name}")
            time.sleep(self.sleep)
        else:
            #check if enemy can revive
            if len(self.phases) == 1:
                self.phase_transfer()
            else:
                self.enemies.remove(target)
                target.health = 0

    def phase_transfer(self):
        """
        Intermission for phase change
        """
        print("\ninsert phase transition")
        self.enemies[0] = self.phases[0]
        self.phases.remove(self.phases[0])
        self.transfer = 1

    def enemy_turn(self, player_choice: str) -> None:
        """
        let enemies attack
        """

        if self.transfer == 1:
            self.transfer = 0
            return
        
        #enemies take turns in random order
        enemies = self.enemies
        random.shuffle(enemies)
        
        for enemy in enemies:

            #negate damage if player is shielding
            if player_choice == "shield":
                print(f"\n{enemy.name} used {enemy.move}, but it was deflected by your shield")
                time.sleep(self.sleep)

            #deal damage to the player 
            else:
                damage = max(1, enemy.attack - self.player.defence)
                self.player.health = self.player.health - damage
                print(f"\n{enemy.name} used {enemy.move}, dealing {damage} damage to {self.player.name}")
                time.sleep(self.sleep)
                if self.player.health <= 0:
                    break

class gabriel_fight(encounter):
    """
    an encounter that inherits from the encounter class
    """

    def __init__(self, enemy: "Enemy"):
        super().__init__(enemy)
        self.timer = 3
        self.spinning_blades = 0
        self.melee = ["buster sword", "master sword", "virtuous treaty",
                      "zenith", "rgx butterfly knife", "wand", "toy knife"]
        self.enemy = self.enemies[0]
        self.spin_warning = 0

    def enemy_turn(self, player_choice: str) -> None:
        """
        enemy turn

        changing this method to implement gabriel's fight mechanics
        """
        enemy = self.enemy
        if self.timer > 0:
            if player_choice == "shield":
                print(f"\nGabriel used light combo, but it was deflected by your shield")
            else:
                damage = max(1, enemy.attack - self.player.defence)
                self.player.health = self.player.health - damage
                print(f"\nGabriel used light combo, dealing {damage} damage to {self.player.name}")
            time.sleep(self.sleep)

        if self.timer > 1:
            enemy.defence = 10
            self.spinning_blades = 1
            print(f"Gabriel used spinning blades, increasing his defence by 10 for one turn")
            time.sleep(self.sleep)

        if self.timer == 1:
            enemy.defence = 0
            self.spinning_blades = 0

        if self.timer == 0:
            self.spinning_blades = 0
            self.timer = 3
            if player_choice == self.player.weapon.name.lower() and player_choice in self.melee:
                print("\nGabriel used his special move, Sword Throw")
                time.sleep(self.sleep)
                print(f"""
As you swung the {self.player.weapon.name}, you +PARRIED Gabriel's
Sword Throw, sending it back to him and dealing 150 damage""")
                enemy.health = enemy.health - 150
            else:
                if player_choice == "shield":
                    print(f"\nGabriel used his special move, Sword Throw, but it was deflected by your shield")
                else:
                    damage = max(1, 60 - self.player.defence)
                    self.player.health = self.player.health - damage
                    print(f"\nGabriel used his special move, Sword Throw, dealing {damage} damage to {self.player.name}")

        self.timer = self.timer - 1

    def damage(self, weapon: "Weapon/Spell", target: "enemy") -> None:
        """
        deal damage to target using the weapon

        changing this method so that executing melee attacks while spinning blades is active deals damage to the player
        """
        #calculate damage dealt
        damage = max(1, weapon.attack + self.player.attack - target.defence)
        target.health = target.health - damage

        #check if enemy is dead
        if target.health > 0:
            print(f"\n{self.player.name}{weapon.move}, dealing {damage} damage to {target.name}")
            time.sleep(self.sleep)
            
        else:
            print(f"\n{self.player.name}{weapon.win_front}{target.name}{weapon.win_back}")
            self.enemies.remove(target)
            target.health = 0
            self.dead.append(target)
            time.sleep(self.sleep)

        if weapon.name.lower() in self.melee and self.spinning_blades == 1:
            damage = max(1, self.enemy.attack - self.player.defence)
            self.player.health = self.player.health - damage
            print(f"\nGabriel's spinning blades hit you as you attacked, dealing {damage} damage to you")
            if self.spin_warning == 0:
                print("You would do well to keep your distance while this ability is active")
                self.spin_warning = 1
            

    def target(self) -> "Enemy":
        """
        let player choose a target for their attack/spell
        returns enemy object to be attacked, or none if cancelled

        changing this method because "gabriel, apostate of hate" with punctuation is a serious pain in the ass to type out
        """

        enemy = self.enemy
        print()
        print(f" - {'Gabriel' : <15} {str(enemy.health) + ' health remaining' : >20}")
        print()
        
        accepted = ["gabriel", "cancel"]
            
        target = input("Which enemy do you want to attack? (type cancel to cancel): ")
        while target.lower() not in accepted:
            print(f"\nYou tried to attack {target} but they seem to have mysteriously disappeared")
            time.sleep(self.sleep)
            target = input("Which enemy do you want to attack? (type cancel to cancel): ")

        if target.lower() == "cancel":
            return None

        return self.enemies[accepted.index(target.lower())]

    def status(self) -> None:
        """
        print the status of player and all enemies

        changing this method to telegraph gabriel's sword throw
        """
        player = self.player
        enemies = self.enemies
        dead = self.dead

        #print player health, mana, flasks
        print(f"\n{'-'*50}\n")
        print(f"{player.name} has {player.health} health")
        print(f"{player.name} has {player.mana} mana")
        print(f"{player.name} has {player.health_flask} Flask of Crimson Tears")
        print(f"{player.name} has {player.mana_flask} Flask of Cerulean Tears")

        #print enemy health
        print()
        for enemy in enemies:
            print(f"{enemy.name} has {enemy.health} health")

        #print dead enemies
        for die in dead:
            print(f"{die.name} has 0 health")

        if self.timer == 0:
            print("\nGabriel is preparing something")