#import from python built in libraries
import time
import random

#import from other files
from setup import *
import tkinter as tk
import map

temp = setup()
selfend = False
selfroom = temp[0]
selfcharacter = temp[1]
selfrooms = []
selfactions = ["look", "move", "attack", "loot", "flask", "equip", "status", "information", "settings", "map", "meow"]
selfdescription = ["Looks around the room","Move to another room", "Attack the enemny", "Search the room for loot", "Drink your flasks", "Change your equipment", "See your statistics", "Find out more about your items", "Change settings", "Shows map", "Meow"]
selfmap = map.game_map()
currentPressedKey = ""
out = []
with open("settings.txt", "r") as f:
    out = f.readlines()
    out = [x.split()[1] for x in out]
selfsleep = int(out[0])

def sleep(t):
    root.after(int(t*1000), lambda: sleepCount.set(sleepCount.get()+1))
    root.wait_variable(sleepCount)

def write(txt=""):
    text['state'] = 'normal'
    text.insert(tk.END, txt+"\n")
    text['state'] = 'disabled'

def delete():
    text['state'] = 'normal'
    text.delete("1.0", tk.END)
    text['state'] = 'disabled'

def start_typing(e):
    text['state'] = 'normal'
    data = text.get("1.0",'end-1c')
    if e.keysym == "BackSpace":
        if data != 'Tarnished, key in your name: ':
            text.delete('end-2c','end-1c')
    else:
        text.insert(tk.END, e.char)
    text['state'] = 'disabled'


def intro():
    """print introduction for the start of the game """
    
    # Displays the introduction messages
    write('Welcome to Hogwarts School of Witchcraft and Wizardry')
    sleep(selfsleep)
    write("\nThe Dark Lord Voldemort has taken over Hogwarts and opened multiple interdimensional gates, bringing hordes of enemies into the school. Your job as the chosen one is to traverse the school in order to locate The Shrieking Shack and thwart Voldemort's evil plan to take over the world.\n")
    sleep(selfsleep)
    decision = get_input("Do you wish to enter the school?", ["Yes", "No"], None, False)
    delete()
    pause_var.set("")
    
    if decision.lower() == "yes":
        text['state'] = 'normal'
        text.insert(tk.END, "Tarnished, key in your name: ")
        text['state'] = 'disabled'
        text.bind('<Key>', start_typing)
        root.bind('<Return>', lambda x: pause_var.set("done"))
        root.wait_variable(pause_var)
        root.unbind('<Return>')
        text.unbind('<Key>')
        pause_var.set("")
        name = text.get("1.0",'end-1c')[29:]
        name = name[:len(name)-1]
        delete()
        selfcharacter.name = name
        # Check if the user used the secret easter egg name
        if name == "meow":
            secret()
            root.after(selfsleep*1000, run)
        else:
            write("You boldly opened the front gates of the school and made your way into the first room\n")
            wait_for_key_press()
            root.after(selfsleep*1000, run)
            
    elif decision.lower() == "no":
        write("Due to your utter cowardice, voldemort continued to gain power, spreading his control and chaos all over the world, leading to the complete annihilation of the human race.")
        sleep(selfsleep)
        end_game()
        return
    else:
        write("Due to your indecision, voldemort continued to gain power, spreading his control and chaos all over the world, leading to the complete annihlation of the human race.")
        sleep(selfsleep)
        end_game()
        return

def wait_for_key_press():
    write("\nPress any key to continue")
    root.bind('<Key>', lambda x: pause_var.set("done"))
    root.wait_variable(pause_var)
    root.unbind('<Key>')
    pause_var.set("")
    
def show(prompt, options, deletebefore):
    data = text.get("1.0",'end-1c')
    delete()
    keep = ""
    if not deletebefore:
        keep = data.split(prompt)[0]
        
    """main action for user to get the list of possible actions"""
    # Displays the list of actions the user can do
    p = pointer.get()
    write(keep+prompt+"\n")
    for i, e in enumerate(options):
        arrow = " "
        if p == i: arrow = ">"
        write(f"{arrow} {e}")
        
def up_action(prompt, options, delete):
    p = pointer.get()
    if p != 0:
        pointer.set(p-1)
    else:
        pointer.set(len(options)-1)

    show(prompt, options, delete)

def down_action(prompt, options, delete):
    p = pointer.get()
    if p != len(options)-1:
        pointer.set(p+1)
    else:
        pointer.set(0)

    show(prompt, options, delete)

def get_input(prompt, options, displayoptions = None, deletebefore = True):
    """sub action for run() that prompts user for a main action"""
    if displayoptions is None:
        displayoptions = options
    show(prompt, displayoptions, deletebefore)
    root.bind('<Return>', lambda x: pause_var.set("done"))
    root.bind('<Up>', lambda e: up_action(prompt, displayoptions, deletebefore))
    root.bind('<Down>', lambda e: down_action(prompt, displayoptions, deletebefore))
    root.wait_variable(pause_var)
    root.unbind('<Return>')
    root.unbind('<Up>')
    root.unbind('<Down>')
    pause_var.set("")
    decision = options[pointer.get()]
    pointer.set(0)
    delete()
    return decision

        
