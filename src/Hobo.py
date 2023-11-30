from dialogue import interact_handler 
from Ratata import Rat 
from time import sleep 
import time 
 
class Hobo(): 
    def __init__(self): 
        self.encounter = 0
        self.cheese = 1 
         
    def hobo_encounter(self,r): 
        self.encounter+=1 
        return self.hobo_interact(r) 
        #if self.cheese > 8 
         
        # encounter logic and also cheese logic 
        #return rat dialogue, options 
        # take in rat object and change its stats and return the rat to qx 
        # return dialog,player/rat, options 
        # maybe we should implement storyline where the rat interacts with the hobo idk  
        # make sure hobo hints that he can just come back next time to deliver many cheese 
    def hobo_interact(self,r): 
        # Functions to do what you will do to the rat/hobo 
        def hobo_take(self,r): #take cheese from hobo 
            r.belongings["cheese"] += 1 
            self.cheese -= 1 
            print("Hobo:I will get going now. Have fun exploring and stay safe from those pesky cats.") 
            return r 
         
        def hobo_eat(r):#eat cheese from hobo 
            eatcheese(r) 
            print("you have eaten the cheese and thank him byebye") 
            return r  
         
        def hobo_leave(self,r): #decline/leave 
            if self.encounter == 1:  
                print("You thanked the hobo for his kind gesture but declined his cheese.") 
                time.sleep(.5) 
                print("Hobo was dissapointed, waves goodbye and left to explore the sewers.") 
                return r 
            if self.encounter != 1: 
                print("You waved goodbye with your little paws.") 
                time.sleep(.5) 
                print("Hobo looks forward to meeting you again.") 
 
                return r 
            return r  
         
        def hobo_give(self,r): #rat give cheese 
            if r.belongings["cheese"]>=1: 
                r.belongings["cheese"] -= 1 
                self.cheese += 1 
                if self.cheese >= 1: 
                    print("Hobo is delighted to received your gift and promises to return the favour in the future") 
                elif self.cheese == 4: 
                    print("Hobo is  thankful for your past gifts and handed you a strong Health Potion. Your hp increased and stuff") 
                    rat.health += 20 
                elif self.cheese >4: 
                    print("Hobo  accepted your gift and left...") 
                elif self.cheese == 6: 
                    print("Excited hobo gives u golden cheese lmao") 
                return r 
            else: print("As you have no cheese, Hobo expressed his dissapointment and left.") 
        def hobo_share(self,r): 
            if r.rat_gang >= 1: 
                print("You shared your story on how you gather your gang rat members.") 
                time.sleep(0.5) 
                print("Hobo thanked you for the story and left to explore the sewers.") 
            # if ( new implementation that can share) 
 
            return r 
       
        if self.encounter == 1: 
            dialogue = ["Hobo: Oh hello! This is the first time I have seen you around./n Do"] 
            options = ["1. Take cheese ", "2. Eat cheese", "3. Decline"]  
            return dialogue,options, [hobo_take,hobo_eat,hobo_leave] 
        elif self.encounter > 1 and self.encounter < 5: 
            dialogue = [' The hobo is delighted to see you again. He is intrigued to learn of your journey thus far. '] 
            options = ["1. Give cheese", "2. Share more on your story", "3. Leave"] 
            return dialogue,options,[hobo_give,hobo_share,hobo_leave]  
        #elif self.encounter >= 5:  
           # dialogue = [ ''] 
     
def eatcheese(r): 
    r.hunger += 10 
    return(r) 