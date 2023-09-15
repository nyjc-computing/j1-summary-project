# importing from other files
from Content.room import *
from Content.character import *
from Content.weapon import *
from Content.spell import *
from Content.item import *
from Content.upgrade import *

def link_left(room1, room2):
    room1.left = room2
    room2.right = room1

def link_right(room1, room2):
    room1.right = room2
    room2.left = room1

def link_forward(room1, room2):
    room1.forward = room2
    room2.back = room1

def link_back(room1, room2):
    room1.back = room2
    room2.forward = room1

def setup(load=False) -> [Room, Character]:
    """
    Generates the map and the character and returns it in a list
    """

    character = Character()

    zebes = Zebes()
    kingdomOfKu = KingdomOfKu()
    bunker = Bunker()
    greenhillZone = GreenhillZone()
    theMushroomKingdom = TheMushroomKingdom()
    asphodel = Asphodel()
    commencement = Commencement()
    walledCity99 = WalledCity99()
    mementos = Mementos()
    shoresOfNine = ShoresOfNine()
    theForge = TheForge()
    midgar = Midgar()
    dirtmouth = Dirtmouth()
    theEndDimension = TheEndDimension()
    theShriekingShack = TheShriekingShack()
    hyruleKingdom = HyruleKingdom()
    celestialResort = CelestialResort()
    ascent = Ascent()
    sixthCircleOfHell = SixthCircleOfHell()
    towerOfFate = TowerOfFate()
    miquellasHaligtree = MiquellasHaligtree()
    theHallow = TheHallow()
    theObraDinn = TheObraDinn()
    kamurocho = Kamurocho()
    snowdin = Snowdin()
    theAstralPlane = TheAstralPlane()
    apertureLab = ApertureLab()
    theSealedTemple = TheSealedTemple()

    enemies = {TheRadiance().get_save_name() : TheRadiance(),
               TheHollowKnight().get_save_name() : TheHollowKnight(),
               MrOshiro().get_save_name() : MrOshiro(),
               TheHighDragun().get_save_name() : TheHighDragun(),
               Malenia().get_save_name() : Malenia(),
               Glados().get_save_name() : Glados(),
               Yaldabaoth().get_save_name() : Yaldabaoth(),
               Ridley().get_save_name() : Ridley(),
               Emil().get_save_name() : Emil(),
               TheBoneHyrda().get_save_name() : TheBoneHyrda(),
               GeneralMugen().get_save_name() : GeneralMugen(),
               DoctorEggman().get_save_name() : DoctorEggman(),
               TheMoonLord().get_save_name() : TheMoonLord(),
               Mithrix().get_save_name() : Mithrix(),
               Sephiroth().get_save_name() : Sephiroth(),
               Ganondorf().get_save_name() : Ganondorf(),
               TheEnderDragon().get_save_name() : TheEnderDragon(),
               Shibusawa().get_save_name() : Shibusawa(),
               Enchantress().get_save_name() : Enchantress(),
               Freya().get_save_name() : Freya(),
               Reyna().get_save_name() : Reyna(),
               Voldemort().get_save_name() : Voldemort(),
               Gabriel().get_save_name() : Gabriel(),
               Papyrus().get_save_name() : Papyrus(),
               TheHeir().get_save_name() : TheHeir(),
               JenaAnderson().get_save_name() : JenaAnderson(),
               TheKraken().get_save_name() : TheKraken(),
               Bowser().get_save_name() : Bowser(),
               Sentinel().get_save_name() : Sentinel(),
               KingBoo().get_save_name() : KingBoo(),
               Dio().get_save_name() : Dio(),
               CalamityGanon().get_save_name() : CalamityGanon()}


    rooms = {zebes.get_save_name() : zebes, 
             kingdomOfKu.get_save_name() : kingdomOfKu, 
             bunker.get_save_name() : bunker, 
             greenhillZone.get_save_name() : greenhillZone, 
             theMushroomKingdom.get_save_name() : theMushroomKingdom, 
             asphodel.get_save_name() : asphodel, 
             commencement.get_save_name() : commencement, 
             walledCity99.get_save_name() : walledCity99, 
             mementos.get_save_name() : mementos, 
             shoresOfNine.get_save_name() : shoresOfNine, 
             theForge.get_save_name() : theForge, 
             midgar.get_save_name() : midgar, 
             dirtmouth.get_save_name() : dirtmouth, 
             theEndDimension.get_save_name() : theEndDimension, 
             theShriekingShack.get_save_name() : theShriekingShack, 
             hyruleKingdom.get_save_name() : hyruleKingdom, 
             celestialResort.get_save_name() : celestialResort, 
             ascent.get_save_name() : ascent, 
             sixthCircleOfHell.get_save_name() : sixthCircleOfHell, 
             towerOfFate.get_save_name() : towerOfFate, 
             miquellasHaligtree.get_save_name() : miquellasHaligtree, 
             theHallow.get_save_name() : theHallow, 
             theObraDinn.get_save_name() : theObraDinn, 
             kamurocho.get_save_name() : kamurocho, 
             snowdin.get_save_name() : snowdin, 
             theAstralPlane.get_save_name() : theAstralPlane, 
             theSealedTemple.get_save_name() : theSealedTemple}
    
    loots = {FlaskOfCrimsonTears().get_save_name() : FlaskOfCeruleanTears(),
             FlaskOfCeruleanTears().get_save_name() : FlaskOfCeruleanTears(),
             DectusMedallionLeft().get_save_name() : DectusMedallionLeft(),
             DectusMedallionRight().get_save_name() : DectusMedallionRight(),
             RustyKey().get_save_name() : RustyKey(),
             BlackBox().get_save_name() : BlackBox(),
             RoboticArm().get_save_name() : RoboticArm()}
    
    spells = {WingardiumLeviosa().get_save_name() : WingardiumLeviosa(),
              VengefulSpirit().get_save_name() : VengefulSpirit(),
              Megidolaon().get_save_name() : Megidolaon(),
              GlintstoneCometshard().get_save_name() : GlintstoneCometshard(),
              WillOTheWisp().get_save_name() : WillOTheWisp()}
    
    armours = {NetheriteArmour().get_save_name() : NetheriteArmour(),
               OrnatePlate().get_save_name() : OrnatePlate(),
               PowerSuit().get_save_name() : PowerSuit(),
               DragonMail().get_save_name() : DragonMail(),
               Cappy().get_save_name() : Cappy()}
    
    weapons = {BusterSword().get_save_name() : BusterSword(),
               MasterSword().get_save_name() : MasterSword(),
               LeviathanAxe().get_save_name() : LeviathanAxe(),
               VirtuousTreaty().get_save_name() : VirtuousTreaty(),
               Coronacht().get_save_name() : Coronacht(),
               Zenith().get_save_name() : Zenith(),
               RGXButterflyKnife().get_save_name() : RGXButterflyKnife(),
               Wand().get_save_name() : Wand(),
               MarksmanRevolver().get_save_name() : MarksmanRevolver(),
               ToyKnife().get_save_name() : ToyKnife(),
               XBaton().get_save_name() : XBaton()}
    
    accessories = {GoldenFeather().get_save_name() : GoldenFeather(),
                   MasterRound().get_save_name() : MasterRound(),
                   DragonAmulet().get_save_name() : DragonAmulet(),
                   ChaosEmerald().get_save_name() : ChaosEmerald(),
                   HolyCross().get_save_name() : HolyCross()}
    
    shields = {HylianShield().get_save_name() : HylianShield()}

    items = {DectusMedallionLeft().get_save_name() : DectusMedallionLeft(),
             DectusMedallionRight().get_save_name() : DectusMedallionRight(),
             RustyKey().get_save_name() : RustyKey(),
             MementoMortem().get_save_name() : MementoMortem(),
             BlackBox().get_save_name() : BlackBox(),
             ScotchWhiskey().get_save_name() : ScotchWhiskey(),
             RoboticArm().get_save_name() : RoboticArm()}
    
    upgrades = {VirtualBoo().get_save_name() : VirtualBoo(),
                PortalGun().get_save_name() : PortalGun(),
                ShadeCloak().get_save_name() : ShadeCloak(),
                SmokeBombs().get_save_name() : SmokeBombs()}
    
    shops = {ScotchWhiskey().get_save_name() : ScotchWhiskey(),
             SmokeBombs().get_save_name() : SmokeBombs()}
    
    '''
    room_stats = []
    stats = []

    stats.append(["name", character.name])
    stats.append(["health", str(character.health)])
    stats.append(["max_health", str(character.max_health)])

    if len(character.spells) == 0:
            stats.append(["spells", "None"])
    else:
        temp = ""
        for spell in character.spells:
            temp += spell.get_save_name()
            temp += " "
        stats.append(["spells", temp])

    stats.append(["attack", str(character.attack)])
    stats.append(["mana", str(character.mana)])
    stats.append(["max_mana", str(character.max_mana)])
    stats.append(["defence", str(character.defence)])

    if character.armour == None:
        stats.append(["armour", "None"])
    else:
        stats.append(["armour", character.armour.get_save_name()])

    if len(character.armours) == 0:
            stats.append(["armours", "None"])
    else:
        temp = ""
        for armour in character.armours:
            temp += armour.get_save_name()
            temp += " "
        stats.append(["armours", temp])

    if character.weapon == None:
        stats.append(["weapon", "None"])
    else:
        stats.append(["weapon", character.weapon.get_save_name()])

    if len(character.weapons) == 0:
            stats.append(["weapons", "None"])
    else:
        temp = ""
        for weapon in character.weapons:
            temp += weapon.get_save_name()
            temp += " "
        stats.append(["weapons", temp])

    if character.accessory == None:
        stats.append(["accessory", "None"])
    else:
        stats.append(["accessory", character.accessory.get_save_name()])

    if len(character.accessories) == 0:
            stats.append(["accessories", "None"])
    else:
        temp = ""
        for accessory in character.accessories:
            temp += accessory.get_save_name()
            temp += " "
        stats.append(["accessories", temp])
    
    stats.append(["health_flask", str(character.health_flask)])
    stats.append(["mana_flask", str(character.mana_flask)])

    if len(character.items) == 0:
            stats.append(["items", "None"])
    else:
        temp = ""
        for item in character.items:
            temp += item.get_save_name()
            temp += " "
        stats.append(["items", temp])

    if len(character.upgrades) == 0:
            stats.append(["upgrades", "None"])
    else:
        temp = ""
        for upgrade in character.upgrades:
            temp += upgrade.get_save_name()
            temp += " "
        stats.append(["upgrades", temp])

    if character.shield == None:
        stats.append(["shield", "None"])
    else:
        stats.append(["shield", character.shield.get_save_name()])

    if len(character.shields) == 0:
            stats.append(["shields", "None"])
    else:
        temp = ""
        for shield in character.shields:
            temp += shield.get_save_name()
            temp += " "
        stats.append(["shields", temp])

    stats.append(["money", str(character.money)])

    if character.shop:
        stats.append(["shop", "True"])
    else:
        stats.append(["shop", "False"])

    if len(character.shop_inventory) == 0:
            stats.append(["shop_inventory", "None"])
    else:
        temp = ""
        for item in character.shop_inventory:
            temp += item.get_save_name()
            temp += " "
        stats.append(["shop_inventory", temp])

    if character.gamble:
        stats.append(["gamble", "True"])
    else:
        stats.append(["gamble", "False"])

    with open("save.txt", "w") as f:
        f.write("Save True\n\n")
        f.write(f"Rooms {' '.join(room_names)}\n\n")
        f.write("Character\n\n")
        for stat in stats:
            f.write(f"{stat[0]} {stat[1]}\n")
        f.write("\n")
        for room in room_stats:
            f.write(f"{room[0]}\n\n")
            f.write(f"enemy {room[1]}\n")
            f.write(f"loot {room[2]}\n")
            f.write(f"secret {room[3]}\n\n")
    '''

    if load:
        with open("save.txt", "r") as f:
            out = f.readlines()
            current_room = out[2].split()[1]
            visited_rooms = out[4].split()
            character_stats = [x.split() for x in out[8:32]]
            all_rooms  = []
            for i in range(28):
                all_rooms.append([out[33+i*6].strip(), out[35+i*6].split()[1], out[36+i*6].split()[1], out[37+i*6].split()[1]])

        output_rooms = []
        for room in visited_rooms[1:]:
            output_rooms.append(rooms[room])
    
        for room in all_rooms:
            if room[0] in visited_rooms:
                if room[1] == "None":
                    rooms[room[0]].enemy = None
                else:
                    rooms[room[0]].enemy = enemies[room[1]]

                if room[2] == "None":
                    rooms[room[0]].loot = None
                else:
                    rooms[room[0]].loot = loots[room[2]]

                if room[3] == "True":
                    rooms[room[0]].secret = True
                else:
                    rooms[room[0]].secret = False
        
    link_forward(walledCity99, commencement)
    link_right(commencement, asphodel)
    link_back(asphodel, greenhillZone)
    link_right(greenhillZone, theMushroomKingdom)
    link_back(greenhillZone, kingdomOfKu)
    link_left(kingdomOfKu, bunker)
    link_right(kingdomOfKu, zebes)
    link_right(asphodel, mementos)
    link_forward(mementos, shoresOfNine)
    link_back(mementos, theForge)
    link_right(theForge, midgar)
    link_right(midgar, dirtmouth)
    link_forward(dirtmouth, theEndDimension)
    link_forward(theEndDimension, theShriekingShack)
    link_right(dirtmouth, hyruleKingdom)
    link_back(hyruleKingdom, celestialResort)
    link_back(celestialResort, sixthCircleOfHell)
    link_right(sixthCircleOfHell, ascent)
    link_forward(ascent, towerOfFate)
    link_right(ascent, miquellasHaligtree)
    link_forward(miquellasHaligtree, theHallow)
    link_forward(theHallow, theObraDinn)
    link_back(miquellasHaligtree, kamurocho)
    link_left(kamurocho, snowdin)
    link_left(snowdin, apertureLab)
    link_forward(snowdin, theAstralPlane)
    link_back(snowdin, theSealedTemple) 

    # Sets the default statistics of the character
    if load:
        for info in character_stats:
            name = info[0]
            stat = info[1:]

            if name == "name":
                character.name = stat[0]

            elif name in ["health", "max_health", "attack", "mana", "max_mana", "defence", "health_flask", "mana_flask", "money"]:
                setattr(character, name, int(stat[0]))

            elif name == "spells":
                temp = []
                if stat[0] != "None":
                    for spell in stat:
                        temp.append(spells[spell])
                character.spells = temp

            elif name == "armour":
                if stat[0] == "None":
                    character.armour = None
                else:
                    character.armour = armours[stat[0]]

            elif name == "armours":
                temp = []
                if stat[0] != "None":
                    for armour in stat:
                        temp.append(armours[armour])
                character.armours = temp
            
            elif name == "weapon":
                if stat[0] == "None":
                    character.weapon = None
                else:
                    character.weapon = weapons[stat[0]]

            elif name == "weapons":
                temp = []
                if stat[0] != "None":
                    for weapon in stat:
                        temp.append(weapons[weapon])
                character.weapons = temp

            elif name == "accessory":
                if stat[0] == "None":
                    character.accessory = None
                else:
                    character.accessory = accessories[stat[0]]

            elif name == "accessories":
                temp = []
                if stat[0] != "None":
                    for accessory in stat:
                        temp.append(accessories[accessory])
                character.accessories = temp

            elif name == "shield":
                if stat[0] == "None":
                    character.shield = None
                else:
                    character.shield = shields[stat[0]]

            elif name == "shields":
                temp = []
                if stat[0] != "None":
                    for shield in stat:
                        temp.append(shields[shield])
                character.shields = temp

            elif name == "items":
                temp = []
                if stat[0] != "None":
                    for item in stat:
                        temp.append(items[item])
                character.items = temp

            elif name == "upgrades":
                temp = []
                if stat[0] != "None":
                    for upgrade in stat:
                        temp.append(upgrades[upgrade])
                character.upgrades = temp

            elif name == "shop_inventory":
                temp = []
                if stat[0] != "None":
                    for item in stat:
                        temp.append(shops[item])
                character.shop_inventory = temp

            elif name in ["shop", "additional_shop", "gamble"]:
                if stat [0] == "True":
                    setattr(character, name, True)
                else:
                    setattr(character, name, False)
            
    else:
        character.spells.append(WingardiumLeviosa())
        character.weapon = Wand()
        character.weapons.append(character.weapon)
        character.health = 100
        character.max_health = 100
        character.mana = 50
        character.max_mana = 50
        character.health_flask = 2
        character.mana_flask = 2
    
    if load:
        return [rooms[current_room], character, output_rooms]
    else:
        return [dirtmouth, character]