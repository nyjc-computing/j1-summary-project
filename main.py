#import from python built in libraries
import time
import random

#import from other files
from setup import *
import tkinter as tk
import map
import encounter
import Content.enemy as enemy
import Content.games as games

temp = setup()
selfend = False
selfroom = temp[0]
selfcharacter = temp[1]
selfrooms = []
selfactions = ["Look", "Move", "Attack", "Loot", "Flask", "Equip", "Status", "Information", "Item", "Settings", "Map", "Meow", "Help"]
selfdescription = ["Looks around the room","Move to another room", "Attack the enemny", "Search the room for loot", "Drink your flasks", "Change your equipment", "See your statistics", "Find out more about your items", "Use your item", "Change settings", "Shows map", "Meow"]
selfmap = map.game_map()
currentPressedKey = ""
out = []
with open("settings.txt", "r") as f:
    out = f.readlines()
    out = [x.split()[1] for x in out]
selfsleep = int(out[0])
selfup = out[2]
selfdown = out[3]
selfreturn = out[4]
selfsaveroom = None
selfcompletion = 0

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
        root.bind(f'<{selfreturn}>', lambda x: pause_var.set("done"))
        root.wait_variable(pause_var)
        root.unbind(f'<{selfreturn}>')
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
            write("You boldly opened the front gates of the school and made your way into the first room")
            wait_for_key_press()
            root.after(selfsleep*1000, run)
            
    elif decision.lower() == "no":
        write("Due to your utter cowardice, voldemort continued to gain power, spreading his control and chaos all over the world, leading to the complete annihilation of the human race.")
        write("__   _______ _   _  ______ _____ ___________")
        sleep(0.2)
        write("\ \ / /  _  | | | | |  _  \_   _|  ___|  _  \\")
        sleep(0.2)
        write(" \ V /| | | | | | | | | | | | | | |__ | | | |")
        sleep(0.2)
        write("  \ / | | | | | | | | | | | | | |  __|| | | |")
        sleep(0.2)
        write("  | | \ \_/ / |_| | | |/ / _| |_| |___| |/ /")
        sleep(0.2)
        write("  \_/  \___/ \___/  |___/  \___/\____/|___/ ")
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
    root.bind(f'<{selfreturn}>', lambda x: pause_var.set("done"))
    root.bind(f"<{selfup}>", lambda e: up_action(prompt, displayoptions, deletebefore))
    root.bind(f"<{selfdown}>", lambda e: down_action(prompt, displayoptions, deletebefore))
    root.wait_variable(pause_var)
    root.unbind(f'<{selfreturn}>')
    root.unbind(f"<{selfup}>")
    root.unbind(f"<{selfdown}>")
    pause_var.set("")
    decision = options[pointer.get()]
    pointer.set(0)
    delete()
    return decision

        
def run():
    global selfroom
    global selfend
    global selfcompletion
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

    if "Save" not in selfactions and selfroom.save and selfroom.enemy == None:
        selfactions.insert(-1, "Save")
        selfdescription.append("Saves the game")
    elif "Save" in selfactions and not selfroom.save:
        selfactions.remove("Save")
        selfdescription.remove("Saves the game")

    if "Shop" not in selfactions and selfcharacter.shop and selfroom.name == "The Forge":
        selfactions.insert(-1, "Shop")
        selfdescription.append("Buy stuff from the shop")
    elif "Shop" in selfactions and selfroom.name != "The Forge":
        selfactions.remove("Shop")
        selfdescription.remove("Buy stuff from the shop")

    if "Gamble" not in selfactions and selfroom.name == "Kamurocho" and selfcharacter.gamble:
        selfactions.insert(-1, "Gamble")
        selfdescription.append("Go to the Underground Casino")
    elif "Gamble" in selfactions and selfroom.name != "Kamurocho":
        selfactions.remove("Gamble")
        selfdescription.remove("Go to the Underground Casino")
        
    decision = get_input("What do you wish to do?", selfactions)

    # Does the action the user selected

    if decision.lower() == "look":
        display_room_name()
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

    elif decision.lower() == "help":
        help()

    elif decision.lower() == "save":
        save()

    elif decision.lower() == "item":
        item()

    elif decision.lower() == "shop":
        shop()

    elif decision.lower() == "gamble":
        gamble()

    if selfroom.enemy == None and selfroom.loot == None and not selfroom.secret and not selfroom.complete:
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
        selfcompletion += 1
        selfroom.complete = True

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
            write(f"\nThere is a {room.loot.name} hidden in {room.name}")
            sleep(selfsleep)
        else:
            write(f"\nThere is no loot hidden in {room.name}")
            sleep(selfsleep)
        
    elif room.enemy != None:
    # Displays the enemy in the room
        write(f"\nIn the middle of the room is {room.enemy.name}, {room.enemy.description}")

    if room.enemy == None and room.save:
        write(f"\n{room.save_text}")
        
    if room.name == "The Forge":
        if room.enemy == None and room.secret and selfcharacter.shop:
            write(f"\n{room.secret_message}")

    elif room.enemy == None and room.secret:
        write(f"\n{room.secret_message}")
    wait_for_key_press()

