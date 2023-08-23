import random
import data


def accuracy_calc(light: int) -> bool:
    temp = [True] * light + [False] * (100 - light)
    return temp[random.randint(0, len(temp) - 100)]


def defeat(players: list) -> bool:
    for player in players:
        if not player.is_defeated():
            return False
    return True


def victory(enemies: list) -> bool:
    for enemy in enemies:
        if not enemy.is_defeated():
            return False
    return True


class MUDGame:
    def __init__(self):
        # self.spawn = Room('home', up='closed')
        self.boss = data.Springtrap()
        self.current_room = data.start_room()
        self.gameOver = False
        self.player1 = None
        self.player2 = None
        self.player3 = None
        self.player4 = None

    
    def set_player(self, player, character):
        if player == 'Player 1':
            self.player1 = character
        elif player == 'Player 2':
            self.player2 = character
        elif player == 'Player 3':
            self.player3 = character
        elif player == 'Player 4':
            self.player4 = character

    def run(self):
        data.start_menu()
        for player in ['Player 1', 'Player 2', 'Player 3', 'Player 4']:
            character = data.choose_character()
            while character not in ['freddy', 'chica', 'bonnie', 'foxy', 'skip']:
                print(f"Please select a valid animatronic or finish party by entering 'skip'. Got {character}.")
                character = data.choose_character()
            if character == 'freddy':
                self.set_player(player, data.Freddy())
                print(f'{player} has selected Freddy Fazbear.')
            elif character == 'bonnie':
                self.set_player(player, data.Bonnie())
                print(f'{player} has selected Bonnie.')
            elif character == 'chica':
                self.set_player(player, data.Chica())
                print(f'{player} has selected Chica.')
            elif character== 'foxy':
                self.set_player(player, data.Foxy())
                print(f'{player} has selected Foxy.')
            elif character == 'skip':
                break
        print('The game will begin.')
        while not self.gameOver:
            if not self.current_room.grid.is_encounter():
                #prompt movement
                self.current_room.display_room()
                move = self.current_room.grid.prompt_movement()
                while move not in ['w', 'a', 's', 'd', 'inventory']:
                    print(f"Type w, a, s or d or 'inventory'. Got {move}.")
                    move = self.current_room.grid.prompt_movement()
                #Opening inventory
                if move == 'inventory':
                    data.display_inventory()
                    continue
                #entering next room
                if self.current_room.grid.get_position() == [0, 2] and move == 'w' and self.current_room.is_next_room(move):
                    self.current_room.next_room(move)
                    self.current_room.grid.move([4, 2])
                    continue
                elif self.current_room.grid.get_position() == [2, 0] and move == 'a' and self.current_room.is_next_room(move):
                    self.current_room.next_room(move)
                    self.current_room.grid.move([2, 4])
                    continue
                elif self.current_room.grid.get_position() == [4, 2] and move == 's' and self.current_room.is_next_room(move):
                    self.current_room.next_room(move)
                    self.current_room.grid.move([0, 2])
                    continue
                elif self.current_room.grid.get_position() == [2, 4] and move == 'd'  and self.current_room.is_next_room(move):
                    self.current_room.nextRoom(move)
                    self.current_room.grid.move([2, 0])
                    continue
                #moving in current room
                if move == 'w' and self.current_room.grid.get_position()[0] != 0:
                    current_position = self.current_room.grid.get_position()
                    current_position[1] = current_position[1] + 1
                    self.current_room.grid.move(current_position)
                elif move == 's' and self.current_room.grid.get_position()[0] != 4:
                    current_position = self.current_room.grid.get_position()
                    current_position[1] = current_position[1] - 1
                    self.current_room.grid.move(current_position)
                elif move == 'a' and self.current_room.grid.get_position()[1] != 0:
                    current_position = self.current_room.grid.get_position()
                    current_position[0] = current_position[0] - 1
                    self.current_room.grid.move(current_position)
                elif move == 'd' and self.current_room.grid.get_position()[1] != 4:
                    current_position = self.current_room.grid.get_position()
                    current_position[0] = current_position[0] + 1
                    self.current_room.grid.move(current_position)
                #Picking up items
                if self.current_room.grid.is_item():
                    item = self.current_room.grid.get_item()
                    print(f'You obtained {item}.')
                    self.player1.add_item(item)
                    self.current_room.grid.remove_item()
            #Combat Start
            elif self.current_room.grid.is_encounter():
                #Determine turn order
                player_list = [
                    self.player1, self.player2, self.player3, self.player4
                ]
                enemy_list = self.current_room.grid.get_enemies()
                turn_order = []
                i = 0
                while len(player_list) != 0 and len(enemy_list) != 0:
                    if player_list[i] != None:
                        turn_order.append(player_list[i])
                    turn_order.append(enemy_list[i])
                    player_list.pop(i)
                    enemy_list.pop(i)
                    i += 1
                #Combat
                player_list = [self.player1, self.player2, self.player3, self.player4]
                enemy_list = self.current_room.grid.get_enemies()
                k = 0
                while not defeat(player_list) and not victory(enemy_list):
                    active_character = turn_order[k % (len(turn_order) - 1)]
                    if active_character.has_status('sleeping'):
                        active_character.display_is_asleep()
                        k = k + 1
                        continue
                    active_character.display_turn()
                    if active_character in enemy_list:
                        target = random.choice(player_list)
                        if active_character.has_status('corrupted'):
                            target = random.choice(turn_order)
                        active_character.attack(target)
                    elif active_character in player_list:
                        target = None
                        action = active_character.prompt_action()
                        if active_character.has_status('corrupted'):
                            target = random.choice(turn_order)
                            action = 'attack'
                        if action == 'attack':
                            if target == None:
                                print('Choose an enemy to target.')
                                continue
                            skill = active_character.prompt_attack()
                            while skill not in ['1', '2', '3', 'back']:
                                print(f"Please select a valid action. Got {skill}.")
                                skill = active_character.prompt_attack()
                            if skill == 'back':
                                continue
                            else:
                                active_character.attack(target, skill)
                        elif action.lower() == 'target':
                            target = enemy_list[active_character.target() - 1]
                            continue
                        elif action.lower() == 'check':
                            check = active_character.prompt_check()
                            while check not in ['back', 'enemy', 'party']:
                                print(f'Please select a valid action. Got {check}.')
                                check = active_character.prompt_check()
                            if check == 'enemy':
                                for enemy in enemy_list:
                                    enemy.get_stats()
                            elif check == 'party':
                                for ally in player_list:
                                    ally.get_stats()
                            continue
                        elif action.lower() == 'item':
                            active_character.display_inventory()
                            if active_character.is_use_item(self):
                                active_character.use_item()
                            continue
                        else:
                            print(f'Please select a valid action. Got {action}.')
                            continue
                    #Remove defeated characters
                    for character in turn_order:
                        if character.is_defeated():
                            turn_order.remove(character)
                        if character in enemy_list:
                            enemy_list.remove(character)
                        elif character in player_list:
                            player_list.remove(character)
                    #Reduce count of status effects
                    active_character.remove_status()
                    k = k + 1
                if defeat(player_list):
                    self.gameOver = True
                    #Defeat message
                elif victory(enemy_list):
                    #Victory message
                    self.current_room.grid.clear_tile()
                    break
            elif self.current_room.is_boss():
                boss = self.current_room.get_boss()
                boss.encounter()
                #Determine turn order
                player_list = [
                    self.player1, self.player2, self.player3, self.player4
                ]
                enemy_list = [boss]
                turn_order = []
                i = 0
                while len(player_list) != 0 and len(enemy_list) != 0:
                    if player_list[i] != None:
                        turn_order.append(player_list[i])
                    else:
                        player_list.pop(i)
                    turn_order.append(enemy_list[i])
                    i += 1
                while not defeat(player_list) and not victory(enemy_list):
                    if active_character.has_status('sleep'):
                        active_character.display_is_asleep()
                        k = k + 1
                        continue
                    active_character = turn_order[k % (len(turn_order) - 1)]
                    active_character.display_turn()