class Weapon:
    """
    creates the weapon

    Attribute
    ---------
    + name: str
    + description: str
    + attack: int | float

    Method
    ------
    
    
    """

    def __init__(self, name: str, description: str, attack: int) -> None:
        self.type = 'Weapon'
        self.name = name
        self.description = description
        self.attack = attack

    def __repr__(self) -> str:
        return print(f"Item{self.name}")

class Potion:
    """
    creates the potion

    Attribute
    ---------
    + name: str
    + description: str
    + attack: int | float
    + heal: int | float

    Method
    ------
    
    
    """

    def __init__(self, name: str, description: str, attack: int, heal: int) -> None:
        self.type = 'potion'
        self.name = name
        self.description = description
        self.attack = attack
        self.heal = heal

    def __repr__(self) -> str:
        return print(f"Item{self.name}")