def move(room):
    global selfroom
    """main action for user to traverse from one room to another"""
    movement = get_input('Which direction do you wish to move in?', ['Left', 'Right', 'Forward','Back'])

    # Generate a random number to see if you managed to sneak past the enemy
    caught = False
    upgrades = selfcharacter.get_upgrades()
    
    if room.enemy != None:
        if "Smoke Bombs" in upgrades:
            write(f"\nYou used your Smoke Bombs to sneak past {room.enemy.name}")
            sleep(selfsleep)
        
        elif selfcharacter.name == "meow":
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
        wait_for_key_press()
        attack(room)

def loot(user, loot):
    """main action for user to search the room for loot"""

    # Generate a random number to see if you successfully loot the room whithout the enemy noticing
    caught = False
    upgrades = user.get_upgrades()

    if selfroom.enemy != None:
        if "Smoke Bombs" in upgrades:
            write(f"\nYou used your Smoke Bombs to loot the room without being caught by {selfroom.enemy.name}")
            sleep(selfsleep)
        
        elif user.name == "meow":
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
            
        elif loot.type == "item":
            write(f"\nYou found a {loot.name}, a powerful item")
            wait_for_key_press()
            user.items.append(loot)
            selfroom.loot = None

    else:
        write(f"\n{selfroom.enemy.name} noticed you while you tried to loot the room")
        sleep(selfsleep)
        wait_for_key_press()
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
    global selfend
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
                selfend = True
                return
            else:
                drops(room)
                money(room)
                if selfroom.save == True:
                    delete()
                    write()
                    write(selfroom.save_text)
                    choice = get_input("\nDo you wish to save?", ["Yes", "No"], None, False)
                    if choice == "Yes":
                        save()
            if room.enemy.name == "Sentinels":
                room.secret = True
                delete()
                write()
                write("After you successfully defeated the sentinels, a stray ginger tabby cat emerges from behind a wall and stares at you playfully")
                wait_for_key_press()
            elif room.enemy.name == "The Hollow Knight":
                room.secret = True
                delete()
                write()
                write(room.secret_message)
                wait_for_key_press()
            elif room.enemy.name == "The Radiance":
                room.secret = False

            elif room.enemy.name == "Ganondorf":
                room.secret = True
                delete()
                write()
                write(room.secret_message)
                wait_for_key_press()

            elif room.enemy.name == "Calamity Ganon":
                room.secret = False

            elif room.enemy.name == "Bowser":
                room.secret = True
                delete()
                write()
                write(room.secret_message)
                wait_for_key_press()

            elif room.enemy.name == "Shibusawa":
                room.secret = True
                delete()
                write()
                write(room.secret_message)
                wait_for_key_press()
                
            room.enemy = None
        elif outcome == 2:
            room.encounter.reset()
            end_game()
        elif outcome == 3:
            wait_for_key_press()
            room.encounter.reset()

