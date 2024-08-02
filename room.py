class Room:

    def __init__(self, name, enemy_num):
        self.name = name
        self.enemy_num = enemy_num

    def get_enemy_num(self):
        return self.enemy_num

    def enemy_defeated(self):
        self.enemy_num -= 1
        if self.enemy_num <= 0:
             print(f'Enemies in {self.name} have all been defeated!')




def get_choice(self):
    print(f'You are in {self.get_now_room()}')
    print(f'-Choices- \n 1. next room: {self.nextroom} \n 2. prev room: {self.prev_room} \n 3. look around')
    choice = input("type your choice here: ")
    if choice not in '123':
        print('error')
    elif choice == 1:
        pass
    