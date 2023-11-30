import math 

DIALOG_KEY = "dialog"
OPTION_KEY = "options"

class Cat:
    def __init__(self,name="Tom"):
        self.cat_hunt = False
        self.level = 1
        self.cat_name = name

        
    def time_to_hunt(self):
        self.cat_hunt = True
        pass
        #the cat can smell the rat( player ) hunt is on

    def encounter(self, player):
        dialog = [f"{self.cat_name} found you!!! Choose to Run, Fight or Comfront"]
        options = ["Run!", "Fight!",f"Confront{self.name}!"]
        return dialog, player, options
    
    def run_from_cat(self):
        pass

    def fight_cat(self):
        pass
    def confront_cat(self):
        dialog = f"You tried to confront the cat, but {self.name} is hungry, You are now forced to fight the cat"

    def won(self):
        pass
    def lose(self):
        pass