def drops(room):
    """obtains drops from defeated enemy"""
    enemy = room.enemy
    player = selfcharacter

    if enemy.loot != None:
        write(f"\n{enemy.name} dropped a {enemy.loot.name}")
        sleep(selfsleep)
        choice = get_input(f"\nDo you want to pick up {enemy.loot.name}?",["Yes","No"],None,False)
        if choice.lower() == "yes":
            collect_loot(player, enemy.loot)
            sleep(selfsleep)
            write(f"\n{enemy.loot.description}")
            wait_for_key_press()
            
        elif choice.lower() == "no":
            write(f"\nYou left {enemy.loot.name} on the ground and allowed the resourceful rat to steal it")
            wait_for_key_press()

def money(room):
    if room.enemy.money != 0:
        delete()
        write(f"\nYou gained {room.enemy.money} runes from defeating {room.enemy.name}")
        sleep(selfsleep)
        selfcharacter.money += room.enemy.money
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

def display_flask(user):
    write(f"Flask of Crimson Tears : {user.health_flask}")
    write(f"Flask of Cerulean Tears : {user.mana_flask}")
    write("")
        
def equip(self):
    """main action for user to equip various items"""

    display_equipment(selfcharacter)
    if len(selfcharacter.get_shields()) == 0:
        options = ["Armour", "Weapon", "Accessory", "Finish"]
    else:
        options = ["Armour", "Weapon", "Accessory", "Shield", "Finish"]
    choice = ""
    while choice != "Finish":
        choice = get_input("\nwhat do you want to change?", options, None, False)

        if choice == "Armour":
            equip_armour(selfcharacter)

        elif choice == "Weapon":
            equip_weapon(selfcharacter)

        elif choice == "Accessory":
            equip_accessory(selfcharacter)

        elif choice == "Shield":
            equip_shield(selfcharacter)
    
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

    if len(user.get_shields()) > 0:
        if user.shield == None:
            write("Shield : Empty")
        else:
            write(f"Shield : {user.shield.name}")

def equip_armour(user):
    """sub action from equip() for user to choose an armour to equip"""
    if len(user.armours) == 0:
        write("\nYou do not have any armour to equip")
        wait_for_key_press()
        delete()
        display_equipment(selfcharacter)
    else:
        # Displays the armours the user owns
        armours = user.get_armours()
        armours.append("Cancel")
        option = get_input("\nWhich armour do you want to equip?", armours)
        if option == "Cancel":
            display_equipment(user)

        else:
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
    weapons.append("Cancel")
    # Validates the user's choice
    option = get_input("\nWhich weapon do you want to equip?", weapons)
    if option == "Cancel":
        display_equipment(user)
    else:
        write(f"\nYou equipped {option}")
        wait_for_key_press()
        user.weapon = user.weapons[weapons.index(option)]
        delete()
        display_equipment(user)

def equip_shield(user):
    """sub action from equip() for user to choose a weapon to equip"""
    # Displays the weapons the user owns
    shields = user.get_shields()
    shields.append("Cancel")
    # Validates the user's choice
    option = get_input("\nWhich shield do you want to equip?", shields)
    if option == "Cancel":
        display_equipment(user)
    else:
        write(f"\nYou equipped {option}")
        wait_for_key_press()
        user.shield = user.shields[shields.index(option)]
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
        accessories.append("Cancel")
        option = get_input("\nWhich accessory do you want to equip?", accessories)
        if option == "Cancel":
            display_equipment(user)

        else:
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
            user.defence += accessory.defence_boost
            
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
    write(f"Runes : {user.money}")
    write(f"Completion : {int((selfcompletion/28)*100)}%")
    wait_for_key_press()

def info(user):
    """main action that prompts user for the type of item to find out more information about"""
    if len(user.shields) == 0:
        options = ["weapons", "spells", "armours", "accessories", "flasks", "items", "upgrades", "Cancel"]
    else:
        options = ["weapons", "shields", "spells", "armours", "accessories", "flasks", "items", "upgrades", "Cancel"]
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

    elif choice == "shields":
        shield_info(user)
                
def weapon_info(user):
    """sub action from equip() that prompts user for specific weapon to find out more about"""
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

