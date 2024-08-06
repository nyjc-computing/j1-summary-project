import room
import character
import json

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
    
with open('data.json', 'r' ) as f:
    char_data = json.load(f)

    
def createPlayer() -> character.Player:
    """
    
    """
    record = char_data["player"]
    return character.Player(record["hp"] , record["str"], record["items"])


def createPrincess() -> character.Princess:
    record = char_data["princess"]
    return character.Princess(record["hp"], record["str"])