def run():
    global selfroom
    global selfend
    delete()
    """to be run in a loop to prompt user's action"""
    display_room_name()
    # Checks if the player has entered the room before
    if not selfroom.been_here:
        # Displays a description of the room if the player has not been there before
        display_room_description()
        selfrooms.append(selfroom)
        
        if selfroom.name == "Dirtmouth":
            selfmap.dirtmouth_enter()
        elif selfroom.name == "Celestial Resort":
            selfmap.celestial_resort_enter()
        elif selfroom.name == "The Forge":
            selfmap.forge_enter()
        elif selfroom.name == "Miquella's Haligtree":
            selfmap.haligtree_enter()
        elif selfroom.name == "Aperture Lab":
            selfmap.aperture_enter()
        elif selfroom.name == "Zebes":
            selfmap.zebes_enter()
        elif selfroom.name == "Bunker":
            selfmap.bunker_enter()
        elif selfroom.name == "Asphodel":
            selfmap.asphodel_enter()
        elif selfroom.name == "Kingdom of Ku":
            selfmap.kingdom_ku_enter()
        elif selfroom.name == "Greenhill Zone":
            selfmap.greenhill_enter()
        elif selfroom.name == "The Hallow":
            selfmap.hallow_enter()
        elif selfroom.name == "Commencement":
            selfmap.commencement_enter()
        elif selfroom.name == "Midgar":
            selfmap.midgar_enter()
        elif selfroom.name == "Hyrule Kingdom":
            selfmap.hyrule_enter()
        elif selfroom.name == "The End Dimension":
            selfmap.end_dimension_enter()
        elif selfroom.name == "Kamurocho":
            selfmap.kamurocho_enter()
        elif selfroom.name == "Tower of Fate":
            selfmap.tower_enter()
        elif selfroom.name == "Shores of Nine":
            selfmap.shores_enter()
        elif selfroom.name == "Mementos":
            selfmap.mementos_enter()
        elif selfroom.name == "Ascent":
            selfmap.ascent_enter()
        elif selfroom.name == "The Shrieking Shack":
            selfmap.shrieking_enter()
        elif selfroom.name == "6th Circle of Hell":
            selfmap.sixth_circle_enter()
        elif selfroom.name == "Snowdin":
            selfmap.snowdin_enter()
        elif selfroom.name == "The Sealed Temple":
            selfmap.sealed_temple_enter()
        elif selfroom.name == "The Astral Plane":
            selfmap.astral_plane_enter()
        elif selfroom.name == "The Obra Dinn":
            selfmap.obradinn_enter()
        elif selfroom.name == "The Mushroom Kingdom":
            selfmap.mushroom_enter()
        elif selfroom.name == "Walled City 99":
            selfmap.walled_enter()
        elif selfroom.name == "The Last Resort":
            selfmap.last_resort_enter()
    
    decision = get_input("What do you wish to do?", selfactions, ["{} ({})".format(a,b) for a,b in zip(selfactions, selfdescription)])

    # Does the action the user selected

    if decision.lower() == "look":
        look(selfroom)
        
    elif decision.lower() == "move":
        move(selfroom)
        
    elif decision.lower() == "attack":
        attack(selfroom)

    elif decision.lower() == "loot":
        loot(selfcharacter, selfroom.loot)

    elif decision.lower() == "flask":
        flask(selfcharacter)

    elif decision.lower() == "equip":
        equip(selfcharacter)

    elif decision.lower() == "status":
        status(selfcharacter)

    elif decision.lower() == "information":
        info(selfcharacter)

    elif decision.lower() == "meow":
        meow()

    elif decision.lower() == "settings":
        settings()

    elif decision.lower() == "teleport":
        teleport()

    elif decision.lower() == "map":
        display_map()

    if selfroom.enemy == None and selfroom.loot == None:
        if selfroom.name == "Dirtmouth":
            selfmap.dirtmouth_clear()
        elif selfroom.name == "Celestial Resort":
            selfmap.celestial_resort_clear()
        elif selfroom.name == "The Forge":
            selfmap.forge_clear()
        elif selfroom.name == "Miquella's Haligtree":
            selfmap.haligtree_clear()
        elif selfroom.name == "Aperture Lab":
            selfmap.aperture_clear()
        elif selfroom.name == "Zebes":
            selfmap.zebes_clear()
        elif selfroom.name == "Bunker":
            selfmap.bunker_clear()
        elif selfroom.name == "Asphodel":
            selfmap.asphodel_clear()
        elif selfroom.name == "Kingdom of Ku":
            selfmap.kingdom_ku_clear()
        elif selfroom.name == "Greenhill Zone":
            selfmap.greenhill_clear()
        elif selfroom.name == "The Hallow":
            selfmap.hallow_clear()
        elif selfroom.name == "Commencement":
            selfmap.commencement_clear()
        elif selfroom.name == "Midgar":
            selfmap.midgar_clear()
        elif selfroom.name == "Hyrule Kingdom":
            selfmap.hyrule_clear()
        elif selfroom.name == "The End Dimension":
            selfmap.end_dimension_clear()
        elif selfroom.name == "Kamurocho":
            selfmap.kamurocho_clear()
        elif selfroom.name == "Tower of Fate":
            selfmap.tower_clear()
        elif selfroom.name == "Shores of Nine":
            selfmap.shores_clear()
        elif selfroom.name == "Mementos":
            selfmap.mementos_clear()
        elif selfroom.name == "Ascent":
            selfmap.ascent_clear()
        elif selfroom.name == "The Shrieking Shack":
            selfmap.shrieking_clear()
        elif selfroom.name == "6th Circle of Hell":
            selfmap.sixth_circle_clear()
        elif selfroom.name == "Snowdin":
            selfmap.snowdin_clear()
        elif selfroom.name == "The Sealed Temple":
            selfmap.sealed_temple_clear()
        elif selfroom.name == "The Astral Plane":
            selfmap.astral_plane_clear()
        elif selfroom.name == "The Obra Dinn":
            selfmap.obradinn_clear()
        elif selfroom.name == "The Mushroom Kingdom":
            selfmap.mushroom_clear()
        elif selfroom.name == "Walled City 99":
            selfmap.walled_clear()
        elif selfroom.name == "The Last Resort":
            selfmap.last_resort_clear()

    if not selfend:
        root.after(1,run)
        
