class Character:
    """
    creates the character

    Attribute
    ---------
    + name: str
    + health: int
    + spell: str
    + battle_points: int

    Method
    ------
    + set_health(): updates the character's health
    + get_health(): gets the health of the character
    - is_dead(): checks if the enemy is dead
    
    """
    def __init__(self) -> None:
        self.name = 'Hero'
        self.health = 1000
        self.spell = None
        self.battle_points = 100
        self.item = []

    def __repr__(self) -> str:
        print(f"character: {self.name}")

    def __str__(self):
        return self.name

    def is_dead(self) -> bool:
        """Checks if the enemy is dead"""
        if self.health == 0:
            return True
        return False
    
    def set_health(self, bp: int) -> None:
        """Updates the character's health"""
        self.health += bp

    def get_health(self) -> int:
        """Returns the character's health"""
        return self.health