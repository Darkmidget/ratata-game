import random
from Hobo import Hobo
from Toad import Toad
from Ratata import Rat
from cat import Cat
import other_events
from rat import OtherRat

hobo = Hobo()
toad = Toad()
rat = Rat()
cat = Cat()



def event(rat):
    filth_chance = (rat.filth - 20)/100
    n = random.random()
    dialog = []
    options = []
    option_func = []
    if n <= filth_chance:
        dialog,options,option_func = filth_event(rat)
    else:
        dialog,options,option_func = other_event(rat)
    dialog.append(hunger_trigger(rat))
    dialog.append(filth_trigger(rat))
    return dialog, options, option_func

def other_event(rat):
    n = random.random()
    if not "cheese" in rat.belongings or rat.belongings["cheese"] < 2:
        shop_chance = 0
    else:
        shop_chance = 0.25
    if shop_chance > 0 and len(rat.rat_gang) > 0:
        flood_chance = 0.1
    else:
        flood_chance = 0.0
    theft_chance = 0.15
    pond_chance = 0.25
    if n <= shop_chance:
        return toad.shop(rat)
    elif n <= shop_chance + theft_chance:
        return other_events.theft(rat)
    elif n <= shop_chance + theft_chance + flood_chance:
        return other_events.flood(rat)
    elif n <= shop_chance + theft_chance + flood_chance + pond_chance:
         return other_events.pond(rat)
    else:
        other_rat = OtherRat()
        return other_rat.rat_encounter(rat)
    
def filth_event(rat):
    cat_chance = 0.5
    n = random.random()
    if n <= cat_chance:
        return cat.encounter(rat)
    else:
        return hobo.hobo_interact(rat)

def hunger_trigger(rat):
    if rat.hunger <= 0:
        rat.health  = rat.health - 15
        return "\nYou are malnourished, your consciousness is slowly fading. Life will drop by 1 every 10 seconds."
    elif rat.hunger < 25:
        rat.health  = rat.health - 1
        return "\nYou are desperate for food, you feel weak. Life will drop by 1 every minute."
    elif rat.hunger < 50:
        return "\nYour stomach is grumbling, you need to find food."
    elif rat.hunger < 75:
        return "\nYou are feeling peckish."
    else:
        return "\nYou don’t feel hungry."
    
def filth_trigger(rat):
    if rat.filth <= 25:
        return "\nYou are too clean for a rat, get filthy."
    elif rat.filth > 25:
        return "\nYou are moderately nasty."
    elif rat.filth > 50:
        return "\nYou are excessively foul smelling."
    elif rat.filth > 75:
        return "\nYou are the epitome of disgust, perfect."
    else:
        return "\n You are too clean for a rat. Go get filthy!"


#print(event(rat)[0])