<<<<<<< Updated upstream
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
        options = ["Run!", "Fight!",f"Confront{self.name}!"]
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

=======
from random import randrange,randint
import time
from tkinter import *
from Ratata import Rat
DIALOG_KEY = "dialog"
OPTION_KEY = "options"

class Cat:
    def __init__(self,name="Tom"):
        self.game_window = Tk()
        self.game_window.geometry("1000x600")
        self.game_window.title("CAT HUNTING !!!")

        self.cat_hunt = False
        self.level = 10
        self.name = name
        self.health = self.level*100
        self.dialog = ""
        self.combat = False # True if battling the cat, false if running away from the cat
        self.sequence = []
        self.player = object()
        self.check = 1

    def time_to_hunt(self):
        self.cat_hunt = True
        pass #the cat can smell the rat( player ) hunt is on
#====================================================================================
    def encounter(self,player):
        self.player = player
        self.dialog = f"{self.name} found you!!! Choose to Run, Fight or Confront"
        options = ["Run!", "Fight!",f"Confront{self.name}!"]
        ls_func = [self.run_from_cat,self.fight_cat,self.confront_cat]
        return self.dialog, options, ls_func
#====================================================================================
    def run_from_cat(self): return self.player
    
    def memory_game_init_(self): # run from cat
        self.sequence = [randrange(4) for i in range(self.level*2)]
#====================================================================================
    def confront_cat(self): 
        self.dialog = f"You tried to confront the cat, but {self.name} is hungry, You are now forced to fight the cat"
        self.fight_cat()
    def fight_cat(self):
        self.make_run_game()
        self.game_start()
        print (self.player)
        return self.player
#====================================================================================
    def rat_minus_hp(self):
        self.player.health-=self.level
        self.dialog = f"You have taken {self.level} damage, You have {self.player.health} left!"
    def cat_minus_hp(self):
        self.health-=self.player.size
        self.dialog = f"You have dealt {self.player.size} damage. The Cat have {self.health} left!"
#====================================================================================
    def game_start(self): self.game_window.mainloop()
    def game_end(self): self.game_window.destroy()
    def check_sequence(self,btn,n):
        btn.destroy()
        if self.check>=10:
            for widget in self.game_window.winfo_children():widget.destroy()
            self.game_end()
        elif n==self.check: self.check+=1
        else: # Wrong restart
            self.rat_minus_hp()
            for widget in self.game_window.winfo_children():widget.destroy() 
            self.make_run_game()
    def make_run_game(self):
        numbers = [str(i) for i in range(1,self.level+1)]
        self.check=1
        def place_button(canvas, btn):
            '''place a label on a canvas in a random, non-overlapping location'''
            width = btn.winfo_reqwidth()
            height = btn.winfo_reqheight()
            tries = 0
            while True and tries < 1000:
                tries += 1 # failsafe, to prevent an infinite loop
                x = randint(0, 1000-width)
                y = randint(0, 600-height)
                items = canvas.find_overlapping(x, y, x+width, y+height)
                if len(items) == 0:
                    canvas.create_window(x, y, window=btn, anchor="nw")
                    break
        canvas = Canvas(self.game_window, width=1000, height=600)
        canvas.pack(fill="both", expand=True)
        _f_ = 20
        btn1 = Button(self.game_window,text=numbers[0],font=_f_,width=20,height=5,fg="white",bg="black",command=lambda:self.check_sequence(btn1,1))
        place_button(canvas, btn1)
        btn2 = Button(self.game_window,text=numbers[1],font=_f_,width=20,height=5,fg="white",bg="black",command=lambda:self.check_sequence(btn2,2))
        place_button(canvas, btn2)
        btn3 = Button(self.game_window,text=numbers[2],font=_f_,width=20,height=5,fg="white",bg="black",command=lambda:self.check_sequence(btn3,3))
        place_button(canvas, btn3)
        btn4 = Button(self.game_window,text=numbers[3],font=_f_,width=20,height=5,fg="white",bg="black",command=lambda:self.check_sequence(btn4,4))
        place_button(canvas, btn4)
        btn5 = Button(self.game_window,text=numbers[4],font=_f_,width=20,height=5,fg="white",bg="black",command=lambda:self.check_sequence(btn5,5))
        place_button(canvas, btn5)
        btn6 = Button(self.game_window,text=numbers[5],font=_f_,width=20,height=5,fg="white",bg="black",command=lambda:self.check_sequence(btn6,6))
        place_button(canvas, btn6)
        btn7 = Button(self.game_window,text=numbers[6],font=_f_,width=20,height=5,fg="white",bg="black",command=lambda:self.check_sequence(btn7,7))
        place_button(canvas, btn7)
        btn8 = Button(self.game_window,text=numbers[7],font=_f_,width=20,height=5,fg="white",bg="black",command=lambda:self.check_sequence(btn8,8))
        place_button(canvas, btn8)
        btn9 = Button(self.game_window,text=numbers[8],font=_f_,width=20,height=5,fg="white",bg="black",command=lambda:self.check_sequence(btn9,9))
        place_button(canvas, btn9)
        btn10 = Button(self.game_window,text=numbers[9],font=_f_,width=20,height=5,fg="white",bg="black",command=lambda:self.check_sequence(btn10,10))
        place_button(canvas, btn10)

tommy = Cat()
jerry = Rat()
tommy.encounter(jerry)
tommy.fight_cat()
print(jerry.health)
>>>>>>> Stashed changes
