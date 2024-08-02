import script

class interface:

    def start_menu(self):
        print(script.start_menu['title'])
        [print(f"{num+1}: {value}") for num, value in enumerate(script.start_menu["options"])]
        print(script.prompt)

    def exit_screen():
        print()





UI = interface()
UI.start_menu()