def look(room):
    """main action to look around the room including rooms linked to the room and enemies in the room"""
    write()

    # Displays the connected rooms
    if room.left != None:
        write(f"To the left is {room.left.name}")
        
    if room.right != None:
        write(f"To the right is {room.right.name}")
        
    if room.forward != None:
        write(f"In front of you is {room.forward.name}")
        
    if room.back != None:
        write(f"Behind you is {room.back.name}")

    sleep(selfsleep)
    upgrades = selfcharacter.get_upgrades()

    if "Virtual Boo" in upgrades:
        if room.enemy != None:
            write(f"\nIn the middle of the room is {room.enemy.name}, {room.enemy.description}")
            sleep(selfsleep)
            write(f"\n{room.enemy.name} has {room.enemy.health} health")
            sleep(selfsleep)
        if room.loot != None:
            write(f"\nThere is {room.loot.name} hidden in {room.name}")
            sleep(selfsleep)
        else:
            write(f"\nThere is no loot hidden in {room.name}")
            sleep(selfsleep)
        
    elif room.enemy != None:
    # Displays the enemy in the room
        write(f"\nIn the middle of the room is {room.enemy.name}, {room.enemy.description}")
    wait_for_key_press()

def move(room):
    global selfroom
    """main action for user to traverse from one room to another"""
    movement = get_input('Which direction do you wish to move in?', ['left', 'right', 'forward','back'])

    # Generate a random number to see if you managed to sneak past the enemy
    caught = False

    if room.enemy != None:
        if selfcharacter.name == "meow":
            write(f"\n{room.enemy.name} cowers in your presence, granting you passage through their domain.")
            sleep(selfsleep)
        else:
            chance = random.randint(1, 3)
            if chance == 1:
                caught = True
            else:
                write(f"\nYou managed to sneak past {room.enemy.name}")
                sleep(selfsleep)

    if not caught:
        if movement.lower() == "left":
            if room.left == None:
                write("\nYou walked to the left and smashed into a wall")
                wait_for_key_press()
            else:
                selfroom = room.left
                write(f"\nYou walked into {selfroom.name}")
                wait_for_key_press()

        if movement.lower() == "right":
            if room.right == None:
                write("\nYou walked to the right and smashed into a wall")
                wait_for_key_press()
            else:
                selfroom = room.right
                write(f"\nYou walked into {selfroom.name}")
                wait_for_key_press()

        if movement.lower() == "forward":
            if room.forward == None:
                write("\nYou walked forward and smashed into a wall")
                wait_for_key_press()
            # Check if you are going to the final boss room
            elif room.forward.name == "The Shrieking Shack":
                items = selfcharacter.get_items()
                # Checks if you have the required items to enter the final boss room
                if "Dectus Medallion (right)" in items and "Dectus Medallion (left)" in items:
                    write("\nCongratulations, you placed the two Dectus Medallions together releasing trememndous amounts of energy, breaking the powerful spell on the door")
                    selfroom = room.forward
                    wait_for_key_press()
                else:
                    write("\nYou tried entering the The Shrieking Shack but the door was locked by a powerful spell")
                    sleep(selfsleep)
                    write("\nYou probably need to find a special item to break the spell (remember to loot all the rooms)")
                    wait_for_key_press()
            else:
                selfroom = room.forward
                write(f"\nYou walked into {selfroom.name}")
                wait_for_key_press()

        if movement.lower() == "back":
            if room.back == None:
                write("\nYou turned back and smashed into a wall")
                wait_for_key_press()
            else:
                selfroom = room.back
                write(f"\nYou walked into {selfroom.name}")
                wait_for_key_press()

    else:
        write(f"\nYou tried to sneak to another room but {room.enemy.name} noticed you")
        sleep(selfsleep)
        attack(room)

