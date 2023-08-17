class Enemy:
    """
    creates the enemies that are in the room

    Attributes
    ----------
    + name: str
    + spell: str
    + health: int
    + battle_points: int
    + loot: str

    Methods
    -------
    + attack(): does attack to the character
    + run(): checks the state of the enemy
    
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.spell = None
        self.health = 100
        self.battle_points = 10
        self.loot = None

    def __repr__(self) -> None:
        print(f"enemy: {self.name}")

    def attack(self, characterHP) -> None:
        """
        takes in an attribute characterHP and each time this method is called the character gets damaged by the battle points the enemy has
        """
        characterHP -= self.battle_points
        return characterHP
    
    def is_dead(self) -> str:
        """
        checks if enemy is dead.
        returns the HP is it is not
        drops something if it is dead
        """
        if self.health == 0:
            return self.loot


