class game_map:
    """
    Attributes:
    - self.map: contains the map for the game
    Methods:
    - each room has two map update events
        - one is for when the player enters the room for the first time
        - the other is for when the players has done everything in the room
    """

    def __init__(self):
        self.map = [[" " for x in range(125)] for x in range(35)]

    def display(self) -> None:
        """
        Show the map
        """
        for row in self.map:
            print("".join(row))

    def make_room(self, y: int, x: int, name: str) -> None:
        """
        draws a box, centered on coords (x,y) on the map
        name is the name of the room
        """
        layer1 = "┌" + "─"*len(name) + "┐"
        layer2 = "│" + name + "│"
        layer3 = "└"+ "─"*len(name) + "┘"
        box = [layer1, layer2, layer3]
        x = x - int(len(name)/2) - 1
        y = y - 1
        for row in range(3):
            for column in range(2+len(name)):
                self.map[row + y][column + x] = box[row][column]

    def finish_room(self, y: int, x: int, name: str) -> None:
        """
        draws a bold box, centered on coords (x,y) on the map
        name is the name of the room
        """
        layer1 = "╭" + "━"*len(name) + "╮"
        layer2 = "┃" + name + "┃"
        layer3 = "╰"+ "━"*len(name) + "╯"
        box = [layer1, layer2, layer3]
        x = x - int(len(name)/2) - 1
        y = y - 1
        for row in range(3):
            for column in range(2+len(name)):
                self.map[row + y][column + x] = box[row][column]

    def hconnect(self, y: int, x: int, l: int) -> None:
        """
        draws a horizontal connector from (x,y) to (x+l,y)
        """
        self.map[y][x] = "╠"
        for i in range(l):
            self.map[y][x+1+i] = "═"
        self.map[y][x+1+l] = "╣"

    def vconnect(self, y: int, x: int, l: int) -> None:
        """
        draws a vertical connector from (x,y) to (x,y+l)
        """
        self.map[y][x] = "╦"
        for i in range(l):   
            self.map[y+1+i][x] = "║"
        self.map[y+1+l][x] = "╩"
                
    def dirtmouth_enter(self) -> None:
        """
        updates map for first time visiting dirtmouth
        """
        #make room
        self.make_room(10,60,"Dirtmouth")
        
        #make hidden rooms
        self.make_room(10,51," ? ")
        self.make_room(10,69," ? ")
        self.make_room(6,60, " ? ")

        #(re)make paths
        self.hconnect(10,53,1)
        self.hconnect(10,65,1)
        self.vconnect(7,60,1)

    def dirtmouth_clear(self) -> None:
        """
        updates map for fully clearing dirtmouth
        """
        #make room
        self.finish_room(10,60,"Dirtmouth")

        #(re)make paths
        self.hconnect(10,53,1)
        self.hconnect(10,65,1)
        self.vconnect(7,60,1)

    def end_dimension_enter(self) -> None:
        """
        updates map for first time visiting the end
        """
        #make room
        self.make_room(6,60,"The End Dimension")
        
        #make hidden rooms
        self.make_room(2,60, " ? ")

        #(re)make paths
        self.vconnect(3,60,1)
        self.vconnect(7,60,1)

    def end_dimension_clear(self) -> None:
        """
        updates map for fully clearing the end
        """
        #make room
        self.finish_room(6,60,"The End Dimension")

        #(re)make paths
        self.vconnect(3,60,1)
        self.vconnect(7,60,1)

    def hyrule_enter(self) -> None:
        """
        updates map for first time visiting hyrule
        """
        #make room
        self.make_room(10,75,"Hyrule Kingdom")
        
        #make hidden rooms
        self.make_room(14,75, " ? ")

        #(re)make paths
        self.hconnect(10,65,1)
        self.vconnect(11,75,1)

    def hyrule_clear(self) -> None:
        """
        updates map for fully clearing hyrule
        """
        #make room
        self.finish_room(10,75,"Hyrule Kingdom")

        #(re)make paths
        self.hconnect(10,65,1)
        self.vconnect(11,75,1)

    def celestial_resort_enter(self) -> None:
        """
        updates map for first time visiting celestial resort
        """
        #make room
        self.make_room(14,75,"Celestial Resort")
        
        #make hidden rooms
        self.make_room(18,75, " ? ")

        #(re)make paths
        self.vconnect(11,75,1)
        self.vconnect(15,75,1)

    def celestial_resort_clear(self) -> None:
        """
        updates map for fully clearing celestial resort
        """
        #make room
        self.finish_room(14,75,"Celestial Resort")

        #(re)make paths
        self.vconnect(11,75,1)
        self.vconnect(15,75,1)

    def ascent_enter(self) -> None:
        """
        updates map for first time visiting ascent
        """
        #make room
        self.make_room(18,75,"Ascent")

        #make hidden rooms
        self.make_room(18,86," ? ")

        #(re)make paths
        self.vconnect(15,75,1)
        self.hconnect(18,78,5)

    def ascent_clear(self) -> None:
        """
        updates map for fully clearing ascent
        """
        #make room
        self.finish_room(18,75,"Ascent")

        #(re)make paths
        self.vconnect(15,75,1)
        self.hconnect(18,78,5)

    def sixth_circle_enter(self) -> None:
        """
        updates map for first time visiting 6th circle of hell
        """
        #make room
        self.make_room(18,94,"6th Circle Of Hell")

        #make hidden rooms
        self.make_room(14,94," ? ")
        self.make_room(18,107," ? ")

        #(re)make paths
        self.hconnect(18,78,5)
        self.hconnect(18,103,1)
        self.vconnect(15,94,1)

    def sixth_circle_clear(self) -> None:
        """
        updates map for fully clearing 6th circle of hell
        """
        #make room
        self.finish_room(18,94,"6th Circle Of Hell")

        #(re)make paths
        self.hconnect(18,78,5)
        self.hconnect(18,103,1)
        self.vconnect(15,94,1)

    def tower_enter(self) -> None:
        """
        updates map for first time visiting tower of fate
        """
        #make room
        self.make_room(14,94,"Tower of Fate")

        #make hidden rooms

        #(re)make paths
        self.vconnect(15,94,1)

    def tower_clear(self) -> None:
        """
        updates map for fully clearing tower of fate
        """
        #make room
        self.finish_room(14,94,"Tower of Fate")

        #(re)make paths
        self.vconnect(15,94,1)

    def stormveil_enter(self) -> None:
        """
        updates map for first time visiting stormveil castle
        """
        #make room
        self.make_room(18,114,"Stormveil Castle")

        #make hidden rooms
        self.make_room(14,114," ? ")
        self.make_room(25,114," ? ")

        #(re)make paths
        self.vconnect(15,114,1)
        self.vconnect(19,114,4)
        self.hconnect(18,103,1)

    def stormveil_clear(self) -> None:
        """
        updates map for fully clearing stormveil castle
        """
        #make room
        self.finish_room(18,114,"Stormveil Castle")

        #(re)make paths
        self.vconnect(15,114,1)
        self.vconnect(19,114,4)
        self.hconnect(18,103,1)

    def hallow_enter(self) -> None:
        """
        updates map for first time visiting the hallow
        """
        #make room
        self.make_room(14,114,"The Hallow")

        #make hidden rooms
        self.make_room(10,114," ? ")

        #(re)make paths
        self.vconnect(15,114,1)
        self.vconnect(11,114,1)

    def hallow_clear(self) -> None:
        """
        updates map for fully clearing the hallow
        """
        #make room
        self.finish_room(14,114,"The Hallow")

        #(re)make paths
        self.vconnect(15,114,1)
        self.vconnect(11,114,1)

    def obradinn_enter(self) -> None:
        """
        updates map for first time visiting the obra dinn
        """
        #make room
        self.make_room(10,114,"The Obra Dinn")

        #make hidden rooms

        #(re)make paths
        self.vconnect(11,114,1)

    def obradinn_clear(self) -> None:
        """
        updates map for fully clearing the obra dinn
        """
        #make room
        self.finish_room(10,114,"The Obra Dinn")

        #make hidden rooms

        #(re)make paths
        self.vconnect(11,114,1)

    def kamurocho_enter(self) -> None:
        """
        updates map for first time visiting kamurocho
        """
        #make room
        self.make_room(25,114,"Kamurocho")

        #make hidden rooms
        self.make_room(25,102," ? ")

        #(re)make paths
        self.vconnect(19,114,4)
        self.hconnect(25,104,4)

    def kamurocho_clear(self) -> None:
        """
        updates map for fully clearing kamurocho
        """
        #make room
        self.finish_room(25,114,"Kamurocho")

        #make hidden rooms

        #(re)make paths
        self.vconnect(19,114,4)
        self.hconnect(25,104,4)

    def snowdin_enter(self) -> None:
        """
        updates map for first time visiting snowdin
        """
        #make room
        self.make_room(25,100,"Snowdin")

        #make hidden rooms
        self.make_room(25,89," ? ")
        self.make_room(21,100," ? ")
        self.make_room(29,100," ? ")

        #(re)make paths
        self.hconnect(25,104,4)
        self.hconnect(25,91,4)
        self.vconnect(22,100,1)
        self.vconnect(26,100,1)

    def snowdin_clear(self) -> None:
        """
        updates map for fully clearing snowdin
        """
        #make room
        self.finish_room(25,100,"Snowdin")

        #(re)make paths
        self.hconnect(25,104,4)
        self.hconnect(25,91,4)
        self.vconnect(22,100,1)
        self.vconnect(26,100,1)

    def aperture_enter(self) -> None:
        """
        updates map for first time visiting aperture
        """
        #make room
        self.make_room(25,84,"Aperture Labs")

        #make hidden rooms

        #(re)make paths
        self.hconnect(25,91,4)

    def aperture_clear(self) -> None:
        """
        updates map for fully clearing aperture
        """
        #make room
        self.finish_room(25,84,"Aperture Labs")

        #make hidden rooms

        #(re)make paths
        self.hconnect(25,91,4)

    def astral_plane_enter(self) -> None:
        """
        updates map for first time visiting the astral plane
        """
        #make room
        self.make_room(21,100,"The Astral Plane")

        #make hidden rooms

        #(re)make paths
        self.vconnect(22,100,1)

    def astral_plane_clear(self) -> None:
        """
        updates map for fully clearing the astral plane
        """
        #make room
        self.finish_room(21,100,"The Astral Plane")

        #(re)make paths
        self.vconnect(22,100,1)

    def sealed_temple_enter(self) -> None:
        """
        updates map for first time visiting the sealed temple
        """
        #make room
        self.make_room(29,100,"The Sealed Temple")

        #make hidden rooms

        #(re)make paths
        self.vconnect(26,100,1)

    def sealed_temple_clear(self) -> None:
        """
        updates map for fully clearing the sealed temple
        """
        #make room
        self.finish_room(29,100,"The Sealed Temple")

        #(re)make paths
        self.vconnect(26,100,1)

    def midgar_enter(self) -> None:
        """
        updates map for first time visiting midgar
        """
        #make room
        self.make_room(10,50,"Midgar")

        #make hidden rooms
        self.make_room(10,42," ? ")

        #(re)make paths
        self.hconnect(10,53,1)
        self.hconnect(10,44,1)

    def midgar_clear(self) -> None:
        """
        updates map for fully clearing midgar
        """
        #make room
        self.finish_room(10,50,"Midgar")

        #make hidden rooms

        #(re)make paths
        self.hconnect(10,53,1)
        self.hconnect(10,44,1)

    def forge_enter(self) -> None:
        """
        updates map for first time visiting the forge
        """
        #make room
        self.make_room(10,39,"The Forge")

        #make hidden rooms
        self.make_room(6,39," ? ")

        #(re)make paths
        self.hconnect(10,44,1)
        self.vconnect(7,39,1)

    def forge_clear(self) -> None:
        """
        updates map for fully clearing the forge
        """
        #make room
        self.finish_room(10,39,"The Forge")

        #(re)make paths
        self.hconnect(10,44,1)
        self.vconnect(7,39,1)

    def mementos_enter(self) -> None:
        """
        updates map for first time visiting mementos
        """
        #make room
        self.make_room(6,39,"Mementos")

        #make hidden rooms
        self.make_room(2,39," ? ")
        self.make_room(6,27," ? ")

        #(re)make paths
        self.vconnect(7,39,1)
        self.vconnect(3,39,1)
        self.hconnect(6,29,4)

    def mementos_clear(self) -> None:
        """
        updates map for fully clearing mementos
        """
        #make room
        self.finish_room(6,39,"Mementos")

        #(re)make paths
        self.vconnect(7,39,1)
        self.vconnect(3,39,1)
        self.hconnect(6,29,4)

    def shores_enter(self) -> None:
        """
        updates map for first time visiting shores of 9
        """
        #make room
        self.make_room(2,39,"Shores of Nine")

        #make hidden rooms

        #(re)make paths
        self.vconnect(3,39,1)

    def shores_clear(self) -> None:
        """
        updates map for fully clearing shores of 9
        """
        #make room
        self.finish_room(2,39,"Shores of Nine")

        #make hidden rooms

        #(re)make paths
        self.vconnect(3,39,1)

    def asphodel_enter(self) -> None:
        """
        updates map for first time visiting asphodel
        """
        #make room
        self.make_room(6,25,"Asphodel")

        #make hidden rooms
        self.make_room(6,13," ? ")
        self.make_room(14,30," ? ")

        #(re)make paths
        self.hconnect(6,29,4)
        self.hconnect(6,15,4)
        self.vconnect(7,25,6)
        self.hconnect(14,25,2)
        self.map[14][25] = "╚"

    def asphodel_clear(self) -> None:
        """
        updates map for fully clearing asphodel
        """
        #make room
        self.finish_room(6,25,"Asphodel")

        #(re)make paths
        self.hconnect(6,29,4)
        self.hconnect(6,15,4)
        self.vconnect(7,25,6)
        self.hconnect(14,25,2)
        self.map[14][25] = "╚"

    def commencement_enter(self) -> None:
        """
        updates map for first time visiting commencement
        """
        #make room
        self.make_room(6,9,"Commencement")

        #make hidden rooms
        self.make_room(10,8," ? ")

        #(re)make paths
        self.hconnect(6,15,4)
        self.vconnect(7,8,1)

    def commencement_clear(self) -> None:
        """
        updates map for fully clearing commencement
        """
        #make room
        self.finish_room(6,9,"Commencement")

        #(re)make paths
        self.hconnect(6,15,4)
        self.vconnect(7,8,1)

    def walled_enter(self) -> None:
        """
        updates map for first time visiting walled city 99
        """
        #make room
        self.make_room(10,9,"Walled City 99")

        #make hidden rooms
        self.make_room(14,10," ? ")

        #(re)make paths
        self.vconnect(7,8,1)
        self.vconnect(11,10,1)

    def walled_clear(self) -> None:
        """
        updates map for fully clearing walled city 99
        """
        #make room
        self.finish_room(10,9,"Walled City 99")

        #(re)make paths
        self.vconnect(7,8,1)
        self.vconnect(11,10,1)

    def last_resort_enter(self) -> None:
        """
        updates map for first time visiting the last resort
        """
        #make room
        self.make_room(14,10,"The Last Resort")

        #make hidden rooms

        #(re)make paths
        self.vconnect(11,10,1)

    def last_resort_clear(self) -> None:
        """
        updates map for fully clearing the last resort
        """
        #make room
        self.finish_room(14,10,"The Last Resort")

        #make hidden rooms

        #(re)make paths
        self.vconnect(11,10,1)

    def greenhill_enter(self) -> None:
        """
        updates map for first time visiting greenhill zone
        """
        #make room
        self.make_room(14,36,"Greenhill Zone")

        #make hidden rooms
        self.make_room(18,36," ? ")
        self.make_room(14,48," ? ")

        #(re)make paths
        self.vconnect(7,25,6)
        self.hconnect(14,25,2)
        self.map[14][25] = "╚"
        self.hconnect(14,43,2)
        self.vconnect(15,36,1)

    def greenhill_clear(self) -> None:
        """
        updates map for fully clearing greenhill zone
        """
        #make room
        self.finish_room(14,36,"Greenhill Zone")

        #(re)make paths
        self.vconnect(7,25,6)
        self.hconnect(14,25,2)
        self.map[14][25] = "╚"
        self.hconnect(14,43,1)
        self.vconnect(15,36,1)
        
    def mushroom_enter(self) -> None:
        """
        updates map for first time visiting the mushroom kingdom
        """
        #make room
        self.make_room(14,55,"Mushroom Kingdom")

        #make hidden rooms

        #(re)make paths
        self.hconnect(14,43,2)

    def mushroom_clear(self) -> None:
        """
        updates map for fully clearing mushroom kingdom
        """
        #make room
        self.finish_room(14,55,"Mushroom Kingdom")

        #make hidden rooms

        #(re)make paths
        self.hconnect(14,43,2)

    def kingdom_ku_enter(self) -> None:
        """
        updates map for first time visiting kingdom of ku
        """
        #make room
        self.make_room(18,36,"The Kingdom of Ku")

        #make hidden rooms
        self.make_room(18,49," ? ")
        self.make_room(18,23," ? ")

        #(re)make paths
        self.vconnect(15,36,1)
        self.hconnect(18,45,1)
        self.hconnect(18,25,1)

    def kingdom_ku_clear(self) -> None:
        """
        updates map for fully clearing kingdom of ku
        """
        #make room
        self.finish_room(18,36,"The Kingdom of Ku")

        #(re)make paths
        self.vconnect(15,36,1)
        self.hconnect(18,45,1)
        self.hconnect(18,25,1)

    def zebes_enter(self) -> None:
        """
        updates map for first time visiting zebes
        """
        #make room
        self.make_room(18,50,"Zebes")

        #make hidden rooms

        #(re)make paths
        self.hconnect(18,45,1)

    def zebes_clear(self) -> None:
        """
        updates map for fully clearing zebes
        """
        #make room
        self.finish_room(18,50,"Zebes")

        #make hidden rooms

        #(re)make paths
        self.hconnect(18,45,1)

    def bunker_enter(self) -> None:
        """
        updates map for first time visiting bunker
        """
        #make room
        self.make_room(18,22,"Bunker")

        #make hidden rooms

        #(re)make paths
        self.hconnect(18,25,1)

    def bunker_clear(self) -> None:
        """
        updates map for fully clearing bunker
        """
        #make room
        self.finish_room(18,22,"Bunker")

        #make hidden rooms

        #(re)make paths
        self.hconnect(18,25,1)

    def shrieking_enter(self) -> None:
        """
        updates map for first time visiting shrieking shack
        """
        #make room
        self.make_room(2,60,"Shrieking Shack")

        #make hidden rooms

        #(re)make paths
        self.vconnect(3,60,1)

    def shrieking_clear(self) -> None:
        """
        updates map for fully clearing shrieking shack
        """
        #make room
        self.finish_room(2,60,"Shrieking Shack")

        #make hidden rooms

        #(re)make paths
        self.vconnect(3,60,1)

legend = """
Legend:
┌───┐                                   ╭━━━╮
│   │ = Room has unfinished objectives  ┃   ┃ = Fully Cleared Room
└───┘                                   ╰━━━╯
"""