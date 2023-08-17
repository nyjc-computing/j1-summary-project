class Enemy:
    """
    creates the enemies that are in the room

    Attributes
    ----------
    + name: str
    + spell: str
    - health: int
    + battle_points: int
    + loot: str

    Methods
    -------
    + set_health(): updates the enemy's health
    - is_dead(): checks the state of the enemy
    + get_health(): gets the health of the enemy
    
    """
    def __init__(self, name: str, health) -> None:
        self.name = name
        self.spell = None
        self._health = health
        self.battle_points = 10
        self.loot = None

    def __repr__(self) -> None:
        print(f"enemy{self.name}")

    def _is_dead(self) -> str:
        """
        checks if enemy is dead.
        returns the HP is it is not
        drops something if it is dead
        """
        if self.health == 0:
            return self.loot

    def set_health(self, bp: int) -> None:
        """
        Updates the enemy's health
        """
        self.health -= bp

    def get_health(self) -> int:
        """
        Returns the enemys health
        """
        return self.health