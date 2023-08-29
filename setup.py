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

    link_back(zebes, kingdomOfKu)
    link_right(kingdomOfKu, bunker)
    link_back(kingdomOfKu, greenhillZone)
    link_left(greenhillZone, theMushroomKingdom)
    link_back(greenhillZone, asphodel)
    link_back(asphodel, commencement)
    link_back(commencement, walledCity99)
    link_right(asphodel, mementos)
    link_right(mementos, shoresOfNine)
    link_back(mementos, theForge)
    link_right(theForge, midgar)
    link_right(midgar, dirtmouth)
    link_forward(dirtmouth, theEndDimension)
    link_forward(theEndDimension, theShriekingShack)
    link_right(dirtmouth, hyruleKingdom)
    link_back(hyruleKingdom, celestialResort)
    link_back(celestialResort, ascent)
    link_right(ascent, sixthCircleOfHell)
    link_back(sixthCircleOfHell, towerOfFate)
    link_forward(sixthCircleOfHell, stormveilCastle)
    link_right(stormveilCastle, theHallow)
    link_back(theHallow, theObraDinn)
    link_forward(stormveilCastle, kamurocho)
    link_forward(kamurocho, snowdin)
    link_left(snowdin, theAstralPlane)
    link_forward(snowdin, apertureLab)
    link_right(snowdin, theSealedTemple)

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