def shield_info(user):
    """sub action from equip() that prompts user for specific weapon to find out more about"""
    # Check if the user owns any weapons
    shields = user.get_shields()
    if len(shields) == 0:
        write("\nYou do not own any weapons yet")
        wait_for_key_press()
        delete()
        info(user)
    
    else:
        # Displays the weapons the user owns
        shields.append("Cancel")
        decision = get_input("\nWhich shield do you want to find out more about?", shields)
        if decision == "Cancel":
            delete()
            info(user)
            return
        # Displays the description of the weapon
        write(user.shields[shields.index(decision)].description)
        wait_for_key_press()
        delete()
        shield_info(user)

def spell_info(user):
    """sub action from equip() that prompts user for specific spell to find out more about"""
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
            selfactions.insert(-1, "Teleport")
            selfdescription.append("Teleport to any room you have been to before")

    elif loot.type == "item":
        attacker.items.append(loot)
        write(f"\nYou obtained a {loot.name}, an item")

    elif loot.type == "shield":
        attacker.shields.append(loot)
        write(f"\nYou obtained a {loot.name}, a powerful shield")

    sleep(selfsleep)

def end_game():
    global selfend
    global selfroom

    if selfsaveroom != None:
        choice = get_input("\nDo you want to respawn?", ["Yes", "No"], None, False)
        if choice == "Yes":
            write(f"You respawned in {selfsaveroom.name}")
            selfcharacter.health = selfcharacter.max_health
            selfcharacter.mana = selfcharacter.max_mana
            wait_for_key_press()
            selfroom = selfsaveroom
        else:
            selfend = True

    else:
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
    if selfcompletion == 28:
        write()
        write("Thanks for putting in the effort to 100% the game, hope you enjoyed playing :)")
        sleep(self.sleep)
    wait_for_key_press()
    delete()
    write()
    write("Credits")
    write()
    write("Programmers:")
    write("Noah Lee")
    write("Ethan Tse")
    write("Brydon Ti")
    write()
    write("Play testers:")
    write("Ming Cong")
    write("Ling Kai")
    write("Jae Zen")
    write("Vincent Tse")
    write("Yi Heng")
    write("Josiah Lin")

    write()
    write("Special thanks to Mr Ng for providing us the opportunity to code this game")
    
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
    selfcharacter.money = 999
    #selfcharacter.upgrades.append(ShadeCloak())
    #selfcharacter.upgrades.append(Shield())
    selfmap.full_reveal()
    selfcharacter.items.append(DectusMedallionLeft())
    selfcharacter.items.append(DectusMedallionRight())
    selfcharacter.items.append(MementoMortem())
    #selfcharacter.upgrades.append(PortalGun())
    #selfcharacter.upgrades.append(VirtualBoo())
    selfcharacter.items.append(BlackBox())
    selfcharacter.items.append(RustyKey())
    selfcharacter.items.append(RoboticArm())
    selfcharacter.items.append(ScotchWhiskey())
    selfactions.insert(-1, "Teleport")

def meow():
    if selfroom.secret == True and selfroom.name == "Walled City 99":
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
        selfroom.secret = False
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
    display_settings(settings_dict)
    while choice != "finish":
        choice = get_input("\nWhich setting do you want to change?", ["Sleep", "Music", "Controls", "Finish"], None, False)

        if choice.lower() == "music":
            new = set_music(settings_dict["Music"])
            settings_dict["Music"] = new

        if choice.lower() == "finish":
            with open("settings.txt", "w") as f:
                for entry in settings_dict:
                    f.write(entry + " " + settings_dict[entry] + "\n")
            return
        
        if choice.lower() == "sleep":
            new = set_sleep(settings_dict["Sleep"])
            settings_dict["Sleep"] = new

        elif choice.lower() == "controls":
            set_controls()
            settings_dict["Up"] = selfup
            settings_dict["Down"] = selfdown
            settings_dict["Enter"] = selfreturn

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

    write("\nsleep: the interval between messages sent by the game in seconds.")
    write(f"Current value: {current}")
    
    accept = [str(x) for x in range(6)]
    accept.append("cancel")

    new = get_input("\nEnter a new value for sleep", accept)
    
    if new.lower() == "cancel":
        return current
    else:
        selfsleep = int(new)
        return new
    
