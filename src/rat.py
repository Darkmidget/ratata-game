import math
import time
from Ratata import Rat
from dialogue import interact_handler
import random

#i have no idea what the fk im doing
class OtherRat():

    def __init__(self):
       self.player = object()
       
    
    def rat_encounter(self,player):

        self.player = player
        dialogue = "You sense an enemy rat, prepare to fight."
        options = ["Fight Rat", "Befriend Rat", "Steal Cheese", "Ignore"]
        #option_func = [fight_rat, befriend_rat, steal_cheese, ignore]
        return dialogue, options, #option_func
    
    #Action 1
    def fight_rat(self):

        dialogue = "You sense an enemy Rat. Prepare to fight."
        win = True if random.random() <=0.6 else False

        if win:
            self.player.belongings["cheese"] +=1
            return self.player
        else:
            self.player.belongings["cheese"] -=1
            self.player.health -=10
            return self.player
    
    #Action 2
    def befriend_rat(self):

        dialogue = "You decided to help a fellow rat, give one cheese."
        self.player.belongings["cheese"] -=1
        return self.player
    
    #Action 3
    def steal_cheese(self):

        dialogue = "You're a slick rat, you attempt to steal its cheese right under its snout."
        win = True if random.random() <=0.3 else False

        if win:
            self.player.belongings["cheese"] +=1
            return self.player
        else:
            lose_steal_dialogue = "Too bad, you found nothing! Your efforts have been in vain!"
            return self.player
    #Action 4
    def ignore(self):

        dialogue = "You continue on your journey, oblivious to your surroundings."
        return self.player
    

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