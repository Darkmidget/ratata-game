from dialogue import interact_handler 
from Ratata import Rat 
from time import sleep 
import time 

def handle_item(rat: Rat, item, num):
    if not item in rat.belongings:
        rat.belongings.update({item : num})
    else:
        rat.belongings[item] = rat.belongings[item] + num
    return rat
 
class Hobo(): 
    def __init__(self): 
        self.encounter = 0
        self.cheese = 1 
         
    
    def hobo_interact(self,r): 
        self.encounter += 1
        # Functions to do what you will do to the rat/hobo 
        def hobo_take(r): #take cheese from hobo 
            handle_item(r,"cheese", 1) 
            self.cheese -= 1 
            # print("Hobo:I will get going now. Have fun exploring and stay safe from those pesky cats.") 
            return r 
         
        def hobo_eat(r):#eat cheese from hobo 
            # print("you have eaten the cheese and thank him byebye") 
            return r  
         
        def hobo_leave(r): #decline/leave 
            if self.encounter == 1:  
                # print("You thanked the hobo for his kind gesture but declined his cheese.") 
                # print("Hobo was dissapointed, waves goodbye and left to explore the sewers.") 
                return r 
            if self.encounter != 1: 
                # print("You waved goodbye with your little paws.") 
                # print("Hobo looks forward to meeting you again.") 
 
                return r 
            return r  
         
        def hobo_give(r): #rat give cheese 
            if not "cheese" in r.belongings or r.belongings['cheese']<1:
                # print("As you have no cheese, Hobo expressed his dissapointment and left.")
                pass              
            elif r.belongings["cheese"]>=1: 
                r.belongings["cheese"] -= 1 
                self.cheese += 1 
                if self.cheese >= 1: 
                    print("Hobo is delighted to received your gift and promises to return the favour in the future") 
                elif self.cheese == 4: 
                    print("Hobo is thankful for your past gifts and handed you a strong Health Potion. Your hp increased and stuff") 
                    r.health += 20 
                elif self.cheese >4: 
                    print("Hobo accepted your gift and left...") 
                elif self.cheese == 6: 
                    print("Excited hobo gives u golden cheese lmao") 
                return r 
            
            return r
        def hobo_share(r): 
            # if r.rat_gang >= 1: 
            #     print("You shared your story on how you gather your gang rat members.") 
            #     time.sleep(0.5) 
            #     print("Hobo thanked you for the story and left to explore the sewers.") 
            # if ( new implementation that can share) 
            pass
 
            return r 
       
        print(self.encounter)
        if self.encounter == 1: 
            dialogue = ["Hobo: Oh hello! This is the first time I have seen you around./n Do"] 
            options = ["1. Take cheese ", "2. Eat cheese", "3. Decline"]
            more_dialogues = ["Yoinking cheese", "Eating Cheese", "No means no"]
            return dialogue,options, [hobo_take,hobo_eat,hobo_leave], more_dialogues
        elif self.encounter > 1: 
            dialogue = [' The hobo is delighted to see you again. He is intrigued to learn of your journey thus far. '] 
            options = ["1. Give cheese", "2. Share more on your story", "3. Leave"] 
            more_dialogues = ["Giving Cheese", "Sharing stories", "The hobo looks forward to seeing you again"]
            return dialogue,options,[hobo_give,hobo_share,hobo_leave], more_dialogues
        return (["Problem Here"], ["THERE IS PROBLEM in JY CODE"], [lambda: 1])
        #elif self.encounter >= 5:  
           # dialogue = [ ''] 
     
# def eatcheese(r): 
#     r.hunger += 10 
#     return(r)