def set_music(current):

    new = get_input("\nMusic: ", ["On", "Off", "Cancel"])
    
    if new.lower() == "cancel":
        return current
    else:
        return new

def set_controls():
    choice = get_input("\nWhich control do you want to change?", ["Up", "Down", "Enter", "Finish"])

    if choice == "Up":
        write("\nPress the key you want to change for scrolling up")
        root.bind("<Key>", change_up)
        root.wait_variable(pause_var)
        pause_var.set("")
        root.unbind("<Key>")
        delete()

    elif choice == "Down":
        write("\nPress the key you want to change for scrolling down")
        root.bind("<Key>", change_down)
        root.wait_variable(pause_var)
        pause_var.set("")
        root.unbind("<Key>")
        delete()

    elif choice  == "Enter":
        write("\nPress the key you want to change for selecting options")
        root.bind("<Key>", change_enter)
        root.wait_variable(pause_var)
        pause_var.set("")
        root.unbind("<Key>")
        delete()        

    elif choice == "Cancel":
        return

def change_up(e):
    global selfup
    if e.keysym == selfdown or e.keysym == selfreturn:
        delete()
        write(f"'{e.keysym}' is already binded to another control")
        wait_for_key_press()
    else:
        selfup = e.keysym
    pause_var.set("done")

def change_down(e):
    global selfdown
    if e.keysym == selfup or e.keysym == selfreturn:
        delete()
        write(f"'{e.keysym}' is already binded to another control")
        wait_for_key_press()
    else:
        selfdown = e.keysym
    pause_var.set("done")

def change_enter(e):
    global selfreturn
    if e.keysym == selfup or e.keysym == selfdown:
        delete()
        write(f"'{e.keysym}' is already binded to another control")
        wait_for_key_press()
    else:
        selfreturn = e.keysym
    pause_var.set("done")

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

def help():
    for i in range(len(selfdescription)):
        write(f"{selfactions[i]} : {selfdescription[i]}")
    wait_for_key_press()

def save():
    global selfsaveroom
    selfsaveroom = selfroom
    selfcharacter.health = selfcharacter.max_health
    selfcharacter.mana = selfcharacter.max_mana
    write(selfroom.save_message)
    wait_for_key_press()

def item():
    items = selfcharacter.get_items()

    if len(items) == 0:
        write("You do not own any items")
        wait_for_key_press()

    else:
        items.append("Cancel")
        choice = get_input("Which item do you want to use?", items)

        if choice == "Cancel":
            return
    
        elif choice == "Memento Mortem" and selfroom.name == "Dirtmouth" and selfroom.secret:
            write("You used the Memento Mortem on the empty vessel, transporting you to the past where you face The Radiance, The source of the infection in Hallownest")
            wait_for_key_press()
            secret_attack(enemy.TheRadiance())

        elif choice == "Black Box" and selfroom.name == "Hyrule Kingdom" and selfroom.secret:
            write("You activated the Black Box, breaking a hole in the ground, Calamity Ganon, a dark, amorphous, and monstrous entity, then crawls out of the hole")
            wait_for_key_press()
            secret_attack(enemy.CalamityGanon())
        
        elif choice == "Rusty Key" and selfroom.name == "The Mushroom Kingdom" and selfroom.secret:
            write("You used the Rusty Key to free the Robot")
            sleep(selfsleep)
            write()
            write("The robot thanks you for saving him and asks you to meet him in The Forge")
            wait_for_key_press()
            selfroom.secret = False
            selfcharacter.shop = True
            selfcharacter.items.pop(items.index(choice))

        elif choice == "Robotic Arm" and selfroom.name == "The Forge" and selfroom.secret and selfroom.secret_message == "You notice that Ox is missing his left arm":
            write("You gave the Robotic Arm to Ox")
            sleep(selfsleep)
            write()
            write("Ox thanks you tremendously as its a perfect fit for him")
            sleep(selfsleep)
            write()
            write("There are new items you can purchase from the store now")
            wait_for_key_press()
            selfcharacter.shop_inventory.append(SmokeBombs())
            selfroom.secret = False
            selfcharacter.items.pop(items.index(choice))

        elif choice == "Scotch Whiskey" and selfroom.name == "Kamurocho" and selfroom.secret:
            write("You gave the drunk man the bottle of Scotch Whiskey")
            sleep(selfsleep)
            write()
            write("The man then led you to an underground Casino")
            wait_for_key_press()
            delete()
            gamble()
            selfcharacter.gamble = True
            selfcharacter.items.pop(items.index(choice))
            selfroom.secret = False
            
    
        else:
            write(f"You used {choice} but nothing happened")
            wait_for_key_press()

