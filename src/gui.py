import time
import tkinter as tk
from tkinter import messagebox
from Ratata import Rat
from RatRandomiser import event

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

        self.pause_brain = False
        # self.last_time = time.time_ns()

        self.option_buttons = []
        # Creating buttons
        for _ in range(4):
            button = tk.Button(self.master, text="", font=("Helvetica", 12))
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

    def brain(self, delay = 0.1):
        """Main brain"""
        if not self.pause_brain:
            self.pause_brain = True
            try:
                display_params = event(self.rat)
                self.update_display(*display_params)
                time.sleep(1) # Slows down the speed at which new dialogues are shown
            except:
                print(f"ERROR\n-------\n")
                print(event(self.rat))

            
            # for key, value in vars(self.rat).items():
            #     print(f"{key}: {value}")
        self.master.after(100, self.brain)

    def clear_display(self):
        """Clears all display"""
        pass

    def update_display(self, *args):
        """*args = (dialogues, options, functions, more_dialogue). 
        more_dialogue is for when the NPC will give more dialogue to your action."""
        self.clear_display()

        dialogues = args[0]
        options = args[1]
        functions = args[2]

        if len(args) == 4: 
            more_dialogues = args[3]
            self.update_dialogue(dialogues)
            self.update_option_buttons(options, functions, more_dialogues) # Updates the dialogue when player chooses whatever option
            self.update_stats()
        elif len(args) == 3:
            self.update_dialogue(dialogues)
            self.update_option_buttons(options, functions)
            self.update_stats()
        
    def update_dialogue(self, dialogues):
        self.dialogue_text = ""
        for dialogue in dialogues:
            self.dialogue_text += dialogue
        self.dialogue_label.config(text=self.dialogue_text, font=("Helvetica", 12))

        # current_time = time.time_ns()
        # print(f"Previous dialogue lasts for: {(current_time - self.last_time)*10e-9}")
        # self.last_time = current_time

    def update_stats(self):
        stats_text = "Rat Stats:\n"
        for key, value in self.rat.__dict__.items():
            stats_text += f"{key}: {value}\n"
        self.stats_label.config(text=stats_text, font=("Helvetica", 12))

    def update_option_buttons(self, options, *args):
        """Changes stats of rat and print out more dialogues if available"""
        functions = args[0]
        
        # Updating buttons
        for index, option in enumerate(options):
            # Combines functions and update(more_dialogues[idx]) into one lambda function
            if len(args) == 2:
                more_dialogues = args[1]
                combined_functions = lambda idx = index: [self.handle_option(functions[idx]), self.update_dialogue(more_dialogues[idx])]
            else:
                combined_functions = lambda idx = index: self.handle_option(functions[idx])
            
            self.option_buttons[index].config(text=option, command=combined_functions)
            

    def handle_option(self, function):
        """When pressed, return 1,2,3 or 4"""
        # print(f"function here\n----------\n{function}")
        self.pause_brain = False # Allow a new event to run
        self.rat = function(self.rat)

if __name__ == "__main__":
    root = tk.Tk()
    app = RatGameApp(root)
    app.master.after(500, app.brain)
    app.master.mainloop()