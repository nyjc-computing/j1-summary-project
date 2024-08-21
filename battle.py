import time

class Battle:
    def __init__(self, player, room):
        self.player = player
        self.room = room
        

    def battle_start(self):
        i = 0
        while not self.battle_over():
            if i % 2 == 0:
                self.player_attack()
            elif i % 2 == 1:
                self.enemy_attack()
            
            i += 1
            time.sleep(0.1)
        print("Battle over!")

    def player_attack(self):
        source = self.player
        target = self.room.get_enemies()[0]
        source.attack(target)
        print(f"You attacked the {target.get_type()}! {target.get_type()} health: {self.room.get_enemies()[0].get_health()}")
        if self.get_enemy_health() <= 0:
            self.room.remove_enemy()
            print("Enemy defeated!")
        if self.room.all_enemies_defeated():
            print("All enemies defeated!")

    def enemy_attack(self):
        source = self.room.get_enemies()[0]
        target = self.player
        source.attack(target)
        print(f"{source.get_type()} attacked you! Your health: {self.player.get_health()}")
        if self.player.get_health() <= 0:
            print("You died! WEAK!")

    def get_enemy_health(self):
        return self.room.get_enemies()[0].get_health()

    def battle_over(self):
        return self.player.get_health() <= 0 or self.room.all_enemies_defeated()