def loot(user, loot):
    """main action for user to search the room for loot"""

    # Generate a random number to see if you successfully loot the room whithout the enemy noticing
    caught = False

    if selfroom.enemy != None:
        if user.name == "meow":
            write(f"\n{selfroom.enemy.name} cowers in your presence, granting you access to their domain.")
            sleep(selfsleep)
        else:
            chance = random.randint(1, 3)
            if chance != 1:
                caught = True
            else:
                write(f"\nBy some miracle you managed to loot the room without {selfroom.enemy.name} noticing")
                sleep(selfsleep)

    if not caught:
        # Allow the user to loot the room
        if loot == None:
            write("\nYou searched every nook and cranny but there was nothing to be found")
            wait_for_key_press()
        
        elif loot.name == "Flask of Crimson Tears":
            write(f"\nYou found a {loot.name}, a powerful flask")
            wait_for_key_press()
            user.health_flask += 1
            selfroom.loot = None

        elif loot.name == "Flask of Cerulean Tears":
            write(f"\nYou found a {loot.name}, a powerful flask")
            wait_for_key_press()
            user.mana_flask += 1
            selfroom.loot = None
            
        elif loot.name == "Dectus Medallion (right)":
            write(f"\nYou found a {loot.name}, a powerful item")
            wait_for_key_press()
            user.items.append(loot)
            selfroom.loot = None

        elif loot.name == "Dectus Medallion (left)":
            write(f"\nYou found a {loot.name}, a powerful item")
            wait_for_key_press()
            user.items.append(loot)
            selfroom.loot = None

    else:
        write(f"\n{selfroom.enemy.name} noticed you while you tried to loot the room")
        sleep(selfsleep)
        attack(selfroom)

def flask(user):
    """main action for user to drink their flasks"""
    # Check if the user still has available flasks
    if (user.health_flask + user.mana_flask) == 0:
        write("\nYou ran out of flasks\n")
        wait_for_key_press()
    else:
        use_flask(user)

def attack(room):
    """main action for user to attack the enemy in the room"""
    if room.enemy == None:
        delete()
        write("\nYou attacked the air and realised how insane you looked")
        wait_for_key_press()
        
    else:
        outcome = room.encounter.fight(selfcharacter, root, text)
        if outcome == 1:
            if room.enemy.name == "Voldemort":  
                win(selfcharacter.weapon)
                end_game()
            else:
                drops(room)
            if room.enemy.name == "Sentinels":
                secret_room()
            room.enemy = None
        elif outcome == 2:
            end_game()
        elif outcome == 3:
            room.encounter.reset()

def drops(room):
    """obtains drops from defeated enemy"""
    enemy = room.enemy
    print(enemy.name)
    player = selfcharacter

    if enemy.loot != None:
        write(f"\n{enemy.name} dropped a {enemy.loot.name}")
        sleep(selfsleep)
        choice = get_input(f"\nDo you want to pick {enemy.loot.name}?",["yes","no"],None,False)
        if choice.lower() == "yes":
            collect_loot(player, enemy.loot)
            sleep(selfsleep)
            write(f"\n{enemy.loot.description}")
            sleep(selfsleep)
            
        elif choice.lower() == "no":
            write(f"\nYou left {enemy.loot.name} on the ground and allowed the resourceful rat to steal it")
            sleep(selfsleep)
            
        else:
            write(f"\nYour indecisiveness allowed the resourceful rat to steal the {enemy.loot.name} when you weren't looking")
            sleep(selfsleep)
        wait_for_key_press()
                
