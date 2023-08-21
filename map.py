from enemy import Enemy
from item import Weapon
from item import Potion

class Room:
    """
    creates the room weapon and enemy

    Attribute
    ---------
    + name: str
    + enemy: str
    + right: str
    + left: str
    + up: str
    + down: str
    + been_here: bool
    + discription: str
    - is_fighting: bool

    Method
    ------
    + link_left(): updates the room to the left of the home room(self.name)
    + link_right(): updates the room to the right of the home room(self.name)
    + link_up(): updates the room to the up of the home room(self.name)
    + link_down(): updates the room to the down of the home room(self.name)
    + set_is_fighting: updates the status of the character in the room
    + get_is_fighting: gets the status of the character in the room
    + set_been_here(): updates the status of wether the character has been to this room
    + get_been_here(): gets the status of wether the character has been to this room
    """
   
    def __init__(self, name: str, enemy, description):
        self.name = name
        self.enemy = enemy
        self.description = description
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.been_here = False
        self.is_fighting = False
        self.description = description

    def __repr__(self):
        print(f"Room({self.name})")

    def set_been_here(self, status: bool) -> None:
        self.been_here = status
        
    def get_been_here(self) -> bool:
        return self.been_here

    def set_is_fighting(self, status: bool) -> None:
        self.is_fighting = status

    def get_is_fighting(self) -> bool:
        return self.is_fighting
    
    def __str__(self):
        return self.name

    def link_left(self, name: str, enemy: str, description: str):
        temp = Room(name, enemy, description)
        temp.right = self
        self.left = temp

    def link_right(self, name: str, enemy: str, description: str):
        temp = Room(name, enemy, description)
        temp.left = self
        self.right = temp

    def link_up(self, name: str, enemy: str, description: str):
        temp = Room(name, enemy, description)
        temp.down = self
        self.up = temp

    def link_down(self, name: str, enemy: str, description: str):
        temp = Room(name, enemy, description)
        temp.up = self
        self.down = temp

gryffindor_sword = Weapon("Gryffindor SSSword", "You have obtained the Sword Of Gryffindor, which can only be held by a TRUE gryffindor! This sword does X2 damage to Basilisk!", 250)

philosopher_stone = Weapon("Philosopher's SSStone", "You have obtained the Philosopher's Stone, which can only be held by a TRUE YOU! This stone does xtra 500 damage to Voldemort, meow!", 500)

felix_felicis = Potion("Felix Felicis", "WOW, you have gotten a FELIX FELICIS potion! This potion gives you good luck! However, it is a single-use-item, make good use of it! It increase attack by 1000", 1000, 0)

elixir_of_life = Potion("Elixir Of Life", "NICE, you've got the elixir of life! Use it wisely as it is a single-use-item! It heals 500 hp", 0, 500)

def setup():
    """
    Generates 3 rooms, named room1, room2, room3 and links them together
    """

    
    map = Room("Room1", Enemy('Dementors', 100), "Upon entering the room, and an icy shiver creeps up your spine. The air feels heavy and oppressive, as if it's suffocating under an invisible weight. The light that filters through the windows seems muted and lifeless, casting long, eerie shadows across the walls. In the center of the room, a figure stands, draped in tattered, dark robes that seem to drink in the feeble light.\n", gryffindor_sword)
    
    map.link_left("Room2", Enemy('Basilisk', 500), "As you cautiously step into the dimly lit chamber, an uneasy weight settles in the pit of your stomach. The air feels heavy with a sense of foreboding, and the faint echo of your footsteps reverberates through the cold stone walls. The room is vast and cavernous, its architecture ancient and mysterious.\nA flicker of movement catches your eye, and your heart skips a beat. Slowly, almost languidly, a massive form emerges from the shadows. The basilisk, a creature of legend and terror, slithers forth with an eerie grace. Its scales, a mesmerizing tapestry of dark and iridescent shades, seem to absorb what little light dares to penetrate the chamber.\n", elixir_of_life)
    
    map.link_right("Room3", Enemy('Death Eater', 1000), "As you cautiously push open the creaking door to the abandoned classroom, a sense of unease washes over you. The air is heavy with the weight of neglect, and the room is dimly illuminated by the pale moonlight that filters through the dusty windows. The remnants of forgotten lessons lay scattered across desks, a silent testament to the room's disuse.\nAs you step further into the room, a sudden movement catches your eye. Out of the shadows, a figure materializes with an eerie swiftness. The darkness seems to cling to them, cloaking them in an aura of menace. The figure's robes billow softly, a whispering echo of their sinister intent.\n", felix_felicis)
    
    map.link_up("Room4", Enemy('Voldemort', 5000), "Upon entering the Slytherin common room, a profound hush descends. The room is bathed in dim green light, casting an unsettling ambiance. At the heart of the chamber stands Voldemort, his presence commanding attention and trepidation. His features, pale and serpentine, are accentuated by the eerie glow.\nHis crimson gaze locks onto you, piercing and intense. The room seems to bend to his will, an extension of his dominance. The very air feels heavy, pregnant with the weight of his history and power. As he addresses you, his voice carries a chilling authority that leaves no room for dissent.\n")
    
    return map