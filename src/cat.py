from random import randrange
from Ratata import Rat
import time
DIALOG_KEY = "dialog"
OPTION_KEY = "options"

class Cat:
    def __init__(self,name="Tom"):
        self.cat_hunt = False
        self.level = 1
        self.cat_name = name
        self.health = self.level*100
        self.dialog = ""
        self.combat = False # True if battling the cat, false if running away from the cat
        self.sequence = []
        self.player = object()

    def time_to_hunt(self):
        self.cat_hunt = True
        pass
        #the cat can smell the rat( player ) hunt is on

    def encounter(self,player):
        self.player = player
        self.dialog = [f"{self.cat_name} found you!!! Choose to Run, Fight or Comfront"]
        options = ["Run!", "Fight!",f"Confront{self.cat_name}!"]
        ls_func = [self.run_from_cat,self.run_from_cat,self.confront_cat]
        return self.dialog, options, ls_func

    def run_from_cat(self):
        pass
    def fight_cat(self):
        func = self.minus_hp
        options = [func,func,func,func]
        options[randrange(4)] = self.cat_minus_hp
        return self.dialog,options

    def memory_game_init_(self): # run from cat
        self.sequence = [randrange(4) for i in range(self.level*2)]

    def speed_game(self): # combat cat
        pass

    def confront_cat(self):
        self.dialog = f"You tried to confront the cat, but {self.name} is hungry, You are now forced to fight the cat"
        self.fight_cat()
    def rat_minus_hp(self):
        self.dialog = f"You have taken {self.level} damage, You have {self.player.health} left!"
        self.interact()
    def cat_minus_hp(self):
        self.health-=self.player.size
        self.dialog = f"You have dealt {self.player.size} damage. The Cat have {self.health} left!"
        self.interact(self.player)