def use_flask(user):
    """Function to allow the user to use flask but also allows them to cancel the action"""
    display_stat(user)
    sleep(selfsleep)
    display_flask(user)
    sleep(selfsleep)
    selection = get_input("Which flask would you like to drink? ", ["Flask of Crimson Tears", "Flask of Cerulean Tears", "Cancel"], None, False)
    valid = False
    while not valid:
        valid = True
        # Checks if the user has enough flask of crimson tears
        if selection == "Flask of Crimson Tears" and user.health_flask == 0:
            write("\nYou ran out of Flask of Crimson Tears\n")
            wait_for_key_press()
            delete()
            display_stat(user)
            sleep(selfsleep)
            display_flask(user)
            sleep(selfsleep)
            selection = get_input("Which flask would you like to drink? ", ["Flask of Crimson Tears", "Flask of Cerulean Tears", "Cancel"], None, False)
            valid = False
            
        elif selection == "Flask of Crimson Tears" and user.health == user.max_health:
            write("\nYou do not need to drink a Flask of Crimson Tears\n")
            wait_for_key_press()
            delete()
            display_stat(user)
            sleep(selfsleep)
            display_flask(user)
            sleep(selfsleep)
            selection = get_input("Which flask would you like to drink? ", ["Flask of Crimson Tears", "Flask of Cerulean Tears", "Cancel"], None, False)
            valid = False
            
        # Checks if the user has enough flask of cerulean tears
        elif selection == "Flask of Cerulean Tears" and user.mana_flask == 0:
            write("\nYou ran out of Flask of Cerulean Tears\n")
            wait_for_key_press()
            delete()
            display_stat(user)
            sleep(selfsleep)
            display_flask(user)
            sleep(selfsleep)
            selection = get_input("Which flask would you like to drink? ", ["Flask of Crimson Tears", "Flask of Cerulean Tears", "Cancel"], None, False)
            valid = False

        elif selection == "Flask of Cerulean Tears" and user.mana == user.max_mana:
            write("\nYou do not need to drink a Flask of Cerulean Tears\n")
            wait_for_key_press()
            delete()
            display_stat(user)
            sleep(selfsleep)
            display_flask(user)
            sleep(selfsleep)
            selection = get_input("Which flask would you like to drink? ", ["Flask of Crimson Tears", "Flask of Cerulean Tears", "Cancel"], None, False)
            valid = False

        elif selection.lower() == "Cancel":
            return

    if selection.lower() == "flask of crimson tears":
        # Makes sure the health healed does not exceed the maximum health
        final_health = min(user.max_health, user.health + FlaskOfCrimsonTears().health)
        healing = final_health - user.health
        write(f"\nYou drank a Flask of Crimson Tears and gained {healing} health")
        wait_for_key_press()
        user.health = final_health
        user.health_flask -= 1
        delete()
        use_flask(user)
        
    elif selection.lower() == "flask of cerulean tears":
        # Makes sure the mana gained does not exceed the maximum mana
        final_mana = min(user.max_mana, user.mana + FlaskOfCeruleanTears().mana)
        healing = final_mana - user.mana
        write(f"\nYou drank a Flask of Cerulean Tears and gained {healing} mana")
        wait_for_key_press()
        user.mana = final_mana
        user.mana_flask -= 1
        delete()
        use_flask(user)

def display_stat(user):
    write(f"Health : {user.health} / {user.max_health}")
    write(f"Mana : {user.mana} / {user.max_mana}\n")
        
def equip(self):
    """main action for user to equip various items"""

    display_equipment(selfcharacter)

    decision = get_input("\ndo you want to change your equipment? ", ["yes", "no"], None, False)

    if decision.lower() == "no":
        return

    elif decision.lower() == "yes":
        choice = ""
        while choice != "finish":
            choice = get_input("\nwhat do you want to change?", ["armour", "weapon", "accessory", "finish"], None, False)

            if choice == "armour":
                equip_armour(selfcharacter)

            elif choice.lower() == "weapon":
                equip_weapon(selfcharacter)

            elif choice.lower() == "accessory":
                equip_accessory(selfcharacter)
    
def display_equipment(user):
    """sub action for equip() to display equipments that the user have"""
    
    if user.armour == None:
        write("\nArmour : Empty")
    else:
        write(f"\nArmour : {user.armour.name}")
        
    if user.weapon == None:
        write("Weapon : Empty")
    else:
        write(f"Weapon : {user.weapon.name}")

    if user.accessory == None:
        write("Accessory : Empty")
    else:
        write(f"Accessory : {user.accessory.name}")
    sleep(selfsleep)



def equip_armour(user):
    """sub action from equip() for user to choose an armour to equip"""
    if len(user.armours) == 0:
        write("\nYou do not have any armour to equip")
        wait_for_key_press()
        delete()
        display_equipment(selfcharacter)
    else:
        # Displays the armours the user owns
        write("\nIn your inventory you have: ")
        armours = user.get_armours()
        sleep(selfsleep)
        option = get_input("\nWhich armour do you want to equip?", armours)
        write(f"\nYou equipped {option}")
        wait_for_key_press()
        # Removes the defence increase of the previous armour
        if user.armour != None:
            user.defence = user.defence - user.armour.defence
        armour = user.armours[armours.index(option)]
        # Adds the defence of the new armour
        user.defence = user.defence + armour.defence
        user.armour = armour
        delete()
        display_equipment(user)

def equip_weapon(user):
    """sub action from equip() for user to choose a weapon to equip"""
    # Displays the weapons the user owns
    weapons = user.get_weapons()
    # Validates the user's choice
    option = get_input("\nWhich weapon do you want to equip?", weapons)
    write(f"\nYou equipped {option}")
    wait_for_key_press()
    user.weapon = user.weapons[weapons.index(option)]
    delete()
    display_equipment(user)

def equip_accessory(user):
    """sub action from equip() for user to choose an accessory to equip"""
    if len(user.accessories) == 0:
        write("\nYou do not have any accessories to equip")
        wait_for_key_press()
        delete()
        display_equipment(selfcharacter)
    else:
        accessories = user.get_accessories()
        option = get_input("\nWhich accessory do you want to equip?", accessories)
        write(f"\nYou equipped {option}")
        wait_for_key_press()

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
        accessory = user.accessories[accessories.index(option)]
        user.health += accessory.health_boost
        user.max_health += accessory.health_boost
        user.attack += accessory.attack_boost
        user.mana += accessory.mana_boost
        user.max_mana += accessory.mana_boost
        user.defence += user.accessory.defence_boost
        
        user.accessory = accessory
        delete()
        display_equipment(user)

