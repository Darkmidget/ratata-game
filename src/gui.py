import time
import tkinter as tk
from tkinter import messagebox
from Ratata import Rat

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

        self.rat = Rat()
        ### --- Dummy code --- ###
        dialogues = ["123", "Hello this is me"]
        options = ["option1", "option2", "option3"]
        functions = [lambda i: i for i in range(3)]
        self.update_display(dialogues, options, functions)
        ### -------------------###

    def clear(self):
        """Clear everything please!"""
        pass

    def update_display(self, dialogues, options, functions):
        self.clear()
 
        # Update the labels and buttons
        self.update_dialogue(dialogues)
        self.update_stats()
        self.update_option_buttons(options, functions)

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
        self.option_buttons = []
        for index, option in enumerate(options):
            function = functions[index]
            button = tk.Button(self.master, text=option, command=self.handle_option(function))
            button.pack(pady=5)
            self.option_buttons.append(button)

    def handle_option(self, function):
        """When pressed, return 1,2,3 or 4"""
        self.rat = function(self.rat)


if __name__ == "__main__":
    root = tk.Tk()
    app = RatGameApp(root)
    root.mainloop()