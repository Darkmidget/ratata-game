import time
import tkinter as tk
from tkinter import messagebox
from Ratata import Rat
from RatRandomiser import event
import copy

## Testing Corner
class RatGameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Ratata")
        self.master.geometry("1200x800")

        self.dialogue_label = tk.Label(master, text="", wraplength=350)
        self.dialogue_label.pack(pady=10)

        self.stats_label = tk.Label(master, text="")
        self.stats_label.pack(pady=10)

        self.options_label = tk.Label(master, text="")
        self.options_label.pack(padx=5)

        self.functions = []

        self.option_buttons = []
        # Creating buttons
        for _ in range(4):
            button = tk.Button(self.master, text="")
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.rat = Rat()

        ### --- Dummy code --- ###
        # dialogues = ["123", "Hello this is me"]
        # options = ["option1", "option2"]
        # functions = [lambda i: i for i in range(2)]
        # self.update_display(dialogues, options, functions)
        # self.brain()
        ### -------------------###

    def brain(self):
        """Main brain"""
        dialogues, options, functions = event(self.rat)
        self.update_display(dialogues, options, functions)
        print("Test")
        # for key, value in vars(self.rat).items():
        #     print(f"{key}: {value}")
        self.master.after(2000, self.brain)

    def empty_func(self):
        return self.rat

    def clear(self):
        """Clear everything please!"""
        pass

    def update_display(self, dialogues, options, functions):
        self.clear()
 
        # Update the labels and buttons
        self.update_dialogue(dialogues)
        self.update_option_buttons(options, functions)
        self.update_stats()
        

    def update_dialogue(self, dialogues):
        self.dialogue_text = ""
        for dialogue in dialogues:
            self.dialogue_text += dialogue
        self.dialogue_label.config(text=self.dialogue_text)

    def update_stats(self):
        stats_text = "Rat Stats:\n"
        for key, value in self.rat.__dict__.items():
            stats_text += f"{key}: {value}\n"
        self.stats_label.config(text=stats_text)

    def update_option_buttons(self, options, functions):    
        # Updating buttons
        self.functions = [self.empty_func for _ in range(4)]
        for index, option in enumerate(options):
            if index == 0:
                self.functions[0] = functions[0]
            elif index == 1:
                self.functions[1] = functions[1]
            elif index == 2:
                self.functions[2] = functions[2]
            elif index ==3:
                self.functions[3] = functions[3]
            function = copy.deepcopy(functions[index])
            print(index)
            self.option_buttons[index].config(text=option, command=lambda: self.handle_option(self.functions[index]))
            # print(self.option_buttons.__dir__())

    def handle_option(self, function):
        """When pressed, return 1,2,3 or 4"""
        # print(vars(self.rat))
        print(function)
        # print(function1)
        self.rat = function(self.rat)
        # print(vars(self.rat))


if __name__ == "__main__":
    root = tk.Tk()
    app = RatGameApp(root)
    app.master.after(500, app.brain)
    app.master.mainloop()