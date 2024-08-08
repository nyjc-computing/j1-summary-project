

class Item():
    def __init__(self, name, effect, description):
        self.name = name
        self.effect = effect
        self.description = description

    def get_name(self):
        return self.name

    def display_effect(self):
        """
        edit the print message
        """
        print(self.effect, self.description)

    def use_item(self):
        
        
        