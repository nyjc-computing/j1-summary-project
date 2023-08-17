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
    + attack():
    
    """
    def __init__(self) -> None:
        self.name = 'Hero'
        self.health = 100
        self.spell = None
        self.battle_points = 0

    def __repr__(self) -> str:
        print(f"character: {self.name}")

    def attack(self, enemyHP) -> int:
        """
        attacks the enemy and minus the enemy's hp
        """
        enemyHP -= self.battle_points
        return enemyHP

    def update_health(self, enemy_attack: int) -> int:
        self.health -= enemy_attack

    