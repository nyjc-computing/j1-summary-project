class Battle:
    def __init__(self, player, room):
        self.player = player
        self.room = room

    def battle_start(self):
        i = 0
        while not self.battle_over():
            print(f"Your health: {self.player.get_health()}")
            print(f"Enemy health: {self.room.get_enemies()[0].get_health()}")
            if i % 2 == 0:
                self.player_attack()
            elif i % 2 == 1:
                self.enemy_attack()
            
            i += 1
        print("Battle over!")

    def player_attack(self):
        self.player.attack(self.room.get_enemies()[0])
        if self.get_enemy_health() <= 0:
            self.room.remove_enemy()
            print("Enemy defeated!")
        if self.room.all_enemies_defeated():
            print("All enemies defeated!")

    def enemy_attack(self):
        self.room.enemies[0].attack(self.player)
        if self.player.get_health() <= 0:
            print("You died! WEAK!")

    def get_enemy_health(self):
        return self.room.get_enemies()[0].get_health()

    def battle_over(self):
        return self.player.get_health() <= 0 or self.room.all_enemies_defeated()
