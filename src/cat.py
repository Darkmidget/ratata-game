from random import randrange,randint,random
import time
from tkinter import *
from tkinter import ttk
from Ratata import Rat
DIALOG_KEY = "dialog"
OPTION_KEY = "options"

class Cat:
    def __init__(self,name="Tom"):
        self.game_window = Tk()
        self.game_window.geometry("1000x600")
        self.game_window.title("CAT HUNTING !!!")

        self.cat_hunt = False
        self.level = 1
        self.name = name
        self.health = self.level*100
        self.dialog = ""
        self.combat = False # True if battling the cat, false if running away from the cat
        self.sequence = []
        self.player = object()
        self.check = 1
        self.start_timer = 0

    def time_to_hunt(self):
        self.cat_hunt = True
        pass #the cat can smell the rat( player ) hunt is on
#====================================================================================
    def encounter(self,player):
        self.player = player
        self.dialog = f"{self.name}, the cat, found you!!!"
        options = ["Prepare to Fight", f"Befriend {self.name}",f"Run Away from {self.name}!"]
        ls_func = [self.fight_cat,self.confront_cat,self.run_from_cat]
        return self.dialog, options, ls_func
#====================================================================================
    def run_from_cat(self): 
        success = random() < self.level/10
        self.dialog = "You and the Cat make eye contact. You attempt to flee"
        if success:
            self.dialog = "You have gotten away successfully and found some cheese along the way"
            self.level+=1 if self.level<10 else 0
            return self.player
        else: 
            self.rat_minus_hp()
            self.dialog = f"You have failed to run away from {self.name}, the cat. Prepare to battle."
            self.fight_cat()
#====================================================================================
    def confront_cat(self): 
        self.dialog = f"You attempt to befriend the enemy ... what an idiot! You are now forced to fight the cat"
        self.fight_cat()
    def fight_cat(self):
        self.dialog = "You have stumbled upon your mortal nemesis, Prepare to Fight. Click in accending Sequence"
        self.make_run_game()
        self.game_start()
        return self.player
#====================================================================================
    def rat_minus_hp(self):
        self.player.health-=self.level
        self.dialog += f"You have taken {self.level} damage, You have {self.player.health} Hp left!"
    def cat_minus_hp(self):
        self.health-=self.player.size
        self.dialog = f"You have dealt {self.player.size} damage. The Cat have {self.health} left!"
#====================================================================================
    def game_start(self): self.game_window.mainloop()
    def game_end(self):
        self.game_window.destroy()
        return self.player
    def check_sequence(self,btn,n):
        def minus_restart():
            self.rat_minus_hp()
            if self.player.health<=0:
                self.game_end()
                return self.player # rat died
            else:
                for widget in self.game_window.winfo_children():widget.destroy() 
                self.make_run_game()
        btn.destroy()
        end=time.time()
        if (end-self.start_timer)>(10/self.level+1):
            self.dialog = "Too Slow! "
            minus_restart()
        elif self.check>=10:
            for widget in self.game_window.winfo_children():widget.destroy()
            self.game_end()
        elif n==self.check: self.check+=1
        else:
            self.dialog = "You have missed clicked..."
            minus_restart()
            
    def make_run_game(self):
        self.start_timer = time.time()
        numbers = [str(i) for i in range(1,11)]
        self.check=1
        def place_button(canvas, btn):
            '''place a label on a canvas in a random, non-overlapping location'''
            width = btn.winfo_reqwidth()
            height = btn.winfo_reqheight()
            tries = 0
            while True and tries < 1000:
                tries += 1 # failsafe, to prevent an infinite loop
                x = randint(0, 1000-width)
                y = randint(0, 500-height)
                items = canvas.find_overlapping(x, y, x+width, y+height)
                if len(items) == 0:
                    canvas.create_window(x, y, window=btn, anchor="nw")
                    break
        label_dialog = Label(self.game_window,text=self.dialog)
        label_dialog.pack()
        #timer_bar = ttk.Progressbar(self.game_window,orient=HORIZONTAL,length=300,mode='determinate')
        #timer_bar.pack(pady=20)
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
        #timer()

tommy = Cat()
jerry = Rat()
tommy.encounter(jerry)
tommy.fight_cat()
print(jerry.health)

