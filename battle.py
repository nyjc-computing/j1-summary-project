import time

class Battle:
    def __init__(self, player, room):
        self.player = player
        self.room = room
        

    def battle_start(self):
        if not self.room.all_enemies_defeated():
            print("YOU FOUND ENEMIES!!!!")
            i = 0
            while not self.battle_over():
                if i % 2 == 0:
                    self.player_attack()
                elif i % 2 == 1:
                    self.enemy_attack()
                
                i += 1
                time.sleep(0.1)
            print("Battle over!")
        else:
            print("All soldiers in the room have been defeated already!")

    def player_attack(self):
        source = self.player
        target = self.room.get_enemies()[0]
        source.attack(target)
        print(f"You attacked the {target.get_type()}! {target.get_type()} health: {target.get_health()}")
        if target.get_health() <= 0:
            if target.get_type() == "Princess":
                print("Princess is now unconcious! Time to escape!")
            else:
                print("Soldier defeated!")
            self.room.remove_enemy()
        if self.room.all_enemies_defeated():
            print("All soldiers in the room are defeated!")

    def enemy_attack(self):
        source = self.room.get_enemies()[0]
        target = self.player
        source.attack(target)
        print(f"{source.get_type()} attacked you! Your health: {target.get_health()}")
        # if target.get_health() <= 0:
        #     print("You died! WEAK!")

    def battle_over(self):
        return self.player.get_health() <= 0 or self.room.all_enemies_defeated()
