import script


class Interface:
    def prompt(self):
        return script.prompt

    def start_menu(self):
        print(script.start_menu['title'])
        [
            print(f"{num+1}: {value}")
            for num, value in enumerate(script.start_menu["options"])
        ]

    def exit_screen():
        print()


# UI = interface()
# UI.start_menu()
