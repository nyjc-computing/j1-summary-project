import tkinter as tk
import random



class Game:

    def __init__(self):
        with open("settings.txt", "r") as f:
            out = f.readlines()
            out = [x.split()[1] for x in out]
        self.selfsleep = int(out[0])
        self.selfup = out[1]
        self.selfdown = out[2]
        self.selfreturn = out[3]
        self.line = 1
        self.taglines = []

    def reapply_tag(self):
        for tag in self.text.tag_names():
            self.text.tag_delete(tag)

        for i, line in enumerate(self.taglines):
            color, start, end = line
            self.text.tag_add(f"colour{i}", start, end)
            self.text.tag_config(f"colour{i}", foreground=color)

    def sleep(self, t):
        self.root.after(int(t*1000), lambda: self.sleepCount.set(self.sleepCount.get()+1))
        self.root.wait_variable(self.sleepCount)
    
    def write(self, txt=""):
        self.text['state'] = 'normal'
        self.text.insert(tk.END, txt+"\n")
        self.text['state'] = 'disabled'
        self.line += 1

    def write_color(self, txt, color):
        """
        writes red to the text field in red

        the colors rely on the line tracker which only increments by 1
        for each thing you write pls pls pls do not use newline characters
        """
        self.text['state'] = 'normal'
        self.text.insert(tk.END, txt+"\n")

        self.taglines.append([color, f"{self.line}.0", f"{self.line}.end"])
        self.text['state'] = 'disabled'
        self.line += 1
        self.reapply_tag()
    
    def delete(self):
        self.text['state'] = 'normal'
        self.text.delete("1.0", tk.END)
        self.text['state'] = 'disabled'
        self.line = 1
        self.taglines = []
    
    def wait_for_key_press(self):
        self.write("\nPress any key to continue")
        self.root.bind('<Key>', lambda x: self.pause_var.set("done"))
        self.root.wait_variable(self.pause_var)
        self.root.unbind('<Key>')
        self.pause_var.set("")
        
    def show(self, prompt, options, deletebefore):
        data = self.text.get("1.0",'end-1c')
        self.delete()
        keep = ""
        if not deletebefore:
            keep = data.split(prompt)[0]
            
        """main action for user to get the list of possible actions"""
        # Displays the list of actions the user can do
        p = self.pointer.get()
        self.write(keep+prompt+"\n")
        for i, e in enumerate(options):
            arrow = " "
            if p == i: arrow = ">"
            self.write(f"{arrow} {e}")
            
    def up_action(self, prompt, options, delete):
        p = self.pointer.get()
        if p != 0:
            self.pointer.set(p-1)
        else:
            self.pointer.set(len(options)-1)
    
        self.show(prompt, options, self.delete)
    
    def down_action(self, prompt, options, delete):
        p = self.pointer.get()
        if p != len(options)-1:
            self.pointer.set(p+1)
        else:
            self.pointer.set(0)
    
        self.show(prompt, options, self.delete)
    
    def get_input(self, prompt, options, displayoptions = None, deletebefore = True):
        """sub action for run() that prompts user for a main action"""
        if displayoptions is None:
            displayoptions = options
        self.show(prompt, displayoptions, deletebefore)
        self.root.bind(f'<{self.selfreturn}>', lambda x: self.pause_var.set("done"))
        self.root.bind(f"<{self.selfup}>", lambda e: self.up_action(prompt, displayoptions, deletebefore))
        self.root.bind(f"<{self.selfdown}>", lambda e: self.down_action(prompt, displayoptions, deletebefore))
        self.root.wait_variable(self.pause_var)
        self.root.unbind(f'<{self.selfreturn}>')
        self.root.unbind(f"<{self.selfup}>")
        self.root.unbind(f"<{self.selfdown}>")
        self.pause_var.set("")
        decision = options[self.pointer.get()]
        self.pointer.set(0)
        self.delete()
        return decision

    def get_bet(self):
        amount = 1
        bets = []
        while self.player.money >= amount:
            bets.append(str(amount))
            amount *= 10

        bets.append("Cancel")

        bet = self.get_input("How much would you like to bet?", bets)

        return bet
    
class JanKenPon(Game):
    def __init__(self, player, root, text):
        super().__init__()
        self.root = root
        self.text = text
        self.player = player
        self.pause_var = tk.StringVar()
        self.pointer = tk.IntVar()
        self.sleepCount = tk.IntVar()

    def play(self):
        bet = self.get_bet()

        if bet == "Cancel":
            self.delete()
            
        else:
            moves = ["Rock", "Paper", "Scissors"]
            selection = self.get_input("What do you want to use?", moves)
            opponent_selection = random.choice(moves)
            if selection == opponent_selection:
                self.write(f"The opponent also used {selection}, its a draw")
                self.sleep(self.selfsleep)
                self.write()
                self.write(f"You get back {bet} runes")
                self.wait_for_key_press()
                self.delete()

            elif (selection == "Rock" and opponent_selection == "Paper") or (selection == "Paper" and opponent_selection == "Scissors") or (selection == "Scissors" and opponent_selection == "Rock"):
                self.write_color(f"The opponent used {opponent_selection}, you lost", "red")
                self.sleep(self.selfsleep)
                self.write()
                self.write(f"You lost {bet} runes")
                self.player.money -= int(bet)
                self.wait_for_key_press()
                self.delete()
            
            else:
                self.write_color(f"The opponent used {opponent_selection}, you won", "green")
                self.sleep(self.selfsleep)
                self.write()
                self.write(f"You earned {bet} runes")
                self.player.money += int(bet)
                self.wait_for_key_press()
                self.delete()

class Blackjack(Game):

    def __init__(self, player, root, text):
        super().__init__()
        self.root = root
        self.text = text
        self.player = player
        self.pause_var = tk.StringVar()
        self.pointer = tk.IntVar()
        self.sleepCount = tk.IntVar()

    def play(self):
        bet = self.get_bet()

        if bet == "Cancel":
            self.delete()

        else:
            pass