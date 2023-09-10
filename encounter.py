#import builtins
import random
import time
import tkinter as tk
import string

#import local files
import item
import enemy as e

class encounter:
    """
    Parent class for fights
    """

    def __init__(self, enemy: "Enemy"):
        self.initenemy = enemy
        self.enemies = [enemy]
        self.dead = []
        with open("settings.txt", "r") as f:
            out = f.readlines()
            out = [x.split()[1] for x in out]
        self.sleep = int(out[0])
        self.up = out[1]
        self.down = out[2]
        self.enter = out[3]
        self.line = 1
        self.tips = ["Remember to restore your health and mana before every fight",
                    "Other rooms may have useful drops that could make this fight easier"]
        self.taglines = []

    def reapply_tag(self):
        for tag in self.text.tag_names():
            self.text.tag_delete(tag)

        for i, line in enumerate(self.taglines):
            color, start, end = line
            self.text.tag_add(f"colour{i}", start, end)
            self.text.tag_config(f"colour{i}", foreground=color)
        
    def show(self, prompt, options, deletebefore):
        data = self.text.get("1.0",'end-1c')
        self.delete(True)
        keep = ""
        if not deletebefore:
            keep = data.split(prompt)[0]
            
        """main action for user to get the list of possible actions"""
        # Displays the list of actions the user can do
        p = self.pointer.get()
        self.write(keep+prompt+"\n")
        for i, e in enumerate(options):
            arrow = " "
            if p == i: arrow = ">"
            self.write(f"{arrow} {e}")
        self.reapply_tag()
        
    def up_action(self, prompt, options, delete):
        p = self.pointer.get()
        if p != 0:
            self.pointer.set(p-1)
        else:
            self.pointer.set(len(options)-1)
    
        self.show(prompt, options, delete)
    
    def down_action(self, prompt, options, delete):
        p = self.pointer.get()
        if p != len(options)-1:
            self.pointer.set(p+1)
        else:
            self.pointer.set(0)
    
        self.show(prompt, options, delete)
    
    def get_input(self, prompt, options, displayoptions = None, deletebefore = True):
        """sub action for run() that prompts user for a main action"""
        if displayoptions is None:
            displayoptions = options
        self.show(prompt, displayoptions, deletebefore)
        self.root.bind(f'<{self.enter}>', lambda x: self.pause_var.set("done"))
        self.root.bind(f"<{self.up}>", lambda e: self.up_action(prompt, displayoptions, deletebefore))
        self.root.bind(f"<{self.down}>", lambda e: self.down_action(prompt, displayoptions, deletebefore))
        self.root.wait_variable(self.pause_var)
        self.root.unbind(f'<{self.enter}>')
        self.root.unbind(f"<{self.up}>")
        self.root.unbind(f"<{self.down}>")
        self.pause_var.set("")
        decision = options[self.pointer.get()]
        self.pointer.set(0)
        self.delete()
        return decision

    def reset(self):
        """
        resets the enemies when the player runs away
        """
        self.initenemy.__init__()
        og = self.initenemy
        self.__init__(og)

    def write(self, txt):
        """
        writes txt to the text field
        
        the colors rely on the line tracker which only increments by 1
        for each thing you write pls pls pls do not use newline characters
        """
        self.text['state'] = 'normal'
        self.text.insert(tk.END, txt+"\n")
        self.text['state'] = 'disabled'
        self.line += 1

    def write_color(self, txt, color):
        """
        writes red to the text field in red

        the colors rely on the line tracker which only increments by 1
        for each thing you write pls pls pls do not use newline characters
        """
        self.text['state'] = 'normal'
        self.text.insert(tk.END, txt+"\n")

        self.taglines.append([color, f"{self.line}.0", f"{self.line}.end"])
        self.text['state'] = 'disabled'
        self.line += 1

    def delete(self, keeptag=False):
        """
        clears the text field
        """
        self.text['state'] = 'normal'
        self.text.delete("1.0", tk.END)
        self.text['state'] = 'disabled'
        self.line = 1

        #deleting tags
        if not keeptag:
            self.taglines = []
            for tag in self.text.tag_names():
                self.text.tag_delete(tag)

    def delay(self):
        """
        stops execution for self.sleep seconds
        """
        if self.sleep == 0:
            pass
        else:
            self.root.after(self.sleep*1000, lambda: self.pause.set(self.pause.get()+1))
            self.root.wait_variable(self.pause)

    def fight(self, player: "character", root: "tk.Tk()", text: "tk.Text()") -> int:
        """
        main loop for the encounter, return 1 if player wins, 2 if player dies, 3 if player flees
        'player' is the player character
        'root' is the tk window
        'text' is the text field to write messages to
        """
        self.player = player
        self.root = root
        self.text = text
        self.pause = tk.IntVar()
        self.pointer = tk.IntVar()
        self.pause_var = tk.StringVar()
        #for the variable 'state', 0 means the fight is ongoing, 1 means the player wins, 2 means the player loses
        self.delete()
        state = 0
        while state == 0:

            #display state of player and enemies

            self.status()
            
            advance = False
            while not advance:

                decision = self.get_choice()

                if decision.lower() == "weapon":
                    advance = self.attack()

                elif decision.lower() == "spell":
                    advance = self.spell()

                elif decision.lower() == "flask":
                    advance = self.flask()

                elif decision.lower() == "defend":
                    self.write(f"You raise up your {self.player.shield.name}")
                    advance = True

                elif decision.lower() == "escape":
                    self.reset()
                    self.delete()
                    self.write("You put on the shade cloak and dashed away from the enemy")
                    self.delay()
                    return 3

            state = self.over()
            if state != 0:
                break
            
            self.enemy_turn(decision)

            self.write("")
            self.write(f"{'-'*50}")

            state = self.over()

        if state == 1:
            return 1

        elif state == 2:
            self.end_game()
            self.write("")
            self.write(random.choice(self.tips))
            return 2
        

    def status(self) -> None:
        """
        print the status of player and all enemies
        """
        player = self.player
        enemies = self.enemies
        dead = self.dead

        #print player health, mana, flasks
        self.write("")
        self.write(f"{player.name}")
        self.write_color(f"Health : {player.health} / {player.max_health}", "green")
        self.write_color(f"Mana : {player.mana} / {player.max_mana}", "blue")
        self.write(f"Flask of Crimson Tears : {player.health_flask}")
        self.write(f"Flask of Cerulean Tears : {player.mana_flask}")
        self.delay()

        #print enemy health
        self.write("")
        for enemy in enemies:
            self.write_color(f"{enemy.name} has {enemy.health} health", "red")
        self.delay()

        #print dead enemies
        for die in dead:
            self.write_color(f"{die.name} has 0 health", "grey")
        if len(dead) != 0:
            self.delay()
    
    def get_choice(self) -> str:
        """
        get choice of action from user
        """
        valid = False

        choices = ["Weapon", "Spell", "Flask"]

        if self.player.shield != None:
            choices.append("Defend")

        if "Shade Cloak" in self.player.get_upgrades():
            choices.append("Escape")

        self.write("")
        return self.get_input("What do you want to use?", choices, None, False)

    def enemy_turn(self, player_choice: str) -> None:
        """
        let enemies attack
        """

        #enemies take turns in random order
        enemies = self.enemies.copy()
        random.shuffle(enemies)
        
        for enemy in enemies:

            #negate damage if player is shielding
            damage = max(1, enemy.attack - self.player.defence)
            if player_choice.lower() == "defend":
                damage = int((self.player.shield.negation/100)*(damage))
                
                
            self.player.health = self.player.health - damage
            self.write("")
            self.write(f"{enemy.name} used {enemy.move}, dealing {damage} damage to {self.player.name}")
            self.delay()
            if self.player.health <= 0:
                break

    def target(self) -> "Enemy":
        """
        let player choose a target for their attack/spell
        returns enemy object to be attacked, or none if cancelled
        """

        if len(self.enemies) == 1:
            self.delete()
            return self.enemies[0]

        option_var = tk.StringVar()
        cont_var = tk.StringVar()
        def key_press(e):
            option_var.set(e.char)
            cont_var.set("go")

        enemies = self.enemies
        self.write("")
        self.write("Which enemy do you want to attack?")
        for i, enemy in enumerate(enemies):
            self.write(f"[{i+1}] {enemy.name : <15} {str(enemy.health) + ' health remaining' : >25}")
            self.root.bind(str(i+1), key_press)
        self.write(f"[{len(enemies)+1}] Cancel Action")
        self.root.bind(str(len(enemies)+1), key_press)

        self.root.wait_variable(cont_var)
        option = option_var.get()
        
        if option == str(len(enemies)+1):
            return None
        else:
            self.delete()
            return enemies[int(option)-1]
        

    def damage(self, weapon: "Weapon/Spell", target: "enemy") -> None:
        """
        deal damage to target using the weapon
        """
        #calculate damage dealt
        damage = max(1, weapon.attack + self.player.attack - target.defence)
        target.health = target.health - damage

        #check if enemy is dead
        if target.health > 0:
            self.write("")
            self.write(f"{self.player.name}{weapon.move}, dealing {damage} damage to {target.name}")
            self.delay()
        else:
            self.write("")
            self.write(f"{self.player.name}{weapon.win_front}{target.name}{weapon.win_back}")
            self.enemies.remove(target)
            target.health = 0
            self.dead.append(target)
            self.delay()

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
            
        spells = self.player.spells.copy()
        spell_display = []
        for spell in spells:
            spell_display.append(f"{spell.name} ({spell.cost} mana)")
        spells.append("Cancel")
        spell_display.append("Cancel")
        
        valid = False

        while not valid:
            
            self.delay()
            self.status()
            self.delay()
            self.write("")
            choice = self.get_input("Which spell would you like to cast?", spells, spell_display, False)

            if choice == "Cancel":
                self.status()
                self.delay()
                return False

            elif choice.cost > self.player.mana:
                self.write("")
                self.write(f"You do not have enough mana to cast {choice.name}")
                

            else:
                valid = True

        target = self.target()
        if target == None:
            return False
        
        self.player.mana = self.player.mana - choice.cost
        self.write("")
        self.write(f"You used up {choice.cost} mana points")

        self.damage(choice, target)

        return True

    def flask(self) -> bool:
        """
        let player choose a flask to use
        return True if turn passes, return False if cancelled action
        """

        user = self.player
        health, mana = item.FlaskOfCrimsonTears(), item.FlaskOfCeruleanTears()

        flasks = [health, mana, "Cancel"]
        display = [f"Flask of Crimson Tears (restores {health.health} health)", f"Flask of Cerulean Tears (restores {mana.mana} health)", "Cancel"]
        
        valid = False

        while not valid:

            self.delay()
            self.status()
            self.delay()
            self.write("")

            choice = self.get_input("Which Flask would you like to drink?", flasks, display, False)

            if choice == "Cancel":
                self.status()
                self.delay()
                return False

            elif choice == health:
                if user.health_flask <= 0:
                    self.write("You ran out of Flask of Crimson Tears")

                elif user.health == user.max_health:
                    self.write("You do not need to drink a Flask of Crimson Tears")

                else:
                    self.health_flask()
                    return True
                    

            elif choice == mana:
                if user.mana_flask <= 0:
                    self.write("You ran out of Flask of Cerulean Tears")

                elif user.mana == user.max_mana:
                    self.write("You do not need to drink a Flask of Cerulean Tears")

                else:
                    self.mana_flask()
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
        self.write("")
        self.write(f"You drank a Flask of Crimson Tears and gained {healing} health")
        self.delay()

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
        self.write("")
        self.write(f"You drank a Flask of Cerulean Tears and gained {mana} mana")
        self.delay()

    def shield(self) -> None:
        """
        deducts 10 mana from player for using shield
        """
        #get shield cost

        self.delete()
        self.player.mana = self.player.mana - cost
        self.write("")
        self.write(f"You used up {cost} mana points to empower your shield")
        self.delay()
        

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
        
    def end_game(self) -> None:

        def short_del():
            pause = tk.StringVar()
            self.root.after(100, lambda: pause.set("go"))
            self.root.wait_variable(pause)
        
        """displays scenario when user dies"""
        self.write("__   _______ _   _  ______ _____ ___________")
        short_del()
        self.write("\ \ / /  _  | | | | |  _  \_   _|  ___|  _  \\")
        short_del()
        self.write(" \ V /| | | | | | | | | | | | | | |__ | | | |")
        short_del()
        self.write("  \ / | | | | | | | | | | | | | |  __|| | | |")
        short_del()
        self.write("  | | \ \_/ / |_| | | |/ / _| |_| |___| |/ /")
        short_del()
        self.write("  \_/  \___/ \___/  |___/  \___/\____/|___/ ")