def status(user):
    """main action that prints user's status"""
    # Displays the users statistics
    write(f"\nName: {user.name}")
    write(f"Health: {user.health} / {user.max_health}")
    write(f"Mana: {user.mana} / {user.max_mana}")
    write(f"Defence: {user.defence}")
    write(f"Strength: {user.attack}")
    wait_for_key_press()

def info(user):
    """main action that prompts user for the type of item to find out more information about"""
    options = ["weapons", "spells", "armours", "accessories", "flasks", "items", "upgrades", "Cancel"]
    choice = get_input("What do you want to find out more about? ", [x.capitalize() for x in options]).lower()

    if choice == "weapons":
        weapon_info(user)

    elif choice == "spells":
        spell_info(user)

    elif choice == "armours":
        armour_info(user)

    elif choice == "accessories":
        accessory_info(user)

    elif choice == "flasks":
        flask_info()

    elif choice == "items":
        item_info(user)

    elif choice == "upgrades":
        upgrade_info(user)

    elif choice == "cancel":
        return
                
def weapon_info(user):
    """sub action from equip() that prompts user for specific weapon to find out more about"""
    # Check if the user owns any weapons
    if len(user.weapons) == 0:
        write("\nYou do not own any weapons yet")
        wait_for_key_press()
        delete()
        info(user)
    
    else:
        # Displays the weapons the user owns
        weapons = user.get_weapons()
        weapons.append("Cancel")
        decision = get_input("\nWhich weapon do you want to find out more about?", weapons)
        if decision == "Cancel":
            delete()
            info(user)
            return
        # Displays the description of the weapon
        write(user.weapons[weapons.index(decision)].description)
        wait_for_key_press()
        delete()
        weapon_info(user)

def spell_info(user):
    """sub action from equip() that prompts user for specific spell to find out more about"""
    # Check if the user knows any spells
    if len(user.spells) == 0:
        write("\nYou do not own any spells yet")
        wait_for_key_press()
        delete()
        info(user)

    else:
        # Displays the spells the user knows
        spells = user.get_spells()
        spells.append("Cancel")

        decision = get_input("\nWhich spell do you want to find out more about?", spells)

        if decision == "Cancel":
            delete()
            info(user)
            return

        # Displays the description of the spell
        write(user.spells[spells.index(decision)].description)
        wait_for_key_press()
        delete()
        spell_info(user)

def armour_info(user):
    """sub action from equip() that prompts user for specific armour to find out more about"""
    # Check if the user owns any armours
    if len(user.armours) == 0:
        write("\nYou do not own any amours yet")
        wait_for_key_press()
        delete()
        info(user)

    else:
        # Displays the armours the user owns
        armours = user.get_armours()
        armours.append("Cancel")

        decision = get_input("\nWhich armour do you want to find out more about?", armours)

        if decision == "Cancel":
            delete()
            info(user)
            return
        # Displays the description of the armour
        write(user.armours[armours.index(decision)].description)
        wait_for_key_press()
        delete()
        armour_info(user)

def accessory_info(user):
    """sub action from equip() that prompts user for specific accessory to find out more about"""
    # Checks if the user owns any accessories
    if len(user.accessories) == 0:
        write("\nYou do not own any accessories yet")
        wait_for_key_press()
        delete()
        info(user)

    else:
        # Displays the accessories the user owns
        accessories = user.get_accessories()
        accessories.append("Cancel")

        decision = get_input("\nWhich accesssory do you want to find out more about?", accessories)

        if decision == "Cancel":
            delete()
            info(user)
            return

        # Displays the description of the accessory
        write(user.accessories[accessories.index(decision)].description)
        wait_for_key_press()
        delete()
        accessory_info(user)

def flask_info():
    """sub action from equip() that prompts user for specific flask to find out more about"""

    decision = get_input("\nWhich accesssory do you want to find out more about?", ["Flask of Crimson Tears", "Flask of Cerulean Tears", "Cancel"])
    if decision.lower() == "flask of crimson tears":
        write(FlaskOfCrimsonTears().description)
        wait_for_key_press()
        delete()
        flask_info()
    elif decision.lower() == "flask of cerulean tears":
        write(FlaskOfCeruleanTears().description)
        wait_for_key_press()
        delete()
        flask_info()
    elif decision == "Cancel":
        delete()
        info(selfcharacter)

def item_info(user):
    """sub action from equip() that prompts user for specific special item to find out more about"""
    # Check if the user owns any items
    if len(user.items) == 0:
        write("\nYou do not own any items yet")
        wait_for_key_press()
        delete()
        info(user)
    else:
        # Displays the items the user owns
        items = user.get_items()
        items.append("Cancel")

        decision = get_input("\nWhich item do you want to find out more about?", items)

        if decision == "Cancel":
            delete()
            info(user)
            return
        # Displays the description of the items
        write(user.items[items.index(decision)].description)
        wait_for_key_press()
        delete()
        item_info(user)

