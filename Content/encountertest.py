#this file is for testing fights and not used in the main game

import Content.character as character
import encounter
import Content.enemy as enemy
import tkinter as tk
from Content.armour import *
from Content.weapon import *
from Content.accessory import *
from Content.spell import *
from Content.shield import *

root = tk.Tk()
pause_var = tk.StringVar()
pointer = tk.IntVar()
sleepCount = tk.IntVar()
root.geometry('1000x600')
root.configure(bg='black')
text = tk.Text(root, height = 560, width = 560, background = "black", foreground = "white")
text.pack()
text.focus_set()

def equip_armour(user, armour):
    # Adds the defence of the new armour
    user.defence = user.defence + armour.defence
    user.armour = armour

def equip_accessory(user, accessory):
    # Adds the stat boost from the new accessory
    user.health += accessory.health_boost
    user.max_health += accessory.health_boost
    user.attack += accessory.attack_boost
    user.mana += accessory.mana_boost
    user.max_mana += accessory.mana_boost
    user.defence += accessory.defence_boost
    user.accessory = accessory

player = character.Character()
player.name = "awpik"
player.health = 200
player.max_health = 200
player.mana = 400
player.max_mana = 400
player.attack = 0

player.armours.append(OrnatePlate())
player.weapons.append(Zenith())
player.accessories.append(GoldenFeather())
player.spells.append(WingardiumLeviosa())
player.spells.append(VengefulSpirit())
player.spells.append(Megidolaon())
player.spells.append(WillOTheWisp())

player.weapon = Zenith()

armour = PowerSuit()
equip_armour(player, armour)

accessory = GoldenFeather()
equip_accessory(player, accessory)

shield = HylianShield()
player.shield = shield

player.health_flask = 20
player.mana_flask = 20

fight = encounter.glados_fight(enemy.Glados())
fight.fight(player, root, text)
