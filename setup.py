# importing from other files
from room import *
from character import *
from weapon import *
from spell import *

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

def setup() -> [Room, Character]:
    """
    Generates the map and the character and returns it in a list
    """
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
    stormveilCastle = StormveilCastle()
    theHallow = TheHallow()
    theObraDinn = TheObraDinn()
    kamurocho = Kamurocho()
    snowdin = Snowdin()
    theAstralPlane = TheAstralPlane()
    apertureLab = ApertureLab()
    theSealedTemple = TheSealedTemple()

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
    link_back(celestialResort, ascent)
    link_right(ascent, sixthCircleOfHell)
    link_forward(sixthCircleOfHell, towerOfFate)
    link_right(sixthCircleOfHell, stormveilCastle)
    link_forward(stormveilCastle, theHallow)
    link_forward(theHallow, theObraDinn)
    link_back(stormveilCastle, kamurocho)
    link_left(kamurocho, snowdin)
    link_left(snowdin, apertureLab)
    link_forward(snowdin, theAstralPlane)
    link_back(snowdin, theSealedTemple)

    # Generates the character
    character = Character()

    # Sets the default statistics of the character
    character.spells.append(WingardiumLeviosa())
    character.weapon = Wand()
    character.weapons.append(character.weapon)
    character.health = 100
    character.max_health = 100
    character.mana = 50
    character.max_mana = 100
    character.health_flask = 2
    character.mana_flask = 2
    
    return [dirtmouth, character]