def upgrade_info(user):
    if len(user.upgrades) == 0:
        write("\nYou do not own any upgrades yet")
        wait_for_key_press()
        delete()
        info(user)
    else:
        upgrades = user.get_upgrades()
        upgrades.append("Cancel")

        decision = get_input("\nWhich upgrade do you want to find out more about?", upgrades)

        if decision == "Cancel":
            delete()
            info(user)

        else:
            write(user.upgrades[upgrades.index(decision)].description)
            wait_for_key_press()
            delete()
            upgrade_info(user)
                
def display_room_name():
    """prints the room's name in a cool way"""
    write()
    write("="*25)
    space = " "*int((25-len(selfroom.name))/2)
    write(f"{space}{selfroom.name}{space}")
    write("="*25)

def display_room_description():
    """prints the room's description"""
    write()
    write(selfroom.description)
    sleep(selfsleep)
    look(selfroom)
    selfroom.been_here = True



def collect_loot(attacker, loot):
    """sub method from attack() to collect loot of defeated monster"""
    if loot.type == "weapon":
        attacker.weapons.append(loot)
        write(f"\nYou obtained a {loot.name}, a powerful weapon")
        
    elif loot.type == "spell":
        attacker.spells.append(loot)
        write(f"\nYou obtained a {loot.name}, a powerful spell")

    elif loot.type == "armour":
        attacker.armours.append(loot)
        write(f"\nYou obtained a {loot.name}, a powerful armour")

    elif loot.type == "accessory":
        attacker.accessories.append(loot)
        write(f"\nYou obtained a {loot.name}, a powerful accessory")

    elif loot.type == "upgrade":
        attacker.upgrades.append(loot)
        write(f"\nYou obtained a {loot.name}, a powerful upgrade")
        if loot.name == "Portal Gun":
            selfactions.append("teleport")
            selfdescription.append("Teleport to any room you have been to before")

    sleep(selfsleep)

def end_game():
    global selfend
    """ends the game"""
    selfend = True

def win(weapon):
    """displays scenario when user wins"""
    write(f"\nUsing the almighty {weapon.name}, you struck insert final boss down, crippling him of all his powers and stopping his evil tyranny over the school")
    sleep(selfsleep)
    write(" _____ ___________   _____ _       ___  _____ _   _ ")
    sleep(0.2)
    write("|  __ \  _  |  _  \ /  ___| |     / _ \|_   _| \ | |")
    sleep(0.2)
    write("| |  \/ | | | | | | \ `--.| |    / /_\ \ | | |  \| |")
    sleep(0.2)
    write("| | __| | | | | | |  `--. \ |    |  _  | | | | . ` |")
    sleep(0.2)
    write("| |_\ \ \_/ / |/ /  /\__/ / |____| | | |_| |_| |\  |")
    sleep(0.2)
    write(" \____/\___/|___/   \____/\_____/\_| |_/\___/\_| \_/")
    selfend = True
       
def secret():
    """secret account that gives God like stats by setting name as meow"""
    write("\nWelcome chosen one, the Gods smile upon you and have rained down their blessing")
    wait_for_key_press()
    selfcharacter.health = 999
    selfcharacter.max_health = 999
    selfcharacter.mana = 999
    selfcharacter.max_mana = 999
    selfcharacter.attack = 999
    selfcharacter.defence = 999
    selfcharacter.health_flask = 999
    selfcharacter.mana_flask = 999
    selfcharacter.upgrades.append(Flee())
    selfcharacter.upgrades.append(Shield())
    selfmap.full_reveal()
    selfcharacter.items.append(DectusMedallionLeft())
    selfcharacter.items.append(DectusMedallionRight())