def secret_attack(boss):
    secret = encounter.encounter(boss)
    outcome = secret.fight(selfcharacter, root, text)

    if outcome == 1:
        write(f"\n{boss.name} dropped a {boss.loot.name}")
        sleep(selfsleep)
        choice = get_input(f"\nDo you want to pick up {boss.loot.name}?",["Yes","No"],None,False)
        if choice.lower() == "yes":
            collect_loot(selfcharacter, boss.loot)
            sleep(selfsleep)
            write(f"\n{boss.loot.description}")
            wait_for_key_press()
    
        elif choice.lower() == "no":
            write(f"\nYou left {boss.loot.name} on the ground and allowed the resourceful rat to steal it")
            wait_for_key_press()

        selfroom.secret = False

    elif outcome == 2:
        selfroom.encounter.reset()
        end_game()
        
    elif outcome == 3:
        selfroom.encounter.reset()

def shop():
    if selfroom.secret_message == "The Robot has set up a shop in The Forge":
        write("The robot introduces himself as Ox")
        write()
        write("You notice that Ox is missing his left arm")
        selfroom.secret_message = "You notice that Ox is missing his left arm"
    items = selfcharacter.shop_inventory.copy()

    if len(items) == 0:
        write("You bought out everything in the store")
        wait_for_key_press()
        return

    display = []
    for item in items:
        display.append(f"{item.name} ({item.cost} runes)")
    items.append("Finish")
    display.append("Finish")

    write()
    choice = get_input(f"Which item would you like to purchase? (You have {selfcharacter.money} runes)", items, display, False)

    if choice == "Finish":
        return
    else:
        if selfcharacter.money < choice.cost:
            write(f"You do not have enough runes to buy {choice.name}")
            wait_for_key_press()
        else:
            write(f"You bought {choice.name}, a {choice.type}")
            sleep(selfsleep)
            write()
            write(choice.description)
            wait_for_key_press()
            if choice.type == "item":
                selfcharacter.items.append(choice)
            elif choice.type == "upgrade":
                selfcharacter.upgrades.append(choice)
            selfcharacter.money -= choice.cost
            selfcharacter.shop_inventory.pop(items.index(choice))
        delete()
        shop()

def gamble():
    write("You step into a vibrant and bustling establishment of lavish and extravagant design, with neon lights and flashy signage")

    advance = False
    while not advance:
        choice = get_input(f"Which game would you like to play? (You have {selfcharacter.money} runes)", ["Jan Ken Pon", "Blackjack", "Slots", "Finish"], None, False)
    
        if choice == "Finish":
            advance = True
        elif choice == "Jan Ken Pon":
            if selfcharacter.money == 0:
                write("Sorry you do not have any runes to gamble")
                delete()
            else:
                games.JanKenPon(selfcharacter, root, text).play()

        elif choice == "Blackjack":
            if selfcharacter.money == 0:
                write("Sorry you do not have any runes to gamble")
                delete()
            else:
                games.Blackjack(selfcharacter, root, text).play()

        elif choice == "Slots":
            if selfcharacter.money == 0:
                write("Sorry you do not have any runes to gamble")
                delete()
            else:
                games.Slots(selfcharacter, root, text).play()
                
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
