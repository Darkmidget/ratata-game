from Ratata import Rat
import random

#i have no idea what the fk im doing
class OtherRat():
    def __init__(self):
       self.player = object()
       self.steal = False
       
    #Action 1
    def fight_rat(self, rat):
        win = True if random.random() <=0.3 + len(rat.rat_gang)/20 else False

        if win:
            rat.belongings["cheese"] += 1
            return rat
        else:
            rat.belongings["cheese"] -=1
            rat.rat_gang.clear()
            rat.health -=10
            return rat
    
    #Action 2
    def befriend_rat(self, rat):
        dialogue = "You decided to help a fellow rat, give one cheese."
        rat.belongings["cheese"] -=1
        rat.rat_gang.append("rat friend")
        return rat
  
    #Action 3
    def steal_cheese(self, rat):
        self.steal = True if random.random() <=0.5 else False
        if self.steal:
            rat.belongings["cheese"] +=1
            return rat
        else:
            return rat
        
    #Action 4
    def ignore(rat):
        return rat

    def response_dialogue(self):
        more_dialogues = []
        # Action 1 - post-dialogue
        more_dialogues.append("You sense an enemy Rat. Prepare to fight.")
        # Action 2 - post dialogue
        more_dialogues.append("You decided to help a fellow rat, give one cheese.")
        # Action 3 - post dialogue
        if self.steal:
            more_dialogues.append("You're a slick rat, you attempt to steal its cheese right under its snout.")
        else:
            more_dialogues.append("Too bad, you found nothing! Your efforts have been in vain!")
        # Action 4 - post dialogue
        more_dialogues.append("You continue on your journey, oblivious to your surroundings.")
        
        return more_dialogues
    
    def rat_encounter(self,player):

        self.player = player
        dialogue = ["You sense an enemy rat, prepare to fight."]
        options = ["Fight Rat", "Befriend Rat", "Steal Cheese", "Ignore"]
        option_func = [self.fight_rat, self.befriend_rat, self.steal_cheese, self.ignore]
        more_dialogues = self.response_dialogue()
        return dialogue, options, option_func, more_dialogues
    

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