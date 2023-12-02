import math
import time
from Ratata import Rat
from dialogue import interact_handler
import random

#i have no idea what the fk im doing
class OtherRat():

    def __init__(self):
       self.player = object()
       pass
    
    def rat_encounter(self,player):

        self.player = player
        dialogue = "You sense an enemy rat, prepare to fight."
        options = ["Fight Rat", "Befriend Rat", "Steal Cheese", "Ignore"]
        option_func = [fight_rat, befriend_rat, steal_cheese, ignore]
        return dialogue, options, option_func
    
        #Action 1
        def fight_rat():

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
        def befriend_rat():

            dialogue = "You decided to help a fellow rat, give one cheese."
            self.player.belongings["cheese"] -=1
            return self.player
        
        #Action 3
        def steal_cheese():

            dialogue = "You're a slick rat, you attempt to steal its cheese right under its snout."
            win = True if random.random() <=0.3 else False

            if win:
                self.player.belongings["cheese"] +=1
                return self.player
            else:
                lose_steal_dialogue = "Too bad, you found nothing! Your efforts have been in vain!"
                return self.player
        #Action 4
        def ignore():

            dialogue = "You continue on your journey, oblivious to your surroundings."
            return self.player

#Testing Corner
jerry = Rat() 
tom = OtherRat()
print(tom.rat_encounter(jerry)) 
print(tom.steal_cheese().belongings)
