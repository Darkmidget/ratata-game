import math
import time
from Ratata import Rat
import random

#Action 1
def fight_rat(rat):

    #dialogue = "You sense an enemy Rat. Prepare to fight."
    win = True if random.random() <=0.3 + len(rat.rat_gang)/20 else False

    if win:
        rat.belongings["cheese"] += 1
        return rat
    else:
        rat.rat_gang.clear()
        rat.health -=10
        return rat
    
#Action 2
def befriend_rat(rat):

    #dialogue = "You decided to help a fellow rat, give one cheese."
    rat.belongings["cheese"] -=1
    rat.rat_gang.append("rat friend")
    return rat
  
#Action 3
def steal_cheese(rat):

    #dialogue = "You're a slick rat, you attempt to steal its cheese right under its snout."
    win = True if random.random() <=0.3 else False

    if win:
        rat.belongings["cheese"] +=1
        return rat
    else:
        #lose_steal_dialogue = "Too bad, you found nothing! Your efforts have been in vain!"
        return rat
#Action 4
def ignore(rat):

    #dialogue = "You continue on your journey, oblivious to your surroundings."
    return rat

#i have no idea what the fk im doing
class OtherRat():

    def __init__(self):
       self.player = object()
       
    
    def rat_encounter(self,player):

        self.player = player
        dialogue = ["You sense an enemy rat, prepare to fight."]
        options = ["Fight Rat : +1 Cheese or -10 HP and Gang flee: Success based on Gang Size", "Befriend Rat : + 1 Gang Member : -1 Cheese", "Steal Cheese : + 1 Chess : 30% Success", "Ignore"]
        option_func = [fight_rat, befriend_rat, steal_cheese, ignore]
        return dialogue, options, option_func
    
    
    

jerry = Rat() 
rat_gang = OtherRat()
#testing corner


# rat_gang.rat_encounter(jerry)
# count = 0
# while True:
#     rat_gang.fight_rat()
#     jerry.belongings["cheese"]
#     count += 1
#     if jerry.belongings["cheese"] == 6:
#         break
    

# print(jerry.belongings["cheese"],count)