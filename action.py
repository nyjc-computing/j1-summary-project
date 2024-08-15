class Action:

    def __init__(self, action):
        self.action = action

    def punch(self, monster):
        """
        reduce monster health
        monster--> monster obj
        """
        damage = 10
        monster.health = monster.health - damage

    def kick(self, monster):
        """reduce monster health"""
        damage = 20
        monster.health = monster.health - damage

    def shoot(self):
        """reduce monster health"""
        damage = 30
        monster.health = monster.health - damage

    def pick_up(self, item):
        """add to player inventory"""
        player.inventory.add_item(item)

    def drop_obj(self):
        """delete from player inventroy"""
        player.inventory.remove_item(item)