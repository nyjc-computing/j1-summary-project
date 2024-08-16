class Action:

    def __init__(self, action, player, monster):
        self.action = action
        self.player = player
        self.monster = monster

    def punch(self):
        """
        reduce monster health
        monster--> monster obj
        """
        damage = 10
        self.monster.take_damage(damage)

    def kick(self, monster):
        """reduce monster health"""
        damage = 20
        self.monster.take_damage(damage)

    def use_item(self,item_index):
        """reduce monster health"""
        item = self.player.inventory[item_index - 1]
        item.use_item()
        

