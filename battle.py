class Battle:
    def __init__(self, player, room):
        self.player = player
        self.room = room

    def player_attack(self):
        self.player.attack(self.room.get_enemies()[0])

    def enemy_attack(self):
        self.room.enemies[0].attack(self.player)

    def get_enemy_health(self):
        return self.room.get_enemies()[0].get_health()

    def battle_over(self):
        return self.player.health == 0 or self.room.all_enemies_defeated()