class voldemort_fight(encounter):
    """
    an encounter that inherits from the encounter class
    """
    def __init__(self, enemy: "Enemy"):
        super().__init__(enemy)
        self.phases = [e.Phase2()]
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
            self.write("")
            self.write(f"{self.player.name}{weapon.move}, dealing {damage} damage to {target.name}")
            self.delay()
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
        self.delete()
        self.write("insert phase transition")
        self.enemies[0] = self.phases[0]
        self.phases.remove(self.phases[0])
        self.transfer = 1
        self.delay()

    def enemy_turn(self, player_choice: str) -> None:
        """
        let enemies attack

        changing this method so that phase 2 doesn't take a turn immediately after reviving
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
                self.write("")
                self.write(f"{enemy.name} used {enemy.move}, but it was deflected by your shield")
                self.delay()

            #deal damage to the player 
            else:
                damage = max(1, enemy.attack - self.player.defence)
                self.player.health = self.player.health - damage
                self.write("")
                self.write(f"{enemy.name} used {enemy.move}, dealing {damage} damage to {self.player.name}")
                self.delay()
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
        self.tips = ["Gabriel's Spinning Blades make close range attacks risky. Try engaging him at a distance with spells.",
                    "Gabriel doesn't activate spinning blades when he's winding up to use Sword Throw."]

    def enemy_turn(self, player_choice: str) -> None:
        """
        enemy turn

        changing this method to implement gabriel's fight mechanics
        """
        enemy = self.enemy
        if self.timer > 0:
            if player_choice == "shield":
                self.write("")
                self.write(f"Gabriel used light combo, but it was deflected by your shield")
            else:
                damage = max(1, enemy.attack - self.player.defence)
                self.player.health = self.player.health - damage
                self.write("")
                self.write(f"Gabriel used light combo, dealing {damage} damage to {self.player.name}")
            self.delay()

        if self.timer > 1:
            enemy.defence = 10
            self.spinning_blades = 1
            self.write(f"Gabriel used spinning blades, increasing his defence by 10 for one turn")
            self.delay()

        if self.timer == 1:
            enemy.defence = 0
            self.spinning_blades = 0

        if self.timer == 0:
            self.spinning_blades = 0
            self.timer = 3
            if player_choice == "weapon" and self.player.weapon.name.lower() in self.melee:
                self.write("")
                self.write("Gabriel used his special move, Sword Throw")
                self.delay()
                self.write("")
                self.write(f"As you swung the {self.player.weapon.name}, you +PARRIED Gabriel's")
                self.write("Sword Throw, sending it back to him and dealing 150 damage")
                enemy.health = enemy.health - 150
            else:
                if player_choice == "shield":
                    self.write("")
                    self.write(f"Gabriel used his special move, Sword Throw, but it was deflected by your shield")
                else:
                    damage = max(1, 60 - self.player.defence)
                    self.player.health = self.player.health - damage
                    self.write("")
                    self.write(f"Gabriel used his special move, Sword Throw, dealing {damage} damage to {self.player.name}")

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
            self.write("")
            self.write(f"{self.player.name}{weapon.move}, dealing {damage} damage to {target.name}")
            self.delay()
            
        else:
            self.write("")
            self.write(f"{self.player.name}{weapon.win_front}{target.name}{weapon.win_back}")
            self.enemies.remove(target)
            target.health = 0
            self.dead.append(target)
            self.delay()

        if weapon.name.lower() in self.melee and self.spinning_blades == 1:
            damage = max(1, self.enemy.attack - self.player.defence)
            self.player.health = self.player.health - damage
            self.write("")
            self.write(f"Gabriel's spinning blades hit you as you attacked, dealing {damage} damage to you")
            if self.spin_warning == 0:
                self.write("You would do well to keep your distance while this ability is active")
                self.spin_warning = 1

    def status(self) -> None:
        """
        print the status of player and all enemies

        changing this method to telegraph gabriel's sword throw
        """
        player = self.player
        enemies = self.enemies
        dead = self.dead

        #print player health, mana, flasks
        self.write(f"{player.name} has {player.health} health")
        self.write(f"{player.name} has {player.mana} mana")
        self.write(f"{player.name} has {player.health_flask} Flask of Crimson Tears")
        self.write(f"{player.name} has {player.mana_flask} Flask of Cerulean Tears")
        self.delay()

        #print enemy health
        self.write("")
        for enemy in enemies:
            self.write_color(f"{enemy.name} has {enemy.health} health", "red")
        self.delay()

        #print dead enemies
        for die in dead:
            self.write_color(f"{die.name} has 0 health", "grey")
        if len(dead) != 0:
            self.delay()

        #telegraph for sword throw
        if self.timer == 0:
            self.write("")
            self.write("Gabriel is preparing something")