def meow():
    if selfroom.secret == True:
        write("""       
            
   ____ ___  ___  ____ _      __
  / __ `__ \/ _ \/ __ \ | /| / /
 / / / / / /  __/ /_/ / |/ |/ / 
/_/ /_/ /_/\___/\____/|__/|__/  
                               """)
        sleep(selfsleep)
        write("\nYou started communicating with the cat, leading you to discover a hidden passage\n")
        theLastResort = TheLastResort()
        selfroom.back = theLastResort
        theLastResort.forward = selfroom
        selfmap.meow_reveal()
    else:
        choice = random.randint(1, 9)
        if choice == 1:
            write("""  
            
  __  __  U _____ u U  ___ u             
U|' \/ '|u\| ___"|/  \/"_ \/__        __ 
\| |\/| |/ |  _|"    | | | |\"\      /"/ 
 | |  | |  | |___.-,_| |_| |/\ \ /\ / /\ 
 |_|  |_|  |_____|\_)-\___/U  \ V  V /  U
<<,-,,-.   <<   >>     \\  .-,_\ /\ /_,-.
 (./  \.) (__) (__)   (__)  \_)-'  '-(_/ 
                                        """)
        elif choice == 2:
            write("""       
            
   ____ ___  ___  ____ _      __
  / __ `__ \/ _ \/ __ \ | /| / /
 / / / / / /  __/ /_/ / |/ |/ / 
/_/ /_/ /_/\___/\____/|__/|__/  
                               """)

        elif choice == 3:
            write("""                              
                              
 _ __ ___   ___  _____      __
| '_ ` _ \ / _ \/ _ \ \ /\ / /
| | | | | |  __/ (_) \ V  V / 
|_| |_| |_|\___|\___/ \_/\_/  
                              """)

        elif choice == 4:
            write(""" 
            
 _  _  ____  __   _  _ 
( \/ )(  __)/  \ / )( \
/ \/ \ ) _)(  O )\ /\ /
\_)(_/(____)\__/ (_/\_)
                        """)

        elif choice == 5:
            write("""   
            
 _ __ ___   ___  _____      __
| '_ ` _ \ / _ \/ _ \ \ /\ / /
| | | | | |  __/ (_) \ V  V / 
|_| |_| |_|\___|\___/ \_/\_/  
                              """)

        elif choice == 6:
            write("""                                    
                                    
,--,--,--. ,---.  ,---. ,--.   ,--. 
|        || .-. :| .-. ||  |.'.|  | 
|  |  |  |\   --.' '-' '|   .'.   | 
`--`--`--' `----' `---' '--'   '--' 
                                    """)

        elif choice == 7:
            write(""" 
 __    __     ______     ______     __     __    
/\ "-./  \   /\  ___\   /\  __ \   /\ \  _ \ \   
\ \ \-./\ \  \ \  __\   \ \ \/\ \  \ \ \/ ".\ \  
 \ \_\ \ \_\  \ \_____\  \ \_____\  \ \__/".~\_\ 
  \/_/  \/_/   \/_____/   \/_____/   \/_/   \/_/ 
                                                 """)

        elif choice == 8:
            write("""                                        
                                        
 _ .--..--.  .---.   .--.   _   _   __  
[ `.-. .-. |/ /__\\/ .'`\ \[ \ [ \ [  ] 
 | | | | | || \__.,| \__. | \ \/\ \/ /  
[___||__||__]'.__.' '.__.'   \__/\__/   
                                        """)

        elif choice == 9:
            write(""" 
 _      _____ ____  _     
/ \__/|/  __//  _ \/ \  /|
| |\/|||  \  | / \|| |  ||
| |  |||  /_ | \_/|| |/\||
\_/  \|\____\\____/\_/  \|
                          """)
    wait_for_key_press()
    
def settings():
    """Show and change settings"""
    settings = []
    with open("settings.txt", "r") as f:
        settings = f.readlines()
        settings_dict = {}
        for row in settings:
            key, val = row.split()
            settings_dict[key] = val
    choice = ""
    accepted = list(settings_dict.keys())
    accepted.append("finish")
    display_settings(settings_dict)
    while choice != "finish":
        choice = get_input("\nWhich setting do you want to change? (type finish to quit): ", accepted, None, False)

        if choice.lower() == "finish":
            with open("settings.txt", "w") as f:
                for entry in settings_dict:
                    f.write(entry + " " + settings_dict[entry] + "\n")
            return
        
        if choice.lower() == "sleep":
            new = set_sleep(settings_dict["sleep"])
            settings_dict["sleep"] = new

        display_settings(settings_dict)

def display_settings(settings):
    """
    display the settings passed in
    """
    write("\nCurrent Settings:\n")
    for set in settings:
        write(f"{set}: {settings[set]}")

def set_sleep(current):
    global selfsleep
    """
    Change the interval between messages
    returns new value for sleep as string
    """
    count = 0
    write("\nsleep: the interval between messages sent by the game in seconds.")
    write(f"Current value: {current}")
    
    accept = [str(x) for x in range(6)]
    accept.append("cancel")

    new = get_input("\nEnter a new value for sleep (0-5 seconds), or cancel to cancel: ", accept)
    
    if new.lower() == "cancel":
        return current
    else:
        selfsleep = int(new)
        return new
            

def secret_room():
    write("\nAfter you successfully defeated the sentinels, a stray ginger tabby cat emerges from behind a wall and stares at you playfully\n")
    selfroom.secret = True
    wait_for_key_press()

def teleport():
    global selfroom
    rooms = []
    for room in selfrooms:
        rooms.append(room.name)
    rooms.append("Cancel")

    choice = get_input("\nWhich room do you want to teleport to?", rooms)

    if choice == "Cancel":
        return
    else:
        room = selfrooms[rooms.index(choice)]
        write(f"You teleported to {room.name}")
        wait_for_key_press()
        selfroom = room

def display_map():
    """
    Show the map
    """
    
    legend = """Legend:
┌───┐                                   ╭━━━╮
│   │ = Room has unfinished objectives  ┃   ┃ = Fully Cleared Room
└───┘                                   ╰━━━╯
    """
    for row in selfmap.map:
        write("".join(row))
    write(legend)
    wait_for_key_press()
    
if __name__ == "__main__":
    root = tk.Tk()
    pause_var = tk.StringVar()
    pointer = tk.IntVar()
    sleepCount = tk.IntVar()
    root.geometry('1000x600')
    root.configure(bg='black')
    text = tk.Text(root, height = 560, width = 560, background = "black", foreground = "white")
    text.pack()
    text.focus_set()
    root.after(0,intro)
    root.mainloop()
