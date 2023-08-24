import random
import data


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
            while character not in [
                    'freddy', 'chica', 'bonnie', 'foxy', 'skip'
            ]:
                print(
                    f"Please select a valid animatronic or finish party by entering 'skip'. Got {character}."
                )
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
            elif character == 'foxy':
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
                if self.current_room.grid.get_position() == [
                        0, 2
                ] and move == 'w' and self.current_room.is_next_room(move):
                    self.current_room = self.current_room.next_room(move)
                    self.current_room.grid.move([4, 2])
                    continue
                elif self.current_room.grid.get_position() == [
                        2, 0
                ] and move == 'a' and self.current_room.is_next_room(move):
                    self.current_room = self.current_room.next_room(move)
                    self.current_room.grid.move([2, 4])
                    continue
                elif self.current_room.grid.get_position() == [
                        4, 2
                ] and move == 's' and self.current_room.is_next_room(move):
                    self.current_room = self.current_room.next_room(move)
                    self.current_room.grid.move([0, 2])
                    continue
                elif self.current_room.grid.get_position() == [
                        2, 4
                ] and move == 'd' and self.current_room.is_next_room(move):
                    self.current_room = self.current_room.next_room(move)
                    self.current_room.grid.move([2, 0])
                    continue
                #moving in current room
                if move == 'w' and self.current_room.grid.get_position(
                )[0] != 0:
                    current_position = self.current_room.grid.get_position()
                    current_position[1] = current_position[1] + 1
                    self.current_room.grid.move(current_position)
                elif move == 's' and self.current_room.grid.get_position(
                )[0] != 4:
                    current_position = self.current_room.grid.get_position()
                    current_position[1] = current_position[1] - 1
                    self.current_room.grid.move(current_position)
                elif move == 'a' and self.current_room.grid.get_position(
                )[1] != 0:
                    current_position = self.current_room.grid.get_position()
                    current_position[0] = current_position[0] - 1
                    self.current_room.grid.move(current_position)
                elif move == 'd' and self.current_room.grid.get_position(
                )[1] != 4:
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
                    i = i + 1
                #Combat
                player_list = [
                    self.player1, self.player2, self.player3, self.player4
                ]
                enemy_list = self.current_room.grid.get_enemies()
                k = 0
                while not data.is_defeat(player_list) and not data.is_victory(
                        enemy_list):
                    active_character = turn_order[(k % len(turn_order))]
                    if active_character.has_status('Sleeping'):
                        print(f"{active_character.name} is asleep.")
                        k = (k + 1) % len(turn_order)
                        continue
                    active_character.display_turn()
                    if active_character in enemy_list:
                        target = random.choice(player_list)
                        if active_character.has_status('Corrupted'):
                            target = random.choice(turn_order)
                        active_character.attack(target)
                    elif active_character in player_list:
                        target = None
                        action = active_character.prompt_action()
                        if active_character.has_status('Corrupted'):
                            target = random.choice(turn_order)
                            active_character.attack(target, '1')
                            k = (k + 1) % len(turn_order)
                            continue
                        if action == 'attack':
                            if target == None:
                                print('Choose an enemy to target.')
                                continue
                            skill = active_character.prompt_attack()
                            while skill not in ['1', '2', '3', 'back']:
                                print(
                                    f"Please select a valid action. Got {skill}."
                                )
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
                                print(
                                    f'Please select a valid action. Got {check}.'
                                )
                                check = active_character.prompt_check()
                            if check == 'enemy':
                                for enemy in enemy_list:
                                    enemy.get_stats()
                            elif check == 'party':
                                for ally in player_list:
                                    ally.get_stats()
                            continue
                        elif action.lower() == 'item':
                            is_use = active_character.is_use_item()
                            while is_use not in ['y', 'n']:
                                print("Type 'Y' or 'N'.")
                                is_use = active_character.is_use_item()
                            if is_use == 'y':
                                while active_character.is_use_item() == 'y':
                                    active_character.display_inventory()
                                    item = input('Choose an item to use: ')
                                    used = active_character.use_item(item)
                                    if used:
                                        k = (k + 1) % len(turn_order)
                                        break
                            continue
                        else:
                            print(
                                f'Please select a valid action. Got {action}.')
                            continue
                    #Remove defeated characters
                    for character in turn_order:
                        if character.is_defeated():
                            if k >= turn_order.index(character):
                                k = k - 1
                            print(f"{character.name} has died.")
                            turn_order.remove(character)
                        if character in enemy_list:
                            enemy_list.remove(character)
                        elif character in player_list:
                            player_list.remove(character)
                    #Reduce count of status effects
                    active_character.remove_status()
                    #Check if victory or defeat
                    if data.is_defeat(player_list):
                        self.gameOver = True
                        print(
                            "Party defeated. Looks like you'll forgotten, just like the other animatronics down here who met their demise."
                        )
                        break
                    elif data.is_victory(enemy_list):
                        print('Encounter survived.')
                        self.current_room.grid.clear_tile()
                        break
                    #Next Turn
                    k = (k + 1) % len(turn_order)
            elif self.current_room.is_boss():
                #Boss Fight
                self.boss.encounter()
                #Determine turn order
                player_list = [
                    self.player1, self.player2, self.player3, self.player4
                ]
                enemy_list = [self.boss]
                turn_order = []
                i = 0
                while len(player_list) != 0 and len(enemy_list) != 0:
                    if player_list[i] != None:
                        turn_order.append(player_list[i])
                    turn_order.append(enemy_list[i])
                    player_list.pop(i)
                    enemy_list.pop(i)
                    i = i + 1
                #Combat
                player_list = [
                    self.player1, self.player2, self.player3, self.player4
                ]
                enemy_list = [self.boss]
                k = 0
                while not data.is_defeat(player_list) and not data.is_victory(
                        enemy_list):
                    active_character = turn_order[k % (len(turn_order))]
                    if active_character.has_status('Sleeping'):
                        print(f"{active_character.name} is asleep.")
                        k = (k + 1) % len(turn_order)
                        continue
                    active_character.display_turn()
                    if active_character in enemy_list:
                        target = random.choice(player_list)
                        if active_character.has_status('Corrupted'):
                            target = random.choice(turn_order)
                        active_character.attack(target)
                    elif active_character in player_list:
                        target = None
                        action = active_character.prompt_action()
                        if active_character.has_status('Corrupted'):
                            target = random.choice(turn_order)
                            active_character.attack(target, '1')
                            k = (k + 1) % len(turn_order)
                            continue
                        if action == 'attack':
                            if target == None:
                                print('Choose an enemy to target.')
                                continue
                            skill = active_character.prompt_attack()
                            while skill not in ['1', '2', '3', 'back']:
                                print(
                                    f"Please select a valid action. Got {skill}."
                                )
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
                                print(
                                    f'Please select a valid action. Got {check}.'
                                )
                                check = active_character.prompt_check()
                            if check == 'enemy':
                                for enemy in enemy_list:
                                    enemy.get_stats()
                            elif check == 'party':
                                for ally in player_list:
                                    ally.get_stats()
                            continue
                        elif action.lower() == 'item':
                            is_use = active_character.is_use_item()
                            while is_use not in ['y', 'n']:
                                print("Type 'Y' or 'N'.")
                                is_use = active_character.is_use_item()
                            if is_use == 'y':
                                while active_character.is_use_item() == 'y':
                                    active_character.display_inventory()
                                    item = input('Choose an item to use: ')
                                    used = active_character.use_item(item)
                                    if used:
                                        k = (k + 1) % len(turn_order)
                                        break
                        else:
                            print(
                                f'Please select a valid action. Got {action}.')
                            continue
                    #Remove defeated characters
                    for character in turn_order:
                        if character.is_defeated():
                            if k >= turn_order.index(character):
                                k = k - 1
                            turn_order.remove(character)
                            print(f"{character.name} has died.")
                        if character in enemy_list:
                            enemy_list.remove(character)
                        elif character in player_list:
                            player_list.remove(character)
                    #Reduce count of status effects
                    active_character.remove_status()
                    if data.is_defeat(player_list):
                        self.gameOver = True
                        print(
                            "Party defeated. Looks like you'll forgotten, just like the other animatronics down here who met their demise."
                        )
                        break
                    elif data.is_victory(
                            enemy_list) and self.boss.name == 'Springtrap':
                        #Initiate phase 2
                        self.boss = data.Glitchtrap()
                        self.boss.spawn()
                        enemy_list = [self.boss]
                        turn_order.insert(1, enemy_list[0])
                        k = 0
                        continue
                    elif data.is_victory(
                            enemy_list) and self.boss.name == 'Glitchtrap':
                        self.gameOver = True
                        data.Ending()
                    k = (k + 1) % len(turn_order)
