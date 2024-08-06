import script

class interface:

    def start_menu(self):
        print(script.start_menu['title'])
        [print(f"{num+1}: {value}") for num, value in enumerate(script.start_menu["options"])]
        choice = int(input(script.prompt))
        return script.start_menu['options'][choice - 1]
    
    def room_menu(self):
        
        [print(f"{num+1}: {value}") for num, value in enumerate(script.room_menu["options"])]

    # def exit_screen():
    #     print()



UI = interface()
print(UI.start_menu())

