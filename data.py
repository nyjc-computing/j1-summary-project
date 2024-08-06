import room
import character


def createRooms() -> list[room.Room]:
    """
    Must follow order of room: Dungeon, Kitchen, Hall, Toilet, Bedroom
    Store Name & Number of enemies
    """
    list_of_rooms = [
        room.Room("Dungeon", 3),
        room.Room("Kitchen", 3),
        room.Room("Hall", 3),
        room.Room("Toilet", 3),
        room.Room("Bedroom", 3)
    ]

    return list_of_rooms
    


def createPlayer() -> character.Player:
    
    return character.Player(1,1, [])


def createPrincess() -> character.Princess:

    return character.Princess(1,1)
