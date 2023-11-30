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

        ### --- Dummy code --- ###
        dialogues = ["123", "Hello this is me"]
        self.rat = Rat()
        options = ["option1", "option2"]
        self.update_display(dialogues, self.rat, options)
        ### -------------------###

    def clear(self):
        pass

    def update_display(self, dialogues, options):
        self.clear()

        self.dialogue_text = ""
        for dialogue in dialogues:
            self.dialogue_text += dialogue

        # Update the labels
        self.update_dialogue()
        self.update_stats()

    def update_dialogue(self):
        self.dialogue_label.config(text=self.dialogue_text)

    def update_stats(self, rat):
        stats_text = "Rat Stats:\n"
        for key, value in rat.__dict__.items():
            stats_text += f"{key}: {value}\n"
        self.stats_label.config(text=stats_text)

    def create_option_buttons(self, options, functions):
        self.option_buttons = []
        for index, option in enumerate(options):
            button = tk.Button(self.master, text=option, command=self.handle_option(index+1, functions(index)))
            button.pack(pady=5)
            self.option_buttons.append(button)

    def handle_option(self, option_number, function):
        """When pressed, return 1,2,3 or 4"""
        self.rat = function(self.rat)


if __name__ == "__main__":
    root = tk.Tk()
    app = RatGameApp(root)
    root.